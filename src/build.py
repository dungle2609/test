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
head = re.sub(r'<title>.*?</title>', '<title>Bức tranh chuyển đổi số ngành logistics — Base</title>', head, count=1, flags=re.S)
head = re.sub(r'<!--\n  DECK STARTER.*?-->', '''<!--
  Deck "Bức tranh chuyển đổi số ngành logistics" · tổng hợp case study · cập nhật 15/10/2026
  Dựng từ asset.base-2-0.html-deck-starter v1.1.0 (giữ nguyên engine và CSS gốc; bố cục riêng ở CSS mục 11).
  Ba phần: (1) vì sao logistics phải quan tâm công nghệ · (2A) nghiệp vụ đặc thù — dòng hàng · (2B) vận hành nội bộ — dòng việc, case khách hàng Base · (3) Base và Base 2.0.
  Mọi số liệu có dòng nguồn ở chân slide và mục Nguồn tham khảo cuối deck. Giao diện/mảnh dựng lại có nhãn "Minh hoạ".
  Phím: → tiếp · ← lùi · N ghi chú người nói · G tổng quan · F toàn màn hình · P chế độ in/PDF (rồi Ctrl/Cmd+P) · ? trợ giúp.
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
OUT.write_text(out, encoding='utf-8')
print('wrote', OUT, len(out), 'bytes; slides:', out.count('<section class="slide'))
