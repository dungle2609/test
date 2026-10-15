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
  Bản gửi khách: không chứa ghi chú người nói (ghi chú nằm trong src/slides.html). Điện thoại cầm dọc tự mở bản mobile.
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
sub1('<style>\n', """<script>/* điện thoại cầm dọc: mở bản đọc dọc tối ưu cho mobile */
(function(){try{if(innerWidth<760&&innerHeight>innerWidth&&location.hash!=='#deck')location.replace('logistics-chuyen-doi-so-base-mobile.html')}catch(e){}})();</script>
<style>\n""")
OUT.write_text(out, encoding='utf-8')
print('wrote', OUT, len(out), 'bytes; slides:', out.count('<section class="slide'))
