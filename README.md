# Ứng dụng Dự đoán Giá Nhà

Đây là ứng dụng dự đoán giá nhà được phát triển như một phần của dự án Khai phá Dữ liệu (Data Mining). Ứng dụng sử dụng mô hình học máy để dự đoán giá nhà dựa trên các đặc điểm như diện tích, số phòng ngủ và phòng tắm, vị trí, và các tiện ích khác nhau.

## Tính năng

- Dự đoán giá nhà sử dụng mô hình Neural Network (Mạng nơ-ron nhân tạo) được huấn luyện trên dữ liệu giá nhà
- Giao diện người dùng trực quan và thân thiện được xây dựng bằng Streamlit
- Nhập thông tin chi tiết về căn nhà bao gồm:
  - Diện tích (m²)
  - Số phòng ngủ và phòng tắm
  - Số tầng
  - Vị trí đường (đường chính hay không)
  - Các tiện ích (phòng khách, tầng hầm, hệ thống nước nóng, điều hòa)
  - Số chỗ đỗ xe
  - Khu vực ưa thích
  - Tình trạng nội thất (đầy đủ, một phần, không có)

## Cài đặt

1. Clone repository này:
```
git clone https://github.com/NamJore04/midterm_house_price_demo.git
cd house_price_demo
```

2. Tạo môi trường ảo và kích hoạt:
```
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

3. Cài đặt các thư viện cần thiết:
```
pip install -r requirements.txt
```

## Sử dụng

1. Chạy ứng dụng Streamlit:
```
streamlit run app.py
```

2. Trình duyệt web sẽ tự động mở giao diện ứng dụng. Nếu không, truy cập địa chỉ được hiển thị trong terminal (thường là http://localhost:8501).

3. Nhập thông tin về căn nhà bạn muốn dự đoán giá, điều chỉnh các thông số như diện tích, số phòng, và các tiện ích.

4. Nhấn nút "Dự đoán giá nhà" và xem kết quả dự đoán. Kết quả sẽ được hiển thị dưới dạng giá trị tiền theo đơn vị triệu USD.

5. Xem chi tiết về các thông số đã nhập và thông tin thêm về dự án bằng cách mở rộng các phần tương ứng.

## Cấu trúc dự án

- `app.py`: Mã nguồn của ứng dụng Streamlit
- `house_price_eda.ipynb`: Notebook phân tích khám phá dữ liệu (EDA)
- `data-mining.ipynb`: Notebook chính cho phân tích dữ liệu và xây dựng mô hình
- `models_ml/`: Thư mục chứa các mô hình và thành phần tiền xử lý
  - `ann_model.pth`: Mô hình Neural Network đã huấn luyện
  - `linear_regression_model.joblib`: Mô hình hồi quy tuyến tính
  - `random_forest_model.joblib`: Mô hình rừng ngẫu nhiên
  - `xgboost_model.joblib`: Mô hình XGBoost
  - `scaler.joblib`: Bộ chuẩn hóa dữ liệu
  - `label_encoders.joblib`: Bộ mã hóa cho dữ liệu phân loại
  - `column_info.joblib`: Thông tin về cấu trúc cột dữ liệu
  - `sample_data.csv`: Dữ liệu mẫu về giá nhà
  - `preprocessing.py`: Script cho tiền xử lý dữ liệu
- `memory-bank/`: Thư mục chứa tài liệu về dự án
  - `projectbrief.md`: Tổng quan về dự án
  - `activeContext.md`: Ngữ cảnh làm việc hiện tại
  - `progress.md`: Tiến độ dự án
  - `techContext.md`: Thông tin kỹ thuật
  - `models_description.md`: Mô tả chi tiết về các mô hình
  - `demo_guide.md`: Hướng dẫn demo ứng dụng
- `requirements.txt`: Danh sách các thư viện Python cần thiết

## Yêu cầu hệ thống

- Python 3.7 hoặc cao hơn
- Streamlit 1.45.0 hoặc cao hơn
- PyTorch 2.7.0
- scikit-learn 1.6.1
- pandas 2.2.3, numpy 2.1.3
- XGBoost 1.7.3
- Các thư viện khác được liệt kê trong requirements.txt

## Mô hình dữ liệu

Mô hình dự đoán giá nhà dựa trên các đặc điểm sau:
- `area`: Diện tích (m²)
- `bedrooms`: Số phòng ngủ
- `bathrooms`: Số phòng tắm
- `stories`: Số tầng
- `mainroad`: Nhà có nằm trên đường chính không (yes/no)
- `guestroom`: Có phòng khách không (yes/no)
- `basement`: Có tầng hầm không (yes/no)
- `hotwaterheating`: Có hệ thống nước nóng không (yes/no)
- `airconditioning`: Có điều hòa không (yes/no)
- `parking`: Số chỗ đỗ xe
- `prefarea`: Nằm trong khu vực được ưa thích không (yes/no)
- `furnishingstatus`: Tình trạng nội thất (furnished/semi-furnished/unfurnished)

## Tài liệu tham khảo

- Streamlit: https://streamlit.io/
- scikit-learn: https://scikit-learn.org/
- PyTorch: https://pytorch.org/
- XGBoost: https://xgboost.readthedocs.io/

## Tác giả

Dự án được phát triển như một phần của khóa học Khai phá dữ liệu, Năm học 2024-2025.
