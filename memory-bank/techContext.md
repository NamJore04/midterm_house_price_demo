# Ngữ Cảnh Kỹ Thuật

## Công Nghệ Sử Dụng
- **Ngôn ngữ lập trình**: Python
- **Môi trường phát triển**: Jupyter Notebook
- **Framework web**: Streamlit cho giao diện người dùng
- **Thư viện phân tích dữ liệu**: 
  - pandas: Xử lý và phân tích dữ liệu
  - numpy: Tính toán số học
  - matplotlib/seaborn: Trực quan hóa dữ liệu
- **Thư viện học máy**:
  - scikit-learn: Mô hình học máy truyền thống (Linear Regression, Random Forest)
  - XGBoost: Mô hình Gradient Boosting nâng cao
  - PyTorch: Xây dựng mạng nơ-ron (ANN)
- **Lưu trữ mô hình**:
  - joblib: Lưu các mô hình scikit-learn và XGBoost
  - PyTorch save: Lưu mô hình mạng nơ-ron
- **Tiền xử lý dữ liệu**:
  - StandardScaler: Chuẩn hóa dữ liệu số
  - LabelEncoder: Mã hóa dữ liệu phân loại

## Môi Trường Phát Triển
- **Jupyter Notebook**: Môi trường tương tác để phát triển và thử nghiệm mô hình
- **Version Control**: Git để quản lý mã nguồn
- **Quản lý gói**: pip và requirements.txt để quản lý phụ thuộc

## Ràng Buộc Kỹ Thuật
- **Hiệu suất**: Cần tối ưu thời gian huấn luyện và dự đoán
- **Tài nguyên hạn chế**: Thiết kế để chạy trên máy tính cá nhân với GPU tùy chọn
- **Khả năng mở rộng**: Có thể xử lý khối lượng dữ liệu lớn khi cần

## Phụ Thuộc
Các thư viện chính (được liệt kê trong requirements.txt):
- pandas
- numpy
- scikit-learn
- xgboost
- pytorch
- matplotlib
- seaborn
- jupyter

## Mẫu Sử Dụng Công Cụ
- **Phân tích khám phá dữ liệu (EDA)**: Sử dụng pandas và seaborn
- **Tiền xử lý dữ liệu**: Sử dụng scikit-learn's Preprocessing
- **Huấn luyện mô hình**: Khớp mô hình với dữ liệu đã chia
- **Đánh giá mô hình**: Sử dụng các chỉ số từ scikit-learn
- **Lưu/Tải mô hình**: Sử dụng joblib và PyTorch save/load

## Quy Trình Phát Triển
1. Phân tích dữ liệu và tìm hiểu đặc điểm
2. Tiền xử lý và tạo đặc trưng
3. Xây dựng các mô hình cơ sở
4. Tinh chỉnh và cải thiện mô hình
5. Đánh giá và lựa chọn mô hình tốt nhất
6. Lưu mô hình để sử dụng
7. Xây dựng giao diện người dùng với Streamlit
8. Tích hợp các mô hình vào ứng dụng
9. Kiểm thử và triển khai ứng dụng
