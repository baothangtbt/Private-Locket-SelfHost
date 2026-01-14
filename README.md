# 💛 Private Locket - Self-hosted Social Widget

> **Mạng xã hội thu nhỏ dành cho nhóm bạn thân, chạy trên hạ tầng cá nhân (Self-hosted).**

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python)
![Flask](https://img.shields.io/badge/Backend-Flask-green?style=flat&logo=flask)
![SQLite](https://img.shields.io/badge/Database-SQLite-blue?style=flat&logo=sqlite)
![Status](https://img.shields.io/badge/Status-MVP-orange)

---

## 📖 Giới thiệu (Overview)

**Private Locket** là giải pháp thay thế cho các mạng xã hội công cộng, tập trung vào **quyền riêng tư** và chia sẻ khoảnh khắc **thời gian thực (Real-time)**.

Dự án cho phép người dùng **tự làm chủ dữ liệu (Self-host)** thay vì gửi dữ liệu lên các máy chủ bên thứ ba.

Dự án mô phỏng trải nghiệm của **Locket Widget**, nhưng chạy trên nền tảng **Web**, có thể truy cập từ mọi thiết bị (**Cross-platform**).

---

## 🚀 Tính năng chính (Key Features)

- **📸 Đăng ảnh Real-time:** Chụp và upload ảnh ngay lập tức kèm Caption (Trạng thái).
- **💬 Trò chuyện & tương tác:** Bình luận, thả tim trực tiếp trên ảnh.
- **🕰 Dòng thời gian:** Hiển thị ảnh theo thứ tự thời gian thực.
- **🔒 Quyền riêng tư:** Dữ liệu nằm hoàn toàn trên máy chủ cá nhân.
- **📱 Mobile-first UI:** Tối ưu cho điện thoại, hỗ trợ Dark Mode.

---

## 🛠 Công nghệ sử dụng (Tech Stack)

- **Backend:** Python (Flask Framework)
- **Database:** SQLite, SQLAlchemy ORM
- **Frontend:** HTML5, Jinja2, TailwindCSS
- **Infrastructure:** NPort / Cloudflare Tunnel (Tunneling Solution)

---

## ⚙️ Cài đặt & Chạy thử (Installation)

### Yêu cầu hệ thống

- Python 3.x  
- Git  
- NodeJS (nếu dùng NPort)

---

### 🔹 Bước 1: Clone Repository

```bash
git clone https://github.com/baothangtbt/Private-Locket-SelfHost.git
cd Private-Locket-SelfHost
```

---

### 🔹 Bước 2: Cài đặt thư viện (Dependencies)

```bash
pip install -r requirements.txt
```

---

### 🔹 Bước 3: Khởi động Server (Backend)

```bash
python app.py
```

Truy cập:

```text
http://localhost:5000
```

---

### 🔹 Bước 4: Public ra Internet (Truy cập từ điện thoại)

Cài đặt NPort:

```bash
npm install -g nport
```

Mở tunnel (giữ server Flask đang chạy):

```bash
nport 5000 -s ten-du-an-tuy-chon
```

📌 Copy link dạng `https://xxxx.nport.link` để chia sẻ cho bạn bè.

---

## 📂 Cấu trúc dự án (Project Structure)

```plaintext
Private-Locket-SelfHost/
│
├── app.py              # Backend Flask
├── locket.db           # Database (tự tạo khi chạy)
├── requirements.txt    # Danh sách thư viện
├── uploads/            # Ảnh người dùng upload
└── templates/          # Giao diện người dùng
    ├── base.html       # Layout chung
    ├── index.html      # Trang Feed
    └── login.html      # Trang đăng nhập
```

---

## 🤝 Đóng góp (Contributing)

Mọi đóng góp đều được hoan nghênh.

- Fork repository  
- Tạo branch mới  
- Commit thay đổi  
- Tạo Pull Request  

---

## ❤️ Tác giả

Developed with ❤️ by **[tbt超级懒]**
