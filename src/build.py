import re, sys, pathlib
B = pathlib.Path(sys.argv[1])            # build dir
STARTER = pathlib.Path(sys.argv[2])      # deck-starter.html
OUT = pathlib.Path(sys.argv[3])
s = STARTER.read_text(encoding='utf-8')
extra = (B/'extra.css').read_text(encoding='utf-8')
slides = (B/'slides.html').read_text(encoding='utf-8')

head_end = s.index('</style>')
head = s[:head_end]
# title + header comment
head = re.sub(r'<title>.*?</title>', '<title>Bức tranh chuyển đổi số ngành logistics</title>', head, count=1, flags=re.S)
head = re.sub(r'<!--\n  DECK STARTER.*?-->', '''<!--
  Deck "Bức tranh chuyển đổi số ngành logistics" · tổng hợp case study · cập nhật 15/10/2026
  Dựng từ asset.base-2-0.html-deck-starter v1.1.0 (giữ nguyên engine và CSS gốc; bố cục riêng ở CSS mục 11).
  Ba phần: (1) vì sao logistics phải quan tâm công nghệ · (2A) nghiệp vụ đặc thù — dòng hàng · (2B) vận hành nội bộ — dòng việc, case khách hàng Base · (3) Base và Base 2.0.
  Mọi số liệu có dòng nguồn ở chân slide và mục Nguồn tham khảo cuối deck. Giao diện/mảnh dựng lại có nhãn "Minh hoạ".
  Bản gửi khách: không chứa ghi chú người nói (ghi chú nằm trong src/slides.html). Điện thoại cầm dọc tự đổi sang giao diện đọc dọc nhúng trong cùng file.
  Phím: → tiếp · ← lùi · G mục lục · F toàn màn hình · P xem toàn bộ slide · ? trợ giúp.
-->''', head, count=1, flags=re.S)
head = head + extra + '\n'
rest = s[head_end:]
# body: replace content between stage open and stage close
open_tag = '<div id="viewport"><div id="stage">'
close_tag = '</div></div>\n\n<div id="bar">'
i = rest.index(open_tag) + len(open_tag)
j = rest.index(close_tag)
rest = rest[:i] + '\n' + slides + '\n' + rest[j:]
out = head + rest
# --- Bản gửi khách: bỏ ghi chú người nói và công cụ của người trình bày; điện thoại dọc chuyển sang bản mobile ---
out = re.sub(r'\s*<aside class="notes">.*?</aside>', '', out, flags=re.S)
def sub1(a, b):
    global out
    assert out.count(a) == 1, a[:60]
    out = out.replace(a, b)
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
# --- Một file dùng cho cả máy tính và điện thoại: điện thoại cầm dọc chuyển sang giao diện đọc dọc (cùng nội dung, cùng hiệu ứng) ---
sub1('<style>\n', """<script>/* điện thoại cầm dọc: bật giao diện đọc dọc nhúng sẵn trong file */
(function(){try{if(innerWidth<760&&innerHeight>innerWidth&&location.hash!=='#deck')document.documentElement.classList.add('m','js')}catch(e){}})();</script>
<style>\n""")
mobile_css = (B/'mobile.css').read_text(encoding='utf-8')
def scope(css):
    out_rules = []; i = 0
    while i < len(css):
        j = css.find('{', i)
        if j < 0: out_rules.append(css[i:]); break
        sel = css[i:j]; 
        if sel.strip().startswith('@keyframes'):
            depth = 0; k = j
            while True:
                if css[k] == '{': depth += 1
                elif css[k] == '}':
                    depth -= 1
                    if depth == 0: break
                k += 1
            out_rules.append(css[i:k+1]); i = k+1; continue
        k = css.index('}', j)
        comments = re.findall(r'/\*.*?\*/', sel, flags=re.S); bare = re.sub(r'/\*.*?\*/', '', sel, flags=re.S)
        parts = []
        for p in bare.split(','):
            p = p.strip()
            if not p: continue
            if p == 'html': parts.append('html.m')
            elif p.startswith('html.') or p.startswith('html:'): parts.append('html.m' + p[4:])
            elif p.startswith('body'): parts.append('html.m ' + p)
            else: parts.append('html.m ' + p)
        out_rules.append(''.join(c + '\n' for c in comments) + ','.join(parts) + css[j:k+1])
        i = k+1
    return '\n'.join(r.strip('\n') for r in out_rules if r.strip())
mcss = scope(mobile_css) + """
#mtop,#mlist,.mfoot{display:none}
html.m #mlist{display:block}
html.m #mlist[hidden]{display:none}
html.m .mfoot{display:block}
html.m #viewport{position:static;inset:auto;overflow:visible}
html.m #bar,html.m #dots,html.m #counter,html.m #hint,html.m #notes,html.m #overview,html.m #help,html.m #mlabel{display:none!important}
"""
sub1('</style>', mcss + '\n</style>')
sub1('<div id="viewport"><div id="stage">', '<header id="mtop"><button id="mtoc" type="button" aria-label="Mục lục" aria-expanded="false" aria-controls="mlist">☰</button><div class="mt"><span id="mttl">Bức tranh chuyển đổi số ngành logistics</span><span id="mcnt"></span></div><i id="mbar"></i></header>\n<nav id="mlist" hidden></nav>\n<div id="viewport"><div id="stage">')
sub1('</div></div>\n\n<div id="bar">', '</div></div>\n<p class="mfoot">Base.vn · Tài liệu tham khảo cho doanh nghiệp logistics · 10/2026</p>\n\n<div id="bar">')
sub1("\n(function(){\n'use strict';\nvar stage=document.getElementById('stage');", "\nif(!document.documentElement.classList.contains('m'))(function(){\n'use strict';\nvar stage=document.getElementById('stage');")
mobile_js = (B/'mobile.js').read_text(encoding='utf-8')
prelude = """if(document.documentElement.classList.contains('m')){
/* chuẩn bị cho giao diện đọc dọc: tiêu đề chỉ giữ xuống dòng ở ranh giới câu, thêm gợi ý cuộn */
[].slice.call(document.querySelectorAll('#stage h1,#stage h2')).forEach(function(h){h.innerHTML=h.innerHTML.replace(/([^.?!])<br>/g,'$1 ')});
(function(){var f=document.querySelector('#stage > .slide');if(f){var c=document.createElement('p');c.className='mcue';c.textContent='Kéo xuống để xem ↓';f.appendChild(c)}})();
"""
sub1('</body>', '<script>\n' + prelude + mobile_js + '\n}\n</script>\n</body>')
OUT.write_text(out, encoding='utf-8')
print('wrote', OUT, len(out), 'bytes; slides:', out.count('<section class="slide'))
