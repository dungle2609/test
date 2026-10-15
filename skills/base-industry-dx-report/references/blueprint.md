# Khung slide chi tiết — "Bức tranh chuyển đổi số ngành X"

Mỗi dòng: **slide · mục đích · thành phần · nội dung bắt buộc · ví dụ bản logistics (10/2026) · chuyển sang ngành khác**. Markup đầy đủ của từng slide nằm trong `assets/example-logistics/slides.html` (tìm theo `data-title`).

Nguyên tắc chung: mỗi slide một kết luận; đi từ chữ ngắn đến chữ dài; số liệu có dòng nguồn; ghi chú người nói chứa phần "nếu khách hỏi".

## Mở

| # | Slide | Thành phần | Nội dung | Ví dụ logistics | Chuyển ngành |
|---|---|---|---|---|---|
| 1 | Mở đầu | eyebrow, `h1`, `.sub`, `.small` | Tiêu đề "Bức tranh chuyển đổi số<br>ngành X"; câu dẫn "Vì sao phải làm, công nghệ giúp được gì, và phạm vi đáp ứng của Base"; dòng nhỏ "Base.vn · Tài liệu tham khảo cho doanh nghiệp X · tháng/năm" | Ghi chú mở bằng hình ảnh "Biết container đang ở đâu. Còn hồ sơ đang nằm ở ai?" | Tìm một cặp đối lập tương tự: thứ ngành đã số hoá tốt (máy, đơn, công trình) và thứ vẫn chạy tay (hồ sơ, phê duyệt). Dùng lại ở slide đóng |
| 2 | Tài liệu giúp trả lời 3 câu hỏi | `.cards` 3 thẻ | 01 Vì sao chủ doanh nghiệp X phải quan tâm? · 02 Công nghệ giúp được gì? · 03 Base khác ở đâu? | — | Giữ nguyên, đổi tên ngành |

## Phần 1 · Bối cảnh — "Vì sao chủ doanh nghiệp ngành X phải quan tâm?"

| # | Slide | Thành phần | Nội dung | Ví dụ logistics | Chuyển ngành |
|---|---|---|---|---|---|
| 3 | Chương 1 | `.ghost` 01, `h1` | "Vì sao X không thể đứng ngoài công nghệ" | — | — |
| 4 | Chi phí / áp lực | `.kpis` 3 số + `.lede` | Một chỉ số đau của ngành so với chuẩn và mục tiêu chính sách | 16,8% chi phí logistics/GDP (VLA, 2021) · 10,6% thế giới · mục tiêu 12–15% (QĐ 2229/QĐ-TTg). Câu dẫn: "Phần chênh lệch nằm ở những chỗ quen thuộc: xe chạy rỗng, xe chờ ở cảng, chứng từ làm lại." | Sản xuất: tỷ lệ phế phẩm, năng suất lao động; bán lẻ: chi phí vận hành/doanh thu, hàng tồn; xây dựng: chậm tiến độ, đội chi phí |
| 5 | Mức độ số hoá | `.meter` + `.n3` + `.lede` | Tỷ lệ doanh nghiệp còn ở bước số hoá; số doanh nghiệp, tỷ lệ DNNVV | 90,5% còn ở giai đoạn số hoá; 73,5% cấp 2; 1,9% dự báo được; 0,4% thích ứng. Dòng 2 riêng: "Vạch xuất phát còn đông — ai đi trước một bước là có lợi thế." | Tìm khảo sát của hiệp hội/bộ ngành; không có thì dùng khảo sát chuyển đổi số doanh nghiệp chung và ghi rõ phạm vi |
| 6 | Kết quả của những quyết định dựa trên dữ liệu | `.kpis` 3 số + `.lede` | Lợi ích đo được của nhóm đi đầu (nguồn quốc tế uy tín) | McKinsey 2021: −15% chi phí logistics, −35% tồn kho, +65% mức phục vụ. "Ở Việt Nam… cũng đã có con số tương tự — xem phần 2." | Chọn nghiên cứu đúng ngành (McKinsey, BCG, Deloitte, WEF) |
| 7 | Cơ hội | `.cards` 3 + `.lede` | Tăng trưởng thị trường · xu hướng khách hàng · chuẩn mới; câu chính sách "đẩy cùng chiều" | Tăng trưởng 12–15%/năm · 70–80% chủ hàng thuê ngoài · chứng từ điện tử; "Chính sách cũng đẩy cùng chiều: … từ hạng 43 lên nhóm 40 nước dẫn đầu (LPI)" | Chiến lược/quy hoạch ngành của Chính phủ, cam kết FTA, yêu cầu của khách hàng lớn |
| 8 | Vậy thì… nên ứng dụng công nghệ như thế nào? | eyebrow "Vậy thì", `.versus.dense` | Cột ✕ "Nếu đứng ngoài" (3 hệ quả có số) · cột ! "Nếu làm vội" (mua rời rạc, chi phí đào tạo, an toàn dữ liệu) | 35–70% chuyến xe chạy rỗng; Maersk NotPetya 250–300 triệu USD; lời DPL về chi phí đào tạo | Giữ cấu trúc; tìm 1 số "đứng ngoài" đặc thù ngành và 1 sự cố an toàn dữ liệu trong ngành |
| 9 | Lãnh đạo doanh nghiệp X nói gì | `.quotes.q4` 4 câu | Trích nguyên văn của chủ/TGĐ doanh nghiệp trong ngành, ghi chức danh, nơi đăng, ngày | Ratraco (tư duy lãnh đạo), Vinafco 2026 (điểm nghẽn, chi phí ẩn), Vinafco 2022 (3 yếu tố), DPL (chi phí đào tạo) | Ưu tiên lãnh đạo doanh nghiệp (không phải quan chức); trộn: động lực, cách làm, cái giá |
| 10 | Chốt phần 1 | `h1` + `h2.grad` | "Câu hỏi không còn là có làm không?" → "Mà là làm phần nào trước, bằng công cụ nào." | — | Giữ nguyên |

## Phần 2 · Bài toán và lời giải — "Công nghệ, và Base, giúp được gì?"

| # | Slide | Thành phần | Nội dung | Ví dụ logistics | Chuyển ngành |
|---|---|---|---|---|---|
| 11 | Chương 2 | `.ghost` 02 | "Công nghệ — và Base — giúp được gì" | — | — |
| 12 | Hai dòng chảy | `.lanes` 2 làn | Dòng đặc thù (5 bước, công cụ chuyên ngành) · dòng việc (5 bước, nền tảng quản trị — phần Base) | Dòng hàng: Nhận hàng → Kho → Vận tải → Cảng · hải quan → Giao hàng. Dòng việc: Báo giá → Booking → Chứng từ → Tạm ứng · chi phí → Công nợ | Sản xuất: Kế hoạch → Mua NVL → Sản xuất → QC → Xuất kho / dòng việc: Đơn hàng → Phê duyệt mua → Chi phí → Báo cáo → Công nợ |
| 13 | 2A · Năm bài toán đặc thù | `.mx` 5 dòng (slide top) | Bài toán ✕ · công nghệ thường dùng · doanh nghiệp Việt Nam đã làm + số. **Không nhắc Base** | Xe chạy rỗng (Logistics Đông Á) · cổng cảng (Tân Cảng 13 phút → dưới 2 phút; Gemadept −30% xe chờ) · kho (Vinafco SWM) · chia chọn (Viettel Post 91% nhân lực) · chuỗi lạnh (ABA Cooltrans) | Sản xuất: MES, IoT máy, QC thị giác máy, bảo trì dự đoán, truy xuất nguồn gốc |
| 14 | Base chạy song song, không thay phần mềm chuyên ngành | `.stk` 4–5 dòng | Từ case khách Base: phần mềm chuyên ngành họ đang dùng + phần Base đảm nhận (ghi rõ việc gì) | ICD Sóng Thần, TCL, VOSCO, ADDED-VALUE, DPL | Lấy từ bài Base Customers và báo cáo thường niên của khách trong ngành |
| 15 | Việc chạy trên Zalo, Excel và giấy | `.mess.apps` (Zalo, Excel, email, phiếu giấy, giấy nhớ + 4 cờ) | Tình huống dòng việc điển hình của ngành, chữ ngắn đọc được, dòng "Hình minh hoạ…" | Chứng từ lô HPH-2410 ai cầm; booking cut-off 16h; rate card bản sửa 3; phiếu tạm ứng phí nâng hạ chưa ký | Đổi nội dung từng mảnh theo dòng việc của ngành; giữ 4 cờ: chưa ai trả lời · ai đang giữ · bản nào là bản cuối · chưa có chữ ký |
| 16 | Sáu vấn đề vận hành lặp lại khắp ngành | `.ops` 6 thẻ | Tiêu đề ngắn + 1–2 câu + "Gặp ở: <doanh nghiệp>" — mỗi vấn đề phải có doanh nghiệp đã nêu | Trình ký chờ người · đơn không rõ bước · mạng lưới phân tán · dữ liệu rải rác · tạm ứng bằng giấy · lớn lên khó giữ chất lượng | Rút từ chính các case Base trong ngành |
| 17 | Mỗi bước có người giữ, có hạn, có đầu ra | `.chain` 6 bước + `.chsum` + `.rules` 3 | Quy trình mẫu của ngành (bước, bộ phận, SLA, đầu ra) + 3 nguyên tắc | Báo giá → booking: 6 bước, 3 bộ phận, 32 giờ | Lấy quy trình mẫu trong bộ giải pháp Base cho ngành (Drive `[Shared] <Ngành>`) |
| 18–20 | Case 1–3 | `.story` | Chỉ case **có số liệu**: nhận diện + số lớn · Bài toán · Cách làm · Kết quả · câu nói | 247Express (3 tháng, 200+ bưu cục) · ICD Sóng Thần (+50%, 80% thời gian, in ấn −30–50%) · CTX (12 → 5 bước) | Chọn 3 case khác dạng bài toán (mạng lưới, phê duyệt, quy trình) |
| 21 | Ghi nhận từ khách hàng | `.duo` + `blockquote` | Trích báo cáo thường niên / tài liệu ĐHĐCĐ có nhắc Base, ghi trang | VOSCO BCTN 2022 tr.27; TCL tài liệu ĐHĐCĐ 2022 | Tìm doanh nghiệp niêm yết trong ngành có tên Base trong BCTN/BCTC |
| 22 | Ngành × Base: ứng dụng Base để làm gì? | `.jr` 4 thẻ + `.also` | Các hành trình định tính (doanh nghiệp, việc dùng Base) + dòng chip "Xây dựng văn phòng làm việc điện tử: …" | ADDED-VALUE, THT Cargo, Ratraco, Nhật Việt; chip: Logistics Đông Á, DPL, PCT, PCL | — |
| 23 | Hai lớp phần mềm nối với nhau | `.scope` 2 cột + `.band` | Phần mềm chuyên ngành lo gì · Base lo gì · nối qua API, webhook, dữ liệu dùng chung | TOS/ePort, WMS, TMS/GPS, IoT, kế toán · quy trình đơn hàng, phê duyệt, CRM, giao việc, con người | Đổi cột trái theo hệ chuyên ngành của ngành |

## Phần 3 · Base — "Tầm nhìn của Base khác gì?"

| # | Slide | Thành phần | Nội dung | Ghi chú |
|---|---|---|---|---|
| 24 | Chương 3 | `.ghost` 03 | "Tầm nhìn của Base khác ở đâu" | — |
| 25 | Base tổng quan | `.kpis` + `.lede` | 2016 thành lập · số khách hàng mới nhất (10/2026: 12.000+) · FPT đầu tư 2021 · ra mắt Base 2.0 17/09/2026 | Hỏi lại số khách hàng |
| 26 | Thêm app, thêm AI chưa làm tổ chức giỏi hơn | `.cards` 3 + `.qline` | Dữ liệu rời · kinh nghiệm không ở lại · AI không phối hợp; câu của ông Phạm Kim Hùng về "ngữ cảnh vận hành" | Ví dụ khoảng trống 2 theo ngành |
| 27 | Kiến trúc bốn lớp | `.arch` 4 lớp + `.loop` | Service → Output → Knowledge → Agent, mỗi lớp một "Ví dụ <ngành>" | Ví dụ là minh hoạ, ghi chú mức xác minh |
| 28 | Khác biệt so với phần mềm theo app trên thị trường | `.versus` | ✕ menu tính năng, AI rời, kinh nghiệm mất, phải dời nhà · ✓ bắt đầu từ việc cần xong, AI là một bước có người duyệt, mỗi lần làm để lại quy tắc, nối hệ đang có | Không nêu tên đối thủ |
| 29 | Base 2.0: một nền tảng cho dòng việc | `.mp` 4 tầng | AI & Agent · Vận hành (công việc, khách hàng, con người, tài chính, truyền thông) · Kết nối · Hệ chuyên ngành của doanh nghiệp (giữ nguyên) | Tên app theo giao diện Base 2.0 mới nhất |

## Đóng

| # | Slide | Thành phần | Nội dung |
|---|---|---|---|
| 30 | Đóng vòng | `.stack` 3 dòng + dòng `final grad` | Ba tiêu chuẩn mới + câu gọi lại hình ảnh mở bài (logistics: "Biết container ở đâu. Biết hồ sơ đang ở ai.") |
| 31 | Nguồn tham khảo | `.refs` | Nhóm theo phần (Bối cảnh · Nghiệp vụ đặc thù · Khách hàng của Base · Base và Base 2.0), mỗi dòng có đường dẫn; tài liệu nội bộ ghi tên, không đường dẫn |

## Ghi chú người nói mẫu

```html
<aside class="notes">Câu mở ngắn. <i>[bấm]</i> Ý tiếp theo gắn với khối vừa hiện.<br>
<i>[dừng 2 giây]</i> Câu chốt.<br>
<i>(Nếu khách hỏi: lưu ý về nguồn, mức xác minh, phạm vi theo thông tin nội bộ.)</i></aside>
```
