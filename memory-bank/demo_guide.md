# Hướng Dẫn Demo Ứng Dụng Dự Đoán Giá Nhà

## Giới Thiệu
Tài liệu này cung cấp hướng dẫn chi tiết về cách chạy và demo ứng dụng dự đoán giá nhà. Ứng dụng được xây dựng bằng Streamlit và sử dụng các mô hình học máy đã được huấn luyện để dự đoán giá nhà dựa trên các đặc điểm của căn nhà.

## Yêu Cầu Hệ Thống
- Python 3.7 trở lên
- Các thư viện cần thiết được liệt kê trong file `requirements.txt`

## Chuẩn Bị Môi Trường
1. Đảm bảo bạn đã cài đặt Python và pip
2. Cài đặt các thư viện cần thiết:
   ```
   pip install -r requirements.txt
   ```

## Các Bước Chạy Demo

### Bước 1: Khởi Động Ứng Dụng
Mở terminal hoặc command prompt và chạy lệnh sau:
```
streamlit run app.py
```
Ứng dụng sẽ được khởi chạy và mở trong trình duyệt web mặc định của bạn.

### Bước 2: Nhập Thông Tin Căn Nhà
1. Nhập số phòng ngủ (từ 1-10)
2. Nhập số phòng tắm (từ 1-10)
3. Nhập diện tích căn nhà (m²)
4. Nhập số tầng (từ 1-5)
5. Chọn vị trí (có ở đường chính hay không)
6. Chọn có phòng khách hay không
7. Chọn có tầng hầm hay không
8. Chọn có hệ thống nước nóng hay không
9. Chọn có điều hòa hay không
10. Nhập số chỗ đỗ xe (từ 0-5)
11. Chọn khu vực ưa thích hay không
12. Chọn tình trạng nội thất (đầy đủ, một phần, không có)

### Bước 3: Chọn Mô Hình Dự Đoán
Chọn một hoặc nhiều mô hình mà bạn muốn sử dụng để dự đoán giá nhà:
- Linear Regression (Hồi quy tuyến tính)
- Random Forest (Rừng ngẫu nhiên)
- XGBoost
- Neural Network (Mạng nơ-ron nhân tạo)

### Bước 4: Xem Kết Quả Dự Đoán
Nhấn nút "Dự đoán giá nhà" để xem kết quả:
- Giá trung bình từ tất cả các mô hình được chọn
- Dự đoán giá từ từng mô hình riêng biệt
- Thông tin chi tiết về căn nhà đã nhập

## Các Tính Năng Chính
- Dự đoán giá nhà dựa trên nhiều đặc điểm khác nhau
- So sánh kết quả từ nhiều mô hình học máy
- Giao diện người dùng trực quan và dễ sử dụng
- Hiển thị thông tin chi tiết về căn nhà và kết quả dự đoán

## Lưu Ý Khi Demo
- Kết quả dự đoán được hiển thị theo đơn vị triệu VNĐ
- Ứng dụng hỗ trợ các quận chính tại TP.HCM (Quận 1, Quận 2, Quận 3, Quận 7, Quận 10, Thủ Đức)
- Kết quả dự đoán chỉ mang tính chất tham khảo và có thể khác với giá thực tế

## Tắt Ứng Dụng
Để tắt ứng dụng Streamlit, hãy nhấn `Ctrl+C` trong terminal đang chạy ứng dụng.

## Khắc Phục Sự Cố
Nếu gặp lỗi khi khởi động ứng dụng:
1. Kiểm tra xem bạn đã cài đặt đầy đủ các thư viện trong requirements.txt chưa
2. Đảm bảo các file mô hình (*.joblib, *.pth) đã tồn tại trong thư mục models_ml
3. Kiểm tra các thành phần tiền xử lý (scaler.joblib, label_encoders.joblib) đã được tạo đúng cách
