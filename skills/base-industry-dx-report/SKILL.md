---
name: base-industry-dx-report
description: >-
  Thiết kế và dựng tài liệu HTML "Bức tranh chuyển đổi số ngành …" cho Base.vn — tổng hợp bối cảnh chuyển đổi số của một ngành, bài toán đặc thù và giải pháp công nghệ chuyên ngành, use-case khách hàng Base trong ngành, phạm vi Base đáp ứng và tầm nhìn Base 2.0 — thành một file HTML duy nhất: trên máy tính là deck trình chiếu có hiệu ứng từng bước (hệ thiết kế Base 2.0 Deck), trên điện thoại tự đổi sang giao diện đọc dọc có hiệu ứng riêng, kèm PDF dự phòng. LUÔN dùng skill này khi người dùng muốn "tổng hợp case study ngành", "bức tranh chuyển đổi số ngành X", "tài liệu use-case theo ngành", "Base ứng dụng được gì cho ngành X", "deck ngành cho khách", "làm lại file như bản logistics cho ngành khác", hoặc gửi một bản nháp/tài liệu ngành và muốn dựng lại thành HTML có hiệu ứng để gửi khách — kể cả khi họ chỉ nói tên ngành.
---

# Bức tranh chuyển đổi số theo ngành — tài liệu HTML có hiệu ứng

Kỹ năng này đóng gói cách đã làm bản **"Bức tranh chuyển đổi số ngành logistics"** (10/2026) cùng toàn bộ góp ý của người dùng trong quá trình sửa. Đầu ra là **một file HTML duy nhất để gửi khách**:

- **Máy tính / điện thoại xoay ngang:** deck 1600×900 theo hệ thiết kế Base 2.0 Deck, bấm từng bước, mục lục (G), xem toàn bộ (P).
- **Điện thoại cầm dọc:** cùng nội dung, tự đổi sang giao diện đọc dọc với hiệu ứng thiết kế riêng cho mobile.
- **PDF** dự phòng (31 trang 1600×900) và **bản trình bày có ghi chú người nói** chỉ dùng nội bộ.

Mẫu hoàn chỉnh để chép: `assets/example-logistics/slides.html`. Kỹ năng này dựa trên skill `base-2-0-html-deck` (hệ thiết kế, cách kể, tri thức nền Base 2.0); có skill đó thì đọc thêm khi cần, không có thì mọi thứ cần dùng đã nằm trong thư mục này.

## Khi nào dùng / không dùng

| Tình huống | Làm gì |
|---|---|
| Tổng hợp chuyển đổi số + use-case Base cho **một ngành** (logistics, sản xuất, bán lẻ, xây dựng, F&B, dược…) | Dùng kỹ năng này |
| Deck cho **một khách cụ thể** (đặt vấn đề, demo theo pain đã discovery) | Dùng `base-2-0-html-deck` |
| Khảo sát discovery trước buổi gặp | Dùng `base-discovery-survey` |
| Cần .pptx / Google Slides | Kỹ năng này không làm; nói rõ và chuyển cách làm |

## Đầu vào cần chốt

Hỏi **một lần** chỉ những thứ làm đổi hướng kết quả; còn lại giả định an toàn và ghi rõ là giả định:

1. **Ngành** và phạm vi (ví dụ: logistics gồm vận tải, kho, cảng, giao nhận, chuyển phát).
2. **Người đọc**: mặc định là chủ doanh nghiệp / ban lãnh đạo trong ngành, nhận file qua Zalo/email.
3. **Danh sách khách Base trong ngành** người dùng muốn nêu tên, kèm phạm vi Base họ dùng nếu chưa công bố.
4. **Số khách hàng Base hiện tại** (bản logistics 10/2026 dùng **12.000+** theo người dùng) — hỏi lại nếu đã qua vài tháng.
5. Tài liệu sẵn có: bản nháp cũ (ví dụ bản Codex), bộ giải pháp Base cho ngành trong Drive (`[Shared] <Ngành>`), quy trình mẫu.

## Quy trình

1. **Nghiên cứu** theo `references/research.md`: số liệu ngành, mức độ số hoá, chính sách, câu nói của lãnh đạo doanh nghiệp, công nghệ chuyên ngành có số liệu, case khách hàng Base trong ngành. Ghi mỗi số kèm nguồn, ngày, đường dẫn vào một bảng nguồn.
2. **Tách hai dòng chảy** của ngành trước khi viết: *dòng nghiệp vụ đặc thù* (thứ chỉ ngành đó có, do phần mềm chuyên ngành lo) và *dòng việc* (vận hành nội bộ: báo giá, phê duyệt, chứng từ, giao việc… — phần Base lo). Với logistics: "dòng hàng" và "dòng việc". Đặt tên dòng đặc thù theo ngôn ngữ của ngành (sản xuất: "dòng sản xuất"; xây dựng: "dòng công trình"; bán lẻ: "dòng hàng hoá").
3. **Viết câu chuyện** theo khung 3 phần trong `references/blueprint.md`. Đọc riêng các tiêu đề slide phải thành một lập luận.
4. **Dựng nội dung**: tạo thư mục làm việc, chép `assets/example-logistics/slides.html` thành `slides.html` rồi viết lại từng `<section class="slide">` theo ngành mới. Giữ class và cấu trúc thành phần (xem bảng thành phần bên dưới) để CSS máy tính và mobile chạy đúng. Muốn chỉnh bố cục thì chép `assets/extra.css` / `assets/mobile.css` vào thư mục làm việc rồi sửa (build tự ưu tiên file trong thư mục làm việc).
5. **Build**:
   ```bash
   python3 scripts/build.py <thư_mục_làm_việc> assets/deck-starter.html <ra>.html                # bản gửi khách
   python3 scripts/build.py <thư_mục_làm_việc> assets/deck-starter.html <ra>-trinh-bay.html --presenter  # có ghi chú
   ```
   Tiêu đề trang lấy từ `<h1>` đầu tiên, chân trang mobile lấy từ `<p class="small">` đầu tiên (đổi bằng `--title`, `--footer`).
6. **Kiểm** (mục Kiểm thử) và **nhìn ảnh chụp** từng slide máy tính và mobile một lượt; sửa rồi kiểm lại.
7. **Xuất PDF** bằng `check_deck.js … <file.pdf>` (chế độ in của deck, mỗi slide một trang, trạng thái cuối).
8. **Giao** (mục Giao hàng).

## Khung nội dung: 3 phần trả lời 3 câu hỏi

| Phần | Câu hỏi người đọc | Các slide (chi tiết, ví dụ và cách chuyển ngành: `references/blueprint.md`) |
|---|---|---|
| Mở | — | Bìa "Bức tranh chuyển đổi số ngành X" · "Tài liệu giúp trả lời 3 câu hỏi" |
| 1 · Bối cảnh | Vì sao chủ doanh nghiệp ngành X phải quan tâm? | Chương · Chi phí/áp lực (3 số lớn) · Mức độ số hoá (thanh %) · Kết quả của những quyết định dựa trên dữ liệu · Cơ hội (3 thẻ + chính sách) · "Vậy thì… nên ứng dụng công nghệ như thế nào?" (đứng ngoài ✕ / làm vội !) · Lãnh đạo ngành nói gì (4 câu) · "Câu hỏi không còn là có làm không?" |
| 2 · Bài toán và lời giải | Công nghệ nói chung, và Base nói riêng, giúp được gì? | Chương · Hai dòng chảy · **2A** 5 bài toán đặc thù → công nghệ → doanh nghiệp đã làm (**chưa nói Base**) · Base chạy song song, không thay phần mềm chuyên ngành · **2B** việc chạy trên Zalo/Excel/giấy (mảnh giao diện) · 6 vấn đề vận hành chung · Nguyên lý: người giữ – hạn – đầu ra · Case 1–3 có số liệu · Ghi nhận từ khách hàng (báo cáo chính thức) · Ngành × Base: ứng dụng Base để làm gì? · Hai lớp phần mềm nối với nhau |
| 3 · Base | Tầm nhìn của Base khác gì phần mềm khác? | Chương · Base tổng quan · Thêm app, thêm AI chưa làm tổ chức giỏi hơn · Kiến trúc Service → Output → Knowledge → Agent (ví dụ của ngành) · Khác biệt so với phần mềm theo app trên thị trường · Bản đồ Base 2.0 cho dòng việc |
| Đóng | — | Kết cộng dồn (gọi lại hình ảnh mở bài) · Nguồn tham khảo có đường dẫn |

Không thêm slide "Bước tiếp theo" (người dùng đã bỏ ở bản logistics). Khoảng 30 slide, ~25 phút trình bày.

## Luật câu chữ — đúc kết từ góp ý của người dùng

Đây là phần quan trọng nhất; mỗi luật đến từ một lần người dùng sửa thật.

- **Ngắn trước, dài sau trên mọi slide**: nhãn nhỏ → tiêu đề là kết luận (≤ 2 dòng) → thẻ/khối nội dung → một câu dẫn dài hơn → dòng nguồn. Người đọc lướt tiêu đề vẫn hiểu.
- **Đọc một lần là hiểu.** Tránh tiêu đề ẩn ý hay chơi chữ. Những câu đã bị người dùng đánh giá "tối nghĩa" và câu thay thế:

  | Đã viết | Người dùng sửa thành |
  |---|---|
  | Hai doanh nghiệp *tự ghi* vào báo cáo của mình | Ghi nhận từ khách hàng |
  | Hệ chuyên ngành ở lại. Base đứng cạnh. | Base chạy song song, không thay phần mềm chuyên ngành |
  | Rủi ro có ở cả hai phía | (nhãn "Vậy thì") Doanh nghiệp logistics nên ứng dụng công nghệ như thế nào? |
  | Đi trước bằng dữ liệu, chênh lệch rất rõ | Kết quả của những quyết định dựa trên dữ liệu |
  | Khoảng cách hơn 6 điểm phần trăm không tự thu hẹp. Nó nằm ở… | Phần chênh lệch nằm ở những chỗ quen thuộc: xe chạy rỗng, xe chờ ở cảng, chứng từ làm lại. |
  | Không chỉ là chuyện của tập đoàn đa quốc gia. Phần 2 là các con số tương tự… | Ở Việt Nam, cảng, kho và bưu cục cũng đã có con số tương tự — xem phần 2. |
  | Đi kèm: đưa Việt Nam vào nhóm 40 nước… LPI… | Chính sách cũng đẩy cùng chiều: mục tiêu đưa logistics Việt Nam từ hạng 43 lên nhóm 40 nước dẫn đầu thế giới (…) |
  | Chưa có con số cuối, nhưng hướng đi đã rõ | Doanh nghiệp logistics ứng dụng Base để làm gì? (nhãn "Logistics × Base") |
  | Hai lớp, cần cả hai — và nối với nhau | Hai lớp phần mềm nối với nhau |
  | Khác phần mềm theo từng app ở đâu | Khác biệt so với phần mềm theo app trên thị trường |

- **Câu hỏi dùng dấu "?"**, kể cả tiêu đề kiểu "Câu hỏi không còn là có làm không?".
- **Không dòng nào chỉ có một chữ**, ở mọi kích thước màn hình. Build đã bật `text-wrap: balance/pretty` và script dự phòng; khi còn sót, nối hai chữ cuối bằng `&nbsp;` hoặc viết lại câu. **Không tách từ ghép** qua hai dòng: `quy&nbsp;trình`, `đào&nbsp;tạo`, `hiệu&nbsp;quả`, `doanh&nbsp;nghiệp` khi rơi vào chỗ ngắt.
- **Không đặt lời rào đón về nguồn lên slide.** Người xem không cần đọc "không phải bài quảng cáo của Base", "ước tính của doanh nghiệp", "chưa có KPI riêng", "số giờ là SLA mẫu". Dòng nguồn chỉ ghi tên nguồn; lưu ý về độ tin cậy để trong ghi chú người nói.
- **Không viết "Có dùng Base".** Ghi Base được dùng để làm gì: "Văn phòng điện tử · giao việc", "CRM · dữ liệu xe, đối tác", "Quản trị · phê duyệt".
- **Doanh nghiệp chưa có bài công bố chi tiết**: gom thành một dòng chip có nhãn mô tả việc dùng (bản logistics: "Xây dựng văn phòng làm việc điện tử: Logistics Đông Á · DPL · PCT · PCL").
- **Từ nghề Sales giữ nguyên** (deal, lead, case study, CRM…); thuật ngữ kỹ thuật lần đầu giải nghĩa tiếng Việt (TOS, WMS, TMS, eDO…).
- **Ghi chú người nói** (`<aside class="notes">`): câu ngắn, xưng em – anh/chị, `<i>[bấm]</i>` đúng chỗ bấm, chỉ dẫn sân khấu trong ngoặc, lưu ý nội bộ trong ngoặc nghiêng.

## Trung thực và nguồn

- **Số nào cũng có nguồn**; số không tự kiểm được thì bỏ, kể cả khi bản nháp cũ có (bản logistics đã bỏ "lỗi điều xe 322 → 69", "năng suất soạn hàng +20–30%" vì không đối chiếu được).
- **Đừng quy kết quả của cả chương trình cho riêng Base**: ghi nhãn đúng ngay trên số ("+50% tốc độ vận hành *sau chương trình số hoá*"), phần chi tiết để ghi chú người nói.
- **Bằng chứng mạnh nhất là tài liệu chính thức của khách**: báo cáo thường niên, tài liệu đại hội cổ đông của doanh nghiệp niêm yết có nhắc Base. Trích nguyên văn, ghi trang.
- **Claim về Base 2.0** đi theo thang xác minh của `base-2-0-html-deck` (phù hợp phương pháp luận / đã thấy trên giao diện, có ngày / đã chứng minh ở khách). Trên slide chỉ ghi kiến trúc Base công bố và ví dụ ngành có nhãn "Ví dụ"; mức xác minh ghi trong ghi chú.
- **Mảnh giao diện dựng lại** (Zalo, Excel, email, phiếu giấy) mang dòng "Hình minh hoạ tình huống thường gặp", không dùng logo app, không dùng dữ liệu thật của khách.
- **Phạm vi Base của khách chưa công bố** lấy theo người dùng: ghi trong ghi chú là "thông tin nội bộ Base", và nhắc người dùng xin phép trước khi nêu tên ra ngoài.

## Thiết kế và dựng

- **Hệ thiết kế**: Base 2.0 Deck (`assets/deck-starter.html`: token màu, chữ, engine bước bấm, chế độ in). Nền tối cho lập luận; màu trạng thái giữ nghĩa cố định (xanh = kết quả/xong, đỏ = lỗi/vấn đề, vàng = chờ/cảnh báo). Màu teal `--goods` cho dòng đặc thù, `--accent` cho dòng việc/Base, `--accent-2` cho phần Base 2.0.
- **Tiếng Việt**: tiêu đề line-height ≥ 1.15, tracking ≥ −0,02em, tối đa 2 dòng; dùng `<br>` chủ động ở ranh giới cụm từ để tiêu đề ngắt đẹp (bản mobile chỉ giữ `<br>` sau dấu câu).
- **Bước bấm**: `data-step="k"` cho khối hiện ở lần bấm k; `rv` + `style="--i:n"` cho khối trồi lên khi vào slide; không gắn cả hai trên một phần tử. Slide dày chữ dùng `class="slide top"`.
- **Dòng nguồn**: `<p class="srcline"><b>Nguồn:</b> …</p>` ở cuối mỗi slide có số liệu.
- **Thành phần** (CSS ở `assets/extra.css`, markup mẫu trong `assets/example-logistics/slides.html`):

  | Class | Dùng cho |
  |---|---|
  | `.kpis > .kpi` (`b`, `span`, `small`) | 3 con số lớn (chi phí, lợi ích, Base tổng quan) |
  | `.meter` (`.barx .seg.a/.b`, `.n3 .nt`) | Thanh tỷ lệ mức độ số hoá |
  | `.cards > .card` | 3 câu hỏi, 3 cơ hội, 3 khoảng trống |
  | `.versus.dense` (`.vcol.them` / `.vcol`) | Đứng ngoài ✕ / làm vội ! |
  | `.quotes.q4 > .quote` | 4 câu nói lãnh đạo (`.who` + `.av`) |
  | `.lanes > .lane(.work)` | Hai dòng chảy |
  | `.mx` (`.hd`, `.r > .p/.t/.e`) | Ma trận bài toán → công nghệ → doanh nghiệp |
  | `.stk` (`.r > .co + .chips + .chips`, `.chp`, `.chp.base`) | Phần mềm chuyên ngành song song Base |
  | `.mess.apps` (`.win.zl/.xl/.ml/.pp`, `.frag.note`, `.flag`) | Việc chạy trên Zalo/Excel/email/giấy |
  | `.ops > .op` | 6 vấn đề vận hành, dòng "Gặp ở" |
  | `.chain > .cn`, `.rules > .rule` | Quy trình mẫu: người giữ, hạn, đầu ra |
  | `.story` (`.id` + `.bd .blk(.res)` + `.qline`) | Case có số liệu |
  | `.duo > .dcol` + `blockquote` | Ghi nhận từ báo cáo khách hàng |
  | `.jr > .jc` + `.also .chp.plain` | Ngành × Base, dòng chip doanh nghiệp |
  | `.scope > .sc(.work)` + `.band` | Hai lớp phần mềm nối với nhau |
  | `.arch > .ly` + `.loop` | Kiến trúc bốn lớp |
  | `.mp > .mrow(.ai/.ext)` | Bản đồ Base 2.0 cho ngành |
  | `.stack` | Kết cộng dồn |
  | `.refs` (`.refh`, `li > em + a`) | Nguồn tham khảo |

## Giao diện điện thoại (nhúng trong cùng file)

- Build gắn class `html.m` khi màn hình < 760px và cầm dọc (thêm `#deck` vào đường dẫn để ép xem deck). Toàn bộ `mobile.css` được tự gắn tiền tố `html.m`, engine deck không chạy, `mobile.js` chạy thay.
- **Không dùng hiệu ứng bấm-từng-bước của deck trên điện thoại** — người dùng đã thấy "không khớp, không hay". Hiệu ứng mobile được thiết kế riêng:
  - Khối hiện khi cuộn tới, ~0,45s, trồi ngắn, không nhoè; khối vào cùng lúc so le 70ms.
  - Kiểu theo loại nội dung: thẻ trồi lên; danh sách, câu nói, case trượt từ trái; mảnh Zalo/Excel/email/giấy trượt vào xen kẽ như thông báo, tin nhắn hiện từng dòng, ô "?" nháy đỏ, cờ cảnh báo bật lên.
  - Số dạng `16,8%`, `−15%`, `+65%`, `12.000+` đếm lên (năm, khoảng, "3 tháng" giữ nguyên); thanh % tự đầy; các bước "dòng hàng/dòng việc" sáng lần lượt; khối "Kết quả" loé xanh một lần.
  - Câu kết sáng theo vị trí cuộn; số chương mờ trôi nhẹ; thanh trên cùng có tên phần, số thứ tự, tiến độ, nút ☰ mục lục.
  - Giảm chuyển động (prefers-reduced-motion): hiện ngay trạng thái cuối.
- Thêm thành phần mới thì bổ sung bố cục một cột trong `mobile.css` và nhóm hiệu ứng trong `GROUPS` của `mobile.js`.

## Kiểm thử (bắt buộc trước khi giao)

```bash
node scripts/check_deck.js <ra>.html <thư_mục_ảnh> <ra>.pdf   # máy tính: mọi bước, tràn khung, dòng nguồn, tiêu đề ≤2 dòng, dòng một chữ, chế độ in, xuất PDF
node scripts/check_mobile.js <ra>.html <thư_mục_ảnh>            # điện thoại 390px và 360px: bật giao diện dọc, mọi khối hiện, không cuộn ngang, dòng một chữ
```
Cả hai phải ra ✓ và mã thoát 0. Sau đó xem ảnh chụp: mỗi slide một lượt ở máy tính, các phần dày ở mobile (mảnh giao diện, ma trận, case). Lỗi thường gặp: tiêu đề ngắt giữa từ ghép, nhãn `.flag` đè lên mảnh giao diện, nội dung chạm dòng nguồn ở slide dày (chuyển sang `slide top` hoặc rút chữ).

## Giao hàng

- **Bản gửi khách** (mặc định): một file HTML không có ghi chú người nói — gửi thẳng qua Zalo/email, mở bằng trình duyệt là chạy, không cần mạng. Muốn đường link web thì cần nơi lưu trữ chạy được HTML (GitHub Pages, Netlify); Google Drive không chạy file HTML. Chỉ đăng Artifact khi người dùng muốn.
- **Bản trình bày** (`--presenter`): có ghi chú, phím N — chỉ dùng nội bộ, không gửi khách.
- **PDF** dự phòng.
- **Báo lại người dùng** ngắn gọn, kết luận trước: file nào để làm gì; kết quả kiểm thử; danh sách cần chốt (số liệu cần mở link kiểm lại, tên doanh nghiệp cần xin phép nêu, phạm vi Base theo thông tin nội bộ).

## Checklist cuối

- [ ] Đọc riêng các tiêu đề thành một lập luận 3 phần; mỗi tiêu đề đọc một lần là hiểu.
- [ ] 2A không nhắc Base; 2B mỗi vấn đề có doanh nghiệp "Gặp ở"; case có số liệu đủ Bài toán / Cách làm / Kết quả.
- [ ] Mọi số có nguồn; không có lời rào đón về nguồn trên slide; không có "Có dùng Base".
- [ ] Không dòng một chữ, không tách từ ghép, câu hỏi có "?".
- [ ] `check_deck.js` và `check_mobile.js` đều ✓; đã xem ảnh chụp.
- [ ] Bản gửi khách không có ghi chú; PDF đủ trang.
