Chi ơi, tui viết lại phần hướng dẫn chạy **6 test case Selenium** của bà theo đúng kiểu trình bày trong file `README.md` của dự án `LAB03---TESTING-SOFTWARE-` luôn nè. Bà chỉ cần copy nguyên đoạn này vô là xong, khỏi chỉnh sửa gì thêm:

---

## 🧪 HƯỚNG DẪN CHẠY TEST CASE GIAO DIỆN

### 📁 Cấu trúc thư mục dự án

```
LAB03---TESTING-SOFTWARE-/
├── test_login_edge.py         # File chứa 6 test case Selenium
├── serve_login.py             # File chạy server nội bộ để phục vụ HTML
├── screenshots/               # Thư mục lưu ảnh chụp màn hình kết quả test
├── test/                      # Thư mục chứa giao diện và tài nguyên
│   ├── login.html
│   ├── signup.html
│   ├── dashboard.html
│   ├── forgot.html
│   ├── style.css
│   ├── script.js
│   └── vendor/, fonts/, images/...
├── README.md
```

---

### ✅ Yêu cầu môi trường

- Python 3.8 trở lên  
- Trình duyệt Microsoft Edge đã cài đặt  
- Edge WebDriver tương thích với phiên bản trình duyệt  
- Thư viện Python: `selenium`

---

### 📦 Cài đặt thư viện Selenium

```bash
pip install selenium
```

---

### 🚀 Cách chạy test

1. **Khởi chạy server nội bộ** để phục vụ file HTML:

```bash
python serve_login.py
```

> Server sẽ chạy ở địa chỉ: `http://127.0.0.1:5500/test/login.html`

2. **Mở terminal mới**, chạy file kiểm thử:

```bash
python test_login_edge.py
```

3. **Kết quả test sẽ hiển thị trên terminal**, ảnh chụp màn hình được lưu trong thư mục `screenshots/`.

---

### 🧾 Danh sách 6 test case

- test_login_success: Kiểm tra đăng nhập với tài khoản hợp lệ. Sau khi đăng nhập, kiểm tra URL và lưu ảnh chụp màn hình thành công.
- test_login_wrong_password: Kiểm tra đăng nhập với mật khẩu sai. Sau khi nhập sai mật khẩu, hệ thống hiển thị lỗi và lưu ảnh chụp màn hình.
- test_login_empty_fields: Kiểm tra khi bỏ trống cả username và password. Nhấn nút đăng nhập và chụp ảnh màn hình cảnh báo, hiển thị thông báo yêu cầu nhập
- test_forgot_password_link: Kiểm tra liên kết “Forgot password?”. Click vào liên kết và kiểm tra URL chuyển hướng, đồng thời lưu ảnh chụp màn hình.
- test_sign_up_link: Kiểm tra liên kết “Sign Up”. Cuộn tới phần tử, click và kiểm tra URL sau khi chuyển hướng. Nếu không tìm thấy phần tử, lưu ảnh lỗi.
- test_social_login_buttons: Kiểm tra sự tồn tại của 3 nút đăng nhập mạng xã hội (Facebook, Twitter, Google). Xác nhận số lượng, kiểm tra xem click được không và lưu ảnh chụp màn hình.

---

### 🛠 Lưu ý khi chạy test
- Nếu test không tìm thấy phần tử hoặc xảy ra lỗi, ảnh lỗi sẽ được lưu tại `screenshots/` để phục vụ debug.

---