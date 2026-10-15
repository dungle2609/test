import re, sys, pathlib
B = pathlib.Path(sys.argv[1]); STARTER = pathlib.Path(sys.argv[2]); OUT = pathlib.Path(sys.argv[3])
st = STARTER.read_text(encoding='utf-8')
css_core = st[st.index('<style>')+7 : st.index('/* ============ 6. DEMO')]
css_rm = st[st.index('/* ============ 10. GIẢM CHUYỂN ĐỘNG'): st.index('</style>')]
extra = (B/'extra.css').read_text(encoding='utf-8')
mobile = (B/'mobile.css').read_text(encoding='utf-8')
js = (B/'mobile.js').read_text(encoding='utf-8')
slides = (B/'slides.html').read_text(encoding='utf-8')
# bản đọc: bỏ ghi chú người nói (có ghi chú nội bộ), bỏ xuống dòng cưỡng bức trong tiêu đề
slides = re.sub(r'\s*<aside class="notes">.*?</aside>', '', slides, flags=re.S)
def nobr(m): return m.group(0).replace('<br>', ' ')
# tiêu đề: giữ <br> ở ranh giới câu (sau . ? !), các chỗ khác để trình duyệt tự cân dòng theo bề ngang điện thoại
def fixbr(m): return re.sub(r'(?<![.?!])<br>', ' ', m.group(0))
slides = re.sub(r'<h[12][^>]*>.*?</h[12]>', fixbr, slides, flags=re.S)
# gợi ý cuộn ở phần mở đầu
first_end = slides.index('</section>')
slides = slides[:first_end] + '  <p class="mcue">Kéo xuống để xem ↓</p>\n' + slides[first_end:]
html = f'''<!doctype html>
<html lang="vi">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="theme-color" content="#070B1D">
<title>Bức tranh chuyển đổi số ngành logistics — Base</title>
<!--
  Bản mobile của deck "Bức tranh chuyển đổi số ngành logistics" · cập nhật 15/10/2026
  Cùng nguồn nội dung với bản trình chiếu (slides.html); đọc dọc, hiệu ứng hiện dần khi cuộn.
  Bản này không chứa ghi chú người nói.
-->
<script>document.documentElement.classList.add('js')</script>
<style>
{css_core}
{css_rm}
{extra}
{mobile}
</style>
</head>
<body>
<header id="mtop"><button id="mtoc" type="button" aria-label="Mục lục" aria-expanded="false" aria-controls="mlist">☰</button><div class="mt"><span id="mttl">Bức tranh chuyển đổi số ngành logistics</span><span id="mcnt"></span></div><i id="mbar"></i></header>
<nav id="mlist" hidden></nav>
<main id="stage">
{slides}
</main>
<p class="mfoot">Base.vn · Tài liệu tham khảo cho doanh nghiệp logistics · 10/2026</p>
<script>
{js}
</script>
</body>
</html>
'''
OUT.write_text(html, encoding='utf-8')
print('wrote', OUT, len(html.encode('utf-8')), 'bytes; sections:', html.count('<section class="slide'))
