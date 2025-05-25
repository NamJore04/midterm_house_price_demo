# Mô Tả Các Mô Hình Học Máy

Dự án sử dụng bốn mô hình học máy để dự đoán giá nhà. Các mô hình này đã được huấn luyện và lưu trong thư mục `models_ml`. Dưới đây là mô tả chi tiết về mỗi mô hình.

## 1. Linear Regression (Hồi Quy Tuyến Tính)
- **File**: `linear_regression_model.joblib`
- **Thuật toán**: Tìm mối quan hệ tuyến tính giữa các đặc điểm đầu vào và giá trị đầu ra
- **Thông số**: 
  - Learning rate: 1e-3 
  - Số vòng lặp (iterations): 10,000
- **Ưu điểm**: Đơn giản, dễ hiểu, tốc độ nhanh
- **Nhược điểm**: Chỉ mô hình hóa mối quan hệ tuyến tính, không thể nắm bắt các mối quan hệ phức tạp

## 2. Random Forest (Rừng Ngẫu Nhiên)
- **File**: `random_forest_model.joblib`
- **Thuật toán**: Kết hợp nhiều cây quyết định để đưa ra dự đoán
- **Thông số**:
  - Số cây (n_estimators): 100
  - Độ sâu tối đa (max_depth): 10
- **Ưu điểm**: Xử lý tốt dữ liệu phi tuyến, ít bị overfitting
- **Nhược điểm**: Tốn tài nguyên tính toán, khó giải thích kết quả

## 3. XGBoost
- **File**: `xgboost_model.joblib`
- **Thuật toán**: Gradient boosting với tối ưu hóa và hiệu suất cao
- **Thông số**:
  - Số cây (n_estimators): 100
  - Learning rate: 0.1
  - Độ sâu tối đa (max_depth): 6
- **Ưu điểm**: Hiệu suất cao, xử lý tốt nhiều loại dữ liệu
- **Nhược điểm**: Có thể bị overfitting nếu không điều chỉnh tham số phù hợp

## 4. Artificial Neural Network (Mạng Nơ-ron Nhân Tạo)
- **File**: `ann_model.pth`
- **Thuật toán**: Deep learning với nhiều lớp ẩn
- **Kiến trúc**:
  - Lớp đầu vào: Phụ thuộc số đặc trưng
  - Lớp ẩn 1: 64 đơn vị với hàm kích hoạt ReLU
  - Lớp ẩn 2: 32 đơn vị với hàm kích hoạt ReLU
  - Lớp ẩn 3: 16 đơn vị với hàm kích hoạt ReLU
  - Lớp đầu ra: 1 đơn vị (dự đoán giá)
- **Thông số**:
  - Optimizer: Adam
  - Learning rate: 1e-3
  - Số epoch: 10,000
  - Loss function: MSE (Mean Squared Error)
- **Ưu điểm**: Có thể mô hình hóa mối quan hệ phức tạp và phi tuyến
- **Nhược điểm**: Yêu cầu nhiều dữ liệu, tốn thời gian huấn luyện, khó hiểu về mặt giải thích

## Các Thành Phần Tiền Xử Lý
Các thành phần tiền xử lý dữ liệu cũng đã được lưu lại để đảm bảo nhất quán khi sử dụng mô hình:

- **column_info.joblib**: Thông tin về các cột dữ liệu và phân loại
- **scaler.joblib**: Bộ chuẩn hóa dữ liệu (StandardScaler)
- **label_encoders.joblib**: Các bộ mã hóa cho dữ liệu phân loại (mainroad, guestroom, basement, hotwaterheating, airconditioning, prefarea, furnishingstatus)
