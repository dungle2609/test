# Nghiên cứu nguồn cho tài liệu ngành

Mục tiêu: mỗi con số và câu trích trên slide đều có nguồn kiểm được, và phần case Base lấy từ chính các bài công bố về khách hàng Base trong ngành.

## 1. Bảng nguồn — lập trước khi viết

Ghi mỗi dữ kiện thành một dòng; slide và mục "Nguồn tham khảo" lấy từ bảng này.

| Dữ kiện (đúng chữ/số) | Nguồn | Ngày | Đường dẫn | Đã mở toàn văn? | Dùng ở slide |
|---|---|---|---|---|---|

Cột "Đã mở toàn văn?" quan trọng: nếu chỉ đọc được trích đoạn tìm kiếm, nói rõ với người dùng và đề nghị họ mở link kiểm trước khi gửi khách.

## 2. Nguồn theo phần

**Phần 1 · Bối cảnh**
- Báo cáo ngành của bộ chủ quản (Bộ Công Thương, Bộ Xây dựng, Bộ Y tế…), hiệp hội ngành (VLA, VASEP, VITAS…), Tổng cục Thống kê.
- Chiến lược/quy hoạch ngành của Chính phủ (số quyết định, ngày ký) — dùng cho "mục tiêu" và "chính sách đẩy cùng chiều".
- Xếp hạng quốc tế liên quan (LPI, GII…), nghiên cứu McKinsey/BCG/Deloitte/WEF về lợi ích số hoá trong ngành.
- Câu nói của **lãnh đạo doanh nghiệp** trong ngành: báo Đầu tư, VnExpress, VnEconomy, CafeF/CafeBiz, VOV, tạp chí hiệp hội, tin chính thức trên website doanh nghiệp, sự kiện ngành. Trích nguyên văn, giữ dấu "…" khi lược.
- Rủi ro: sự cố an toàn dữ liệu nổi tiếng trong ngành, tỷ lệ dự án chuyển đổi số không tới đích.

**Phần 2A · Nghiệp vụ đặc thù (chưa nói Base)**
- Case công nghệ chuyên ngành có số liệu của doanh nghiệp Việt Nam: báo chí, trang case của nhà cung cấp phần mềm chuyên ngành, nghiên cứu trên tạp chí (Tạp chí Kinh tế Tài chính, Tạp chí Công Thương…).
- Mỗi bài toán cần: tên công nghệ thường dùng + một doanh nghiệp đã làm + một con số nếu có.

**Phần 2B · Khách hàng Base trong ngành**
- `customers.base.vn` — trang danh mục theo ngành (bản logistics: `customers.base.vn/giao-nhan-van-tai-logistics/`), trang chủ có câu nói và số liệu khách.
- `resources.base.vn/category/<ngành>/` — case study theo quy trình (ví dụ CTX: 12 → 5 bước).
- `base.vn/industry/<ngành>` — trang giải pháp ngành, nêu tên khách.
- Bài PR trên VnExpress, Báo Đầu tư, VJST… (thường là bản đầy đủ hơn của bài Base Customers).
- **Báo cáo thường niên, BCTC, tài liệu ĐHĐCĐ** của doanh nghiệp niêm yết có nhắc "Base" — bằng chứng "Ghi nhận từ khách hàng". Ghi số trang.
- Drive của người dùng: tìm `fullText contains '<ngành>' and fullText contains 'Base'` — thường có bộ `[Shared] <Ngành>` (giải pháp, dữ liệu mẫu, success stories) và file `[<Ngành>] - Quy trình.xlsx` với quy trình mẫu (bước, bộ phận, SLA, đầu ra) cho slide nguyên lý.
- Danh sách khách Base trong ngành mà người dùng cung cấp (dùng cho dòng chip; phạm vi theo người dùng).

**Phần 3 · Base**
- Bài viết chính thức của Base về Base 2.0 (28/08/2026: kiến trúc Service → Output → Knowledge → Agent); tin ra mắt Base 2.0 tại Enterprise AI Summit 2026 (17/09/2026) trên Báo Đầu tư, Nhân Dân, CafeBiz.
- Tri thức nền Base 2.0 trong skill `base-2-0-html-deck` (`references/base-2-0-foundation.md`) để kiểm claim và chọn mức xác minh.
- Số khách hàng Base: hỏi người dùng con số mới nhất.

## 3. Mẫu truy vấn tìm kiếm

- `Báo cáo <ngành> Việt Nam <năm> chi phí … so với GDP / tỷ lệ doanh nghiệp chuyển đổi số`
- `khảo sát chuyển đổi số doanh nghiệp <ngành> Việt Nam tỷ lệ phần trăm <hiệp hội>`
- `Chiến lược phát triển <ngành> <giai đoạn> mục tiêu`
- `<tên doanh nghiệp> tổng giám đốc chuyển đổi số phát biểu`
- `customers.base.vn <ngành>` · `<tên doanh nghiệp> Base.vn câu chuyện khách hàng`
- `<tên doanh nghiệp> báo cáo thường niên "Base"`
- `<công nghệ chuyên ngành> <doanh nghiệp> giảm … % thời gian`

## 4. Kiểm và chọn

- Số trùng nhiều nguồn: chọn nguồn gốc (bộ, hiệp hội, báo cáo doanh nghiệp) và ghi năm dữ liệu. Số lệch giữa các nguồn: chọn số có phương pháp rõ, nói rõ "ước tính".
- Không tìm được nguồn gốc cho một số trong bản nháp cũ → bỏ, báo người dùng.
- Kết quả của cả chương trình số hoá (nhiều phần mềm) → ghi nhãn đúng trên slide, không quy riêng cho Base.
- Môi trường cloud có thể chặn mở trang trực tiếp; khi đó dùng tìm kiếm mở rộng để đọc trích đoạn, và ghi vào cột "Đã mở toàn văn?" là "chưa".
