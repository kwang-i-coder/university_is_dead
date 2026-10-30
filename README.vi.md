# university_is_dead 🎓

[English](README.md) | [한국어](README.ko.md) | [中文](README.zh-CN.md) | [日本語](README.ja.md) | [Español](README.es.md) | **Tiếng Việt** | [Português](README.pt-BR.md)

**Bộ chỉ dẫn và mẫu ghi chú Obsidian để học các môn đại học cùng Claude.**
Thêm file PDF bài giảng của bạn, rồi dùng các lệnh ngắn như `운체 3` (chương 3 môn Hệ điều hành), `다음` (tiếp theo) hay `시험 정리본` (bản tóm tắt ôn thi) để nhận lời giải thích chuyên sâu theo đúng thứ tự slide. Claude còn có thể dựng khung ghi chú, bản tóm tắt ôn thi và sách tranh ELI5.

> **Lưu ý về ngôn ngữ:** Bộ chỉ dẫn, các mẫu, các lệnh và vault ví dụ đều được viết bằng tiếng Hàn, và mặc định Claude trả lời bằng tiếng Hàn. Hiện tại chỉ phần tài liệu và các file dành cho người đóng góp có bản tiếng Anh. README này là bản dịch từ bản tiếng Anh; nếu có điểm khác nhau, README tiếng Anh là bản chuẩn.

---

## Tính năng

| Bạn nói | Kết quả |
|---|---|
| `운체 3` | Hiển thị bản đồ chương 3 được chia thành các nhóm, mỗi nhóm ứng với một câu hỏi cốt lõi, rồi giải thích nhóm 1 |
| `운체 3-2` / `다음` | Giải thích từng nhóm theo thứ tự slide, kèm công thức, ví dụ số có lời giải từng bước và câu hỏi tự kiểm tra |
| `골격 만들어줘` + PDF | Tạo một ghi chú trống theo dạng `## Section / ### Slide Title (Korean) / - ` |
| `정리해줘` | Hoàn thiện ghi chú của bạn dựa trên PDF mà vẫn giữ nguyên những gì bạn đã viết |
| `시험 정리본` | Đánh dấu mức độ quan trọng bằng ★, bảng so sánh, bài tập kèm tiêu chí chấm điểm và phần hỏi đáp trọng tâm ôn thi |
| `/eli5 {ghi chú}` | Sách tranh HTML tách bạch phép ví von với định nghĩa trong bài giảng |
| `저장해줘` / `운체 3 전부` | Lưu phần giải thích từng nhóm thành ghi chú trong `클코 설명/`, nối với nhau bằng liên kết `다음 →` từ nhóm đầu đến nhóm cuối |
| `기출 분석` + đề thi cũ hoặc bài chia sẻ sau kỳ thi | Ghi bảng đề thi theo từng năm, các chủ đề hay gặp và thứ tự ưu tiên vào `클코 정리/기출 분석.md` |
| (`증명 과목` trong phần ngoại lệ của môn học) | Mẫu chứng minh cho từng định lý, bảng mệnh đề đảo và điều kiện, cùng đề thi thử theo định dạng đề cũ |

## Cài đặt trong 5 phút

1. Lấy repo này: nhấn **Use this template** trên GitHub, hoặc chọn Code → Download ZIP.
2. Lấy `example-vault/` làm mẫu tham khảo, tạo một thư mục môn học trong vault Obsidian của bạn. Bạn có thể đặt nó bên trong thư mục học kỳ; khi đó, hãy ghi đầy đủ đường dẫn ấy vào bảng môn học.
   ```
   (thư mục gốc vault)/
   ├── CLAUDE.md          ← khi dùng Claude Code (bước 4)
   ├── templates/         ← bản sao templates/ của repo này
   ├── tools/             ← bản sao tools/ của repo này
   └── {môn học}/
       ├── 강의자료/        ← PDF bài giảng (chỉ đọc)
       ├── {tên bài giảng}.md  ← ghi chú theo tuần
       ├── 개념.md          ← trang tổng hợp khái niệm + bảng ghi chú theo tuần
       ├── 클코 정리/       ← bản tóm tắt ôn thi, phân tích đề thi cũ
       ├── 클코 설명/       ← các phần giải thích nhóm đã lưu
       └── 학습자료/        ← HTML ELI5
   ```
   Đặt tên mỗi file PDF bài giảng trùng với tên ghi chú tương ứng (`1주차 정렬 기초.md` ↔ `강의자료/1주차 정렬 기초.pdf`) để liên kết tới trang PDF hoạt động đúng.
3. Mở `INSTRUCTIONS.md` và điền trường, các môn học và tên viết tắt của bạn vào khối **"📝 여기만 고치세요"** ("chỉ sửa ở đây"). Ghi mỗi thư mục môn học dưới dạng đường dẫn tính từ thư mục gốc vault (ví dụ `딥러닝/`).
4. Đưa bộ chỉ dẫn cho Claude.
   - **Claude Projects**: dán nội dung vào Project instructions, rồi tải thư mục môn học và các file trong `templates/` lên làm tri thức dự án (project knowledge).
   - **Claude Code**: sửa tương tự trong `CLAUDE.md`, sao chép `CLAUDE.md`, `templates/` và `tools/` vào thư mục gốc vault, rồi chạy Claude Code từ đó. Công cụ kiểm tra liên kết cần Python 3.8 trở lên.
5. Thử gõ `{tên viết tắt} 1`.

## Cấu trúc repo

| Đường dẫn | Nội dung |
|---|---|
| [`INSTRUCTIONS.md`](INSTRUCTIONS.md) | Bộ chỉ dẫn (dành cho Claude Projects) |
| [`CLAUDE.md`](CLAUDE.md) | Cùng bộ chỉ dẫn đó (dành cho Claude Code) |
| [`templates/`](templates) | Các mẫu trống: khung ghi chú, 개념.md, bản tóm tắt ôn thi, giải thích nhóm, phân tích đề thi cũ, HTML ELI5 |
| [`tools/check_links.py`](tools/check_links.py) | Công cụ kiểm tra liên kết Obsidian (tìm ghi chú, tiêu đề và tệp đính kèm bị thiếu) |
| [`example-vault/알고리즘/`](example-vault/알고리즘) | Ví dụ đã điền sẵn với một môn Thuật toán hư cấu. Hãy mở nó bằng Obsidian |
| [`docs/usage-examples.md`](docs/usage-examples.md) | Luồng hội thoại cho từng lệnh |
| [`docs/FAQ.md`](docs/FAQ.md) | Câu hỏi thường gặp |

## Nguyên tắc cốt lõi

- **Tài liệu bài giảng là chuẩn.** Nội dung nào không có trên slide đều được đánh dấu "교재 보충" (bổ sung từ giáo trình).
- **Ghi chú của bạn không bao giờ bị ghi đè.** Claude chỉ bổ sung phần còn thiếu, với mức chỉnh sửa tối thiểu.
- **Giữ nguyên thứ tự slide.** Các nhóm không bao giờ bị trộn lẫn, và slide phụ lục được xếp thành nhóm riêng.
- **Giải thích không bao giờ sơ sài.** Mỗi khái niệm đi theo trình tự động lực → trực giác → định nghĩa/công thức → ví dụ số → hạn chế.

## ⚠️ Không tải tài liệu bài giảng lên

Tài liệu bài giảng của giảng viên, cũng như ghi chú chép lại nội dung bài giảng, là tác phẩm có bản quyền. Nếu bạn sao lưu vault lên GitHub, hãy dùng [`.gitignore`](.gitignore) của repo này và đừng push vault lên repo công khai. Mọi ví dụ trong repo này đều là bài giảng hư cấu được viết mới.

## Đóng góp

Lệnh mới, quy tắc cho các loại môn học khác và cải tiến mẫu đều được hoan nghênh. Hãy đọc [`CONTRIBUTING.md`](CONTRIBUTING.md), mở issue bằng một trong các mẫu issue (Bug Report / Enhancement Request / Common Issue), rồi gửi PR. Mỗi PR đều được tự động kiểm tra việc đồng bộ các file chỉ dẫn, liên kết trong vault ví dụ và tài liệu bài giảng bị tải lên.

## Giấy phép

[MIT](LICENSE)
