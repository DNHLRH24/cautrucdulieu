import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_excel("C:\\Users\\ADMIN\\quocdan\\ds_salaries.xlsx")

# Chọn các cột chứa dữ liệu chữ
categorical_columns = ["experience_level"]

# Mã hóa một-hot cho các cột chữ
encoded_data = pd.get_dummies(data[categorical_columns], prefix="experience_level")

# Tạo dataframe chỉ chứa các cột số
numeric_column = data['salary_in_usd']

# Kết hợp các cột số và các cột đã được mã hóa
processed_data = pd.concat([numeric_column, encoded_data], axis=1)
print(processed_data.head())

# Tính ma trận tương quan
correlation_matrix = processed_data.corr(numeric_only=True)

# Mức tương tương quan giữa 'experience_level_SE' với 'salary_in_usd"
correlation_experienceSE_salary= correlation_matrix["salary_in_usd"]["experience_level_SE"]
print('Gía trị tương quan giữa mức độ kinh nghiệm SE và lương (usd)=',correlation_experienceSE_salary)

# Vẽ biểu đồ heatmap của ma trận tương quan
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5, fmt='.2f')
plt.title("Ma trận tương quan giữa các cấp độ kinh nghiệm với lương (usd)")
plt.show()

# Tạo biểu đồ nhiệt về các mối tương quan với cột mục tiêu
target_corr = correlation_matrix['salary_in_usd'].drop('salary_in_usd')

# Sắp xếp các giá trị tương quan theo thứ tự giảm dần
target_corr_sorted = target_corr.sort_values(ascending=False)

# Tạo bản đồ nhiệt về các mối tương quan với cột mục tiêu
sns.set(font_scale=0.8)
sns.set_style("white")
sns.set_palette("PuBuGn_d")
sns.heatmap(target_corr_sorted.to_frame(), cmap="coolwarm", annot=True, fmt='.2f')
plt.title('Tương quan với tiền lương usd')
plt.show()
