# Ngữ Cảnh Hiện Tại

## Tập Trung Hiện Tại
- Phân tích bộ dữ liệu về giá nhà 
- Xây dựng và đánh giá các mô hình dự đoán giá nhà
- Tối ưu hóa mô hình Neural Network cho dự đoán giá nhà
- Cải thiện giao diện người dùng với giao diện sáng và trực quan

## Thay Đổi Gần Đây
- Đã thu thập bộ dữ liệu mẫu về giá nhà
- Đã huấn luyện mô hình Neural Network
- Đã lưu mô hình huấn luyện vào thư mục models_ml
- Đã tạo notebook phân tích khám phá dữ liệu (EDA) tại house_price_eda.ipynb
- Đã tạo các thành phần tiền xử lý (scaler.joblib, label_encoders.joblib, column_info.joblib)
- Đã hoàn thiện ứng dụng dự đoán giá nhà (app.py) với giao diện người dùng sử dụng Streamlit
- Đã tối ưu hóa giao diện người dùng với chủ đề sáng hơn

## Bước Tiếp Theo
- Demo ứng dụng dự đoán giá nhà với giao diện sáng mới
- Chạy và kiểm tra notebook phân tích khám phá dữ liệu (EDA)
- Phân tích sâu hơn về mối quan hệ giữa các biến và giá nhà
- Tinh chỉnh mô hình Neural Network để cải thiện hiệu suất
- Thêm biểu đồ trực quan trong giao diện người dùng
- Thu thập phản hồi từ người dùng để cải thiện ứng dụng

## Quyết Định Và Cân Nhắc Hiện Tại
- Cần đánh giá xem các đặc điểm nào có tác động mạnh nhất đến giá nhà
- Quyết định tập trung vào mô hình Neural Network vì hiệu suất tốt nhất
- Cân nhắc việc tạo các đặc trưng mới để cải thiện hiệu quả của mô hình
- Sử dụng giao diện sáng để tăng tính chuyên nghiệp và dễ sử dụng
- Xem xét cách cải thiện trải nghiệm người dùng bằng cách thêm biểu đồ và trực quan hóa

## Mẫu Và Sở Thích Quan Trọng
- Sử dụng các biểu đồ trực quan để hiển thị mối quan hệ giữa các đặc điểm
- Đánh giá mô hình dựa trên nhiều chỉ số (MSE, MAE, R²) không chỉ một chỉ số
- Giải thích được các yếu tố ảnh hưởng đến dự đoán (không chỉ đưa ra kết quả)

## Học Hỏi Và Hiểu Biết Về Dự Án
- Diện tích và số tầng là những yếu tố quan trọng ảnh hưởng đến giá nhà
- Các đặc điểm phân loại (categorical) như tình trạng nội thất cần được mã hóa phù hợp
- Vị trí trên đường chính ảnh hưởng đáng kể đến giá nhà
- Cần cân nhắc các tiện ích (phòng khách, tầng hầm, hệ thống nước nóng, điều hòa) khi dự đoán giá
