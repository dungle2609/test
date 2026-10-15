"""Dựng deck HTML "bức tranh chuyển đổi số ngành" từ bộ khung Base 2.0 Deck.

Cách dùng:
  python3 build.py <thư_mục_nguồn> <deck-starter.html> <file_ra.html> [--presenter] [--title "…"] [--footer "…"]

Thư mục nguồn cần có: slides.html (các <section class="slide">), extra.css (bố cục riêng),
mobile.css + mobile.js (giao diện đọc dọc cho điện thoại).

Mặc định dựng BẢN GỬI KHÁCH: bỏ ghi chú người nói và công cụ người trình bày, nhúng giao diện mobile
vào cùng file (điện thoại cầm dọc tự đổi sang bản đọc dọc). --presenter dựng bản trình bày có ghi chú.
Tiêu đề mặc định lấy từ <h1> đầu tiên; chân trang mobile lấy từ <p class="small"> đầu tiên.
"""
import re, sys, html, pathlib

args = sys.argv[1:]
PRESENTER = '--presenter' in args
def opt(name):
    if name in args:
        k = args.index(name); v = args[k + 1]; del args[k:k + 2]; return v
    return None
TITLE = opt('--title'); FOOTER = opt('--footer')
args = [a for a in args if a != '--presenter']
B, STARTER, OUT = pathlib.Path(args[0]), pathlib.Path(args[1]), pathlib.Path(args[2])
ASSETS = pathlib.Path(__file__).resolve().parent.parent / 'assets'
def src(name):
    """Lấy file từ thư mục nguồn; thiếu thì dùng bản chuẩn trong assets/ của kỹ năng."""
    p = B / name
    return p if p.exists() else ASSETS / name

s = STARTER.read_text(encoding='utf-8')
extra = src('extra.css').read_text(encoding='utf-8')
slides = (B / 'slides.html').read_text(encoding='utf-8')

def plain(fragment):
    t = re.sub(r'<br\s*/?>', ' ', fragment); t = re.sub(r'<[^>]+>', '', t)
    return re.sub(r'\s+', ' ', html.unescape(t)).strip()
if not TITLE:
    m = re.search(r'<h1[^>]*>(.*?)</h1>', slides, flags=re.S); TITLE = plain(m.group(1)) if m else 'Bức tranh chuyển đổi số'
if not FOOTER:
    m = re.search(r'<p class="small[^"]*"[^>]*>(.*?)</p>', slides, flags=re.S); FOOTER = plain(m.group(1)) if m else 'Base.vn'

head_end = s.index('</style>')
head = s[:head_end]
head = re.sub(r'<title>.*?</title>', '<title>' + html.escape(TITLE) + '</title>', head, count=1, flags=re.S)
head = re.sub(r'<!--\n  DECK STARTER.*?-->', '<!--\n  Deck "' + TITLE + '" · dựng từ asset.base-2-0.html-deck-starter (engine và CSS gốc giữ nguyên; bố cục riêng ở CSS mục 11).\n  ' + (
    'Bản trình bày: có ghi chú người nói (phím N).' if PRESENTER else
    'Bản gửi khách: không chứa ghi chú người nói. Điện thoại cầm dọc tự đổi sang giao diện đọc dọc nhúng trong cùng file.') +
    '\n  Phím: → tiếp · ← lùi · G mục lục · F toàn màn hình · P xem toàn bộ slide · ? trợ giúp.\n-->', head, count=1, flags=re.S)
head = head + extra + '\n'
rest = s[head_end:]
open_tag = '<div id="viewport"><div id="stage">'
close_tag = '</div></div>\n\n<div id="bar">'
i = rest.index(open_tag) + len(open_tag); j = rest.index(close_tag)
NO_ORPHAN = """<script>
/* Dự phòng cho trình duyệt chưa hỗ trợ text-wrap: pretty — nối hai chữ cuối để không có dòng chỉ một chữ */
(function(){if(window.CSS&&CSS.supports&&CSS.supports('text-wrap','pretty'))return;
  document.querySelectorAll('#stage h1,#stage h2,#stage h3,#stage p,#stage li,#stage small,#stage blockquote,#stage .who,#stage .nm,#stage .bl,#stage .mt,#stage .e,#stage .t,#stage .p,#stage .tm,#stage .out,#stage .st,#stage .co').forEach(function(el){
    if(el.closest('.notes'))return;var w=document.createTreeWalker(el,NodeFilter.SHOW_TEXT),n,last=null;
    while((n=w.nextNode())){if(/\\S\\s+\\S/.test(n.textContent))last=n}
    if(last)last.textContent=last.textContent.replace(/\\s+(\\S+\\s*)$/,'\\u00A0$1');});
})();
</script>
"""
rest = rest[:i] + '\n' + slides.rstrip() + '\n' + NO_ORPHAN + rest[j:]
out = head + rest

def sub1(a, b):
    global out
    assert out.count(a) == 1, a[:60]
    out = out.replace(a, b)

if not PRESENTER:
    # --- Bản gửi khách: bỏ ghi chú người nói và công cụ của người trình bày ---
    out = re.sub(r'\s*<aside class="notes">.*?</aside>', '', out, flags=re.S)
    sub1('<div id="hint">→ tiếp · ← lùi · N ghi chú · G tổng quan · ? trợ giúp</div>',
         '<div id="hint">Nhấp chuột hoặc bấm → để xem tiếp · ← lùi · G mục lục · F toàn màn hình</div>')
    sub1('  <dt>N</dt><dd>Ghi chú người nói + đồng hồ</dd>\n', '')
    sub1('  <dt>T · Shift+T</dt><dd>Chạy/dừng đồng hồ · đặt lại</dd>\n', '')
    sub1('  <dt>M</dt><dd>Đo toạ độ điểm nóng trên ảnh</dd>\n', '')
    sub1('<dt>G</dt><dd>Tổng quan, bấm để nhảy</dd>', '<dt>G</dt><dd>Mục lục, bấm để nhảy tới slide</dd>')
    sub1('<dt>P</dt><dd>Chế độ in/PDF (rồi Ctrl/Cmd+P)</dd>', '<dt>P</dt><dd>Xem toàn bộ slide liền mạch</dd>')
    sub1("  else if(k==='n'||k==='N'){b.classList.toggle('notes-on');fit()}\n", '')
    sub1("'<small>'+mmss(times[n])+(STEPS[n]?' · '+STEPS[n]+' bước':'')+'</small>'", "''")
    sub1(':root{\n', ':root{\n  color-scheme:dark;\n')

    # --- Một file cho cả máy tính và điện thoại: điện thoại cầm dọc bật giao diện đọc dọc nhúng sẵn ---
    sub1('<style>\n', """<script>/* điện thoại cầm dọc: bật giao diện đọc dọc nhúng sẵn trong file */
(function(){try{if(innerWidth<760&&innerHeight>innerWidth&&location.hash!=='#deck')document.documentElement.classList.add('m','js')}catch(e){}})();</script>
<style>\n""")

    def scope(css):
        """Gắn tiền tố html.m cho mọi bộ chọn của mobile.css để chỉ áp dụng ở giao diện điện thoại."""
        rules = []; i = 0
        while i < len(css):
            j = css.find('{', i)
            if j < 0: rules.append(css[i:]); break
            sel = css[i:j]
            if sel.strip().startswith('@keyframes'):
                depth = 0; k = j
                while True:
                    if css[k] == '{': depth += 1
                    elif css[k] == '}':
                        depth -= 1
                        if depth == 0: break
                    k += 1
                rules.append(css[i:k + 1]); i = k + 1; continue
            k = css.index('}', j)
            comments = re.findall(r'/\*.*?\*/', sel, flags=re.S); bare = re.sub(r'/\*.*?\*/', '', sel, flags=re.S)
            parts = []
            for p in bare.split(','):
                p = p.strip()
                if not p: continue
                if p == 'html': parts.append('html.m')
                elif p.startswith('html.') or p.startswith('html:'): parts.append('html.m' + p[4:])
                else: parts.append('html.m ' + p)
            rules.append(''.join(c + '\n' for c in comments) + ','.join(parts) + css[j:k + 1])
            i = k + 1
        return '\n'.join(r.strip('\n') for r in rules if r.strip())

    mcss = scope(src('mobile.css').read_text(encoding='utf-8')) + """
#mtop,#mlist,.mfoot{display:none}
html.m #mlist{display:block}
html.m #mlist[hidden]{display:none}
html.m .mfoot{display:block}
html.m #viewport{position:static;inset:auto;overflow:visible}
html.m #bar,html.m #dots,html.m #counter,html.m #hint,html.m #notes,html.m #overview,html.m #help,html.m #mlabel{display:none!important}
"""
    sub1('</style>', mcss + '\n</style>')
    sub1('<div id="viewport"><div id="stage">', '<header id="mtop"><button id="mtoc" type="button" aria-label="Mục lục" aria-expanded="false" aria-controls="mlist">☰</button><div class="mt"><span id="mttl">' + html.escape(TITLE) + '</span><span id="mcnt"></span></div><i id="mbar"></i></header>\n<nav id="mlist" hidden></nav>\n<div id="viewport"><div id="stage">')
    sub1('</div></div>\n\n<div id="bar">', '</div></div>\n<p class="mfoot">' + html.escape(FOOTER) + '</p>\n\n<div id="bar">')
    sub1("\n(function(){\n'use strict';\nvar stage=document.getElementById('stage');", "\nif(!document.documentElement.classList.contains('m'))(function(){\n'use strict';\nvar stage=document.getElementById('stage');")
    prelude = """if(document.documentElement.classList.contains('m')){
/* chuẩn bị cho giao diện đọc dọc: tiêu đề chỉ giữ xuống dòng ở ranh giới câu, thêm gợi ý cuộn */
[].slice.call(document.querySelectorAll('#stage h1,#stage h2')).forEach(function(h){h.innerHTML=h.innerHTML.replace(/([^.?!])<br>/g,'$1 ')});
(function(){var f=document.querySelector('#stage > .slide');if(f){var c=document.createElement('p');c.className='mcue';c.textContent='Kéo xuống để xem ↓';f.appendChild(c)}})();
"""
    sub1('</body>', '<script>\n' + prelude + src('mobile.js').read_text(encoding='utf-8') + '\n}\n</script>\n</body>')

OUT.write_text(out, encoding='utf-8')
print('wrote', OUT, len(out.encode('utf-8')), 'bytes; slides:', out.count('<section class="slide'), '; mode:', 'presenter' if PRESENTER else 'client')
