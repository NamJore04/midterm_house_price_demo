# Kiến Trúc Hệ Thống

## Kiến Trúc Tổng Thể
Dự án dự đoán giá nhà được xây dựng theo kiến trúc modular với các thành phần sau:

```
[Dữ liệu Đầu vào] → [Tiền Xử lý] → [Mô hình Học máy] → [Dự đoán] → [Kết quả & Trực quan hóa]
```

## Mẫu Thiết Kế Chính
1. **Pipelines Xử lý Dữ liệu**: Luồng xử lý dữ liệu từ thô đến đã được làm sạch và chuyển đổi
2. **Đánh giá Đa Mô hình**: Xây dựng và so sánh nhiều mô hình để chọn giải pháp tốt nhất
3. **Trực quan hóa Dữ liệu**: Hiển thị các phân tích và kết quả dưới dạng trực quan

## Quyết Định Kiến Trúc
- **Jupyter Notebook**: Được lựa chọn cho việc phát triển và thử nghiệm các mô hình, cho phép phân tích trực quan và ghi chú có cấu trúc
- **Scikit-learn & Thuật toán AI**: Đa dạng mô hình từ Linear Regression đến Neural Networks
- **Lưu trữ Mô hình**: Các mô hình đã huấn luyện được lưu dưới dạng file (.joblib, .pth) để có thể tái sử dụng

## Các Thành Phần Chính
1. **Thành phần Tiền xử lý Dữ liệu**
   - Làm sạch dữ liệu
   - Mã hóa đặc điểm phân loại (categorical features)
   - Chuẩn hóa dữ liệu
   - Xử lý giá trị thiếu và ngoại lai

2. **Thành phần Mô hình**
   - Linear Regression (hồi quy tuyến tính)
   - Random Forest (rừng ngẫu nhiên) 
   - XGBoost
   - Neural Networks (mạng nơ-ron)

3. **Thành phần Đánh giá**
   - Tính toán các chỉ số hiệu suất (MSE, MAE, R²)
   - So sánh giữa các mô hình
   - Phân tích sai số

4. **Thành phần Trực quan hóa**
   - Biểu đồ tương quan
   - So sánh giá dự đoán và thực tế
   - Phân tích tầm quan trọng của các đặc điểm

## Luồng Dữ liệu Quan Trọng
1. **Thu thập Dữ liệu** → Dữ liệu thô từ nguồn
2. **Tiền xử lý** → Dữ liệu sạch và được chuyển đổi
3. **Huấn luyện Mô hình** → Mô hình đã huấn luyện
4. **Đánh giá** → Chỉ số hiệu suất và thấu hiểu mô hình
5. **Dự đoán** → Giá dự đoán cho dữ liệu mới
