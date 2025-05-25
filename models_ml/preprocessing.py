import pandas as pd
import numpy as np
import joblib
from sklearn.preprocessing import StandardScaler, LabelEncoder
from pathlib import Path

# Đọc dữ liệu mẫu
data_path = Path("sample_data.csv")
data = pd.read_csv(data_path)

# Xác định các cột phân loại
categorical_columns = ["mainroad", "guestroom", "basement", "hotwaterheating", "airconditioning", "prefarea", "furnishingstatus"]

# Tạo và áp dụng Label Encoders cho các cột phân loại
label_encoders = {}
for col in categorical_columns:
    le = LabelEncoder()
    le.fit(data[col])
    label_encoders[col] = le
    data[col] = le.transform(data[col])

# Tạo Standard Scaler cho tất cả các đặc trưng
X = data.drop('price', axis=1)
scaler = StandardScaler()
scaler.fit(X)

# Lưu các thành phần tiền xử lý
joblib.dump(label_encoders, "label_encoders.joblib") 
joblib.dump(scaler, "scaler.joblib")

print("Đã tạo và lưu các thành phần tiền xử lý.")
print(f"- Label encoders (cho {len(categorical_columns)} cột phân loại): {', '.join(categorical_columns)}")
print(f"- Scaler: StandardScaler cho {X.shape[1]} đặc trưng")

# Tạo thông tin cột
column_info = {
    "features": list(X.columns),
    "categorical": categorical_columns,
    "numeric": [col for col in X.columns if col not in categorical_columns]
}
joblib.dump(column_info, "column_info.joblib")
print(f"- Thông tin cột: {column_info}")
