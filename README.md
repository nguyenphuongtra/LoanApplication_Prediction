# Loan Application Prediction ✅

**Mô tả:**
Ứng dụng Flask đơn giản để dự đoán việc **phê duyệt hồ sơ vay** dựa trên đầu vào của người dùng (thu nhập, số người phụ thuộc, lịch sử tín dụng, v.v.). Dự án sử dụng mô hình được huấn luyện sẵn (pickle) để trả về kết quả ngay trên giao diện web.

---

## 🔍 Tính năng chính

- Giao diện web với form nhập liệu (templates/Loan_Application.html)
- Dự đoán kết quả vay (Approved / Denied) bằng mô hình học máy (pickle files trong `models/`)
- Có notebook Jupyter cho phần khám phá dữ liệu và huấn luyện mô hình: `Jupyter_Notebooks/ML_AdvancedBootCamp_Assignment_3_Advanced_Loan_or_No_Loan_.ipynb`

---

## 📦 Yêu cầu

- Python 3.7+ (khuyến nghị)
- Các thư viện (xem `requirements.txt`):

```bash
pip install -r requirements.txt
```

(thông thường bao gồm: numpy, pandas, Flask, scikit-learn, xgboost, imblearn, ...)

---

## 🚀 Cách chạy

1. Clone repository:

```bash
git clone <repo-url>
cd LoanApplication_Prediction
```

2. Tạo virtual environment (tùy chọn) và cài đặt dependencies:

```bash
python -m venv venv
# Windows
venv\Scripts\activate
pip install -r requirements.txt
```

3. Chạy ứng dụng:

```bash
python app.py
```

Mở trình duyệt vào `http://127.0.0.1:5000/` để truy cập form đăng ký vay.

*Ghi chú:* Trong môi trường production bạn có thể dùng Gunicorn hoặc một WSGI server khác: `gunicorn app:app`.

---

## 🗂 Cấu trúc thư mục chính

- `app.py` – Flask app và logic dự đoán
- `templates/Loan_Application.html` – giao diện HTML
- `models/` – chứa các file mô hình (.pickle)
- `Jupyter_Notebooks/` – notebook cho EDA & training
- `static/` – CSS/JS/tài nguyên frontend

---

## ℹ️ Thông tin mô hình

Các mô hình đã được huấn luyện và lưu trong thư mục `models/` (ví dụ: `loan_application_model_lr.pickle`). `app.py` hiện đang load `loan_application_model_lr.pickle` để phục vụ dự đoán.

Nếu bạn muốn huấn luyện lại mô hình, mở notebook trong `Jupyter_Notebooks/` để theo dõi pipeline xử lý dữ liệu và huấn luyện mô hình.

---

## Contributing 🤝

- Fork repo, tạo branch feature hoặc fix
- Tạo PR mô tả rõ thay đổi
- Kiểm tra hoạt động của app trước khi gửi PR

---




