import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os
import torch
from pathlib import Path

# Thiết lập tiêu đề và mô tả
st.set_page_config(page_title="Dự đoán giá nhà", layout="wide")

# Đường dẫn tới thư mục chứa các mô hình
MODELS_DIR = Path("models_ml")

# Định nghĩa mô hình Neural Network
class NeuralNetwork(torch.nn.Module):
    def __init__(self, input_size):
        super(NeuralNetwork, self).__init__()
        self.hidden_layer_1 = torch.nn.Linear(input_size, 64)
        self.hidden_layer_2 = torch.nn.Linear(64, 32)
        self.hidden_layer_3 = torch.nn.Linear(32, 16)
        self.output_layer = torch.nn.Linear(16, 1)
        self.relu = torch.nn.ReLU()
        
    def forward(self, x):
        x = self.relu(self.hidden_layer_1(x))
        x = self.relu(self.hidden_layer_2(x))
        x = self.relu(self.hidden_layer_3(x))
        x = self.output_layer(x)
        return x

# Hàm để tải các mô hình và các thành phần tiền xử lý
@st.cache_resource
def load_models():
    try:
        models = {}
        
        # Tải các thành phần tiền xử lý
        scaler = joblib.load(MODELS_DIR / "scaler.joblib")
        label_encoders = joblib.load(MODELS_DIR / "label_encoders.joblib")
        
        # Xác định số lượng các đặc trưng đầu vào cho mô hình ANN
        sample_data = pd.read_csv(MODELS_DIR / "sample_data.csv")
        input_features = len(sample_data.columns) - 1  # Trừ đi cột giá
        
        # Tải mô hình ANN
        ann_model = NeuralNetwork(input_features)
        device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        ann_model.load_state_dict(torch.load(MODELS_DIR / "ann_model.pth", map_location=device))
        ann_model.eval()
        models["Neural Network"] = ann_model
        
        # st.success("Mô hình Neural Network đã được tải thành công!")
        
        return models, scaler, label_encoders
    except FileNotFoundError as e:
        st.error(f"Không tìm thấy file: {str(e)}")
        raise e 
    except Exception as e:
        st.error(f"Lỗi khi tải mô hình: {str(e)}")
        raise e

# Hàm tiền xử lý dữ liệu
def preprocess_input(input_data, scaler, label_encoders):
    try:
        # Chuyển đổi dữ liệu đầu vào thành DataFrame
        input_df = pd.DataFrame([input_data])
        
        # Áp dụng Label Encoder cho các biến phân loại
        categorical_columns = ["mainroad", "guestroom", "basement", "hotwaterheating", "airconditioning", "prefarea", "furnishingstatus"]
        for col in categorical_columns:
            if col in input_df.columns and col in label_encoders:
                input_df[col] = label_encoders[col].transform([input_df[col].iloc[0]])[0]
        
        # Đảm bảo thứ tự cột giống với dữ liệu huấn luyện
        # Lấy danh sách cột từ sample_data, loại bỏ cột 'price'
        sample_data = pd.read_csv(MODELS_DIR / "sample_data.csv")
        feature_columns = [col for col in sample_data.columns if col != 'price']
        
        # Sắp xếp lại các cột trong input_df
        input_df = input_df[feature_columns]
        
        # Chuẩn hóa dữ liệu
        scaled_data = scaler.transform(input_df)
        
        return scaled_data
    except Exception as e:
        st.error(f"Error in preprocessing: {str(e)}")
        raise e

# Hàm dự đoán giá nhà
def predict_price(input_data, model, model_name):
    if model_name == "Neural Network":
        # Chuyển đổi dữ liệu thành tensor PyTorch
        input_tensor = torch.FloatTensor(input_data)
        with torch.no_grad():
            prediction = model(input_tensor).item()
    else:
        prediction = model.predict(input_data)[0]
    
    # Làm tròn và định dạng giá
    price_millions = round(prediction / 1000000, 2)
    
    return price_millions

# Tải các mô hình và thành phần tiền xử lý
try:
    models, scaler, label_encoders = load_models()
    models_loaded = True
except Exception as e:
    st.error(f"Error loading models: {e}")
    models_loaded = False

# Tiêu đề ứng dụng
st.title("🏠 Ứng dụng dự đoán giá nhà")
st.markdown("""
Ứng dụng này sử dụng các mô hình học máy để dự đoán giá nhà dựa trên các đặc điểm của căn nhà.
Hãy nhập thông tin về căn nhà bạn quan tâm và xem ước tính giá từ các mô hình khác nhau.
""")

# Tạo giao diện nhập thông tin căn nhà
st.header("📝 Thông tin căn nhà")

col1, col2 = st.columns(2)

with col1:
    area = st.number_input("Diện tích (m²)", min_value=2000, max_value=20000, value=6000)
    bedrooms = st.number_input("Số phòng ngủ", min_value=1, max_value=10, value=3)
    bathrooms = st.number_input("Số phòng tắm", min_value=1, max_value=10, value=2)
    stories = st.number_input("Số tầng", min_value=1, max_value=5, value=2)
    mainroad = st.selectbox("Ở đường chính", ["yes", "no"], index=0)
    guestroom = st.selectbox("Có phòng khách", ["yes", "no"], index=1)

with col2:
    basement = st.selectbox("Có tầng hầm", ["yes", "no"], index=1)
    hotwaterheating = st.selectbox("Có hệ thống nước nóng", ["yes", "no"], index=1)
    airconditioning = st.selectbox("Có điều hòa", ["yes", "no"], index=0)
    parking = st.number_input("Số chỗ đỗ xe", min_value=0, max_value=5, value=1)
    prefarea = st.selectbox("Sân trước", ["yes", "no"], index=0)
    furnishingstatus = st.selectbox("Tình trạng nội thất", ["furnished", "semi-furnished", "unfurnished"], index=0)

# Chọn mô hình để dự đoán
st.header("🤖 Mô hình dự đoán")
selected_models = ["Neural Network"]
# st.info("Đang sử dụng mô hình ANN để dự đoán giá nhà.")   

# Button dự đoán
predict_button = st.button("🔍 Dự đoán giá nhà")

if predict_button and models_loaded:
    # Thu thập dữ liệu đầu vào
    input_data = {
        "area": area,
        "bedrooms": bedrooms,
        "bathrooms": bathrooms,
        "stories": stories,
        "mainroad": mainroad,
        "guestroom": guestroom,
        "basement": basement,
        "hotwaterheating": hotwaterheating,
        "airconditioning": airconditioning,
        "parking": parking,
        "prefarea": prefarea,
        "furnishingstatus": furnishingstatus
    }
    
    # Tiền xử lý dữ liệu
    processed_input = preprocess_input(input_data, scaler, label_encoders)
    
    # Hiển thị kết quả dự đoán
    st.header("💰 Kết quả dự đoán giá nhà")
    
    results = {}
    for model_name in selected_models:
        price_millions = predict_price(processed_input, models[model_name], model_name)
        results[model_name] = price_millions
    
    # Tính giá trung bình từ tất cả các mô hình
    avg_price = sum(results.values()) / len(results)
    
    # Hiển thị kết quả
    st.markdown(f"### Giá trung bình dự đoán: **{avg_price:.2f} triệu USD**")
    
    # Hiển thị kết quả từ từng mô hình
    # st.markdown("#### Dự đoán từ các mô hình:")
    
    col1, col2 = st.columns(2)
    
    # for i, (model_name, price) in enumerate(results.items()):
    #     if i % 2 == 0:
    #         with col1:
    #             st.info(f"**{model_name}**: {price:.2f} triệu USD")
    #     else:
    #         with col2:
    #             st.info(f"**{model_name}**: {price:.2f} triệu USD")
      # Hiển thị thông tin chi tiết về căn nhà
    st.markdown("#### Chi tiết căn nhà:")
    
    details = f"""
    - **Diện tích**: {area} m²
    - **Số phòng ngủ**: {bedrooms}
    - **Số phòng tắm**: {bathrooms}
    - **Số tầng**: {stories}
    - **Ở đường chính**: {mainroad}
    - **Có phòng khách**: {guestroom}
    - **Có tầng hầm**: {basement}
    - **Có hệ thống nước nóng**: {hotwaterheating}
    - **Có điều hòa**: {airconditioning}
    - **Số chỗ đỗ xe**: {parking}
    - **Sân trước**: {prefarea}
    - **Tình trạng nội thất**: {furnishingstatus}
    """
    
    st.markdown(details)
    
    # Hiển thị lưu ý
    st.warning("""
    **Lưu ý**: Kết quả dự đoán này chỉ mang tính chất tham khảo và có thể khác với giá thực tế.
    Nhiều yếu tố khác như tình trạng kinh tế, xu hướng thị trường, và các đặc điểm cụ thể của khu vực 
    cũng có thể ảnh hưởng đến giá nhà.
    """)
 
# Thông tin thêm về dự án
with st.expander("ℹ️ Thông tin về dự án"):
    st.markdown("""
    ## Về dự án dự đoán giá nhà
    
    Dự án này sử dụng mô hình học máy để dự đoán giá nhà dựa trên các đặc điểm của căn nhà.
      ### Các đặc điểm được sử dụng:
    - Số lượng phòng ngủ và phòng tắm
    - Diện tích căn nhà
    - Số tầng
    - Vị trí (nằm trên đường chính hoặc không)
    - Tiện nghi (phòng khách, tầng hầm, hệ thống nước nóng, điều hòa)
    - Số chỗ đỗ xe
    - Sân trước
    - Tình trạng nội thất (đầy đủ, một phần, không có)
    
    ### Nguồn dữ liệu:
    Mô hình được huấn luyện trên dữ liệu về giá nhà tại các bang của Mỹ.
    """)

# Footer
st.markdown("---")
st.markdown("Developed for Data Mining Course Project | 2025")
