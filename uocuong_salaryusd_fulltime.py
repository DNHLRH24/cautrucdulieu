import numpy as np
import pandas as pd
from scipy.stats import norm

# Đọc dữ liệu từ file Excel (thay đổi đường dẫn và tên file Excel của bạn)
data = pd.read_excel("C:\\Users\ADMIN\\quocdan\\ds_salaries.xlsx")

# Lọc dữ liệu chỉ chọn các mẫu có loại hình công việc là FT
ft_sample = data[data['employment_type'] == 'FT']['salary_in_usd']

# Kích thước mẫu
n_ft = 800

# Tính giá trị trung bình mẫu và độ lệch chuẩn mẫu cho FT
mean_ft = ft_sample.mean()
std_ft = ft_sample.std(ddof=1)

# Nhập giá trị tin cậy từ người dùng
confidence_level = float(input("Nhập giá trị tin cậy (từ 0 đến 1): "))

# Giá trị z-score tương ứng với confidence level
z_score_ft = norm.ppf((1 + confidence_level) / 2)

# Tính khoảng tin cậy
margin_of_error_ft = z_score_ft * std_ft / np.sqrt(n_ft)

# ước luoejng khoảng lương trung bình cho loại hình công việc Full time
confidence_interval_ft = (mean_ft - margin_of_error_ft, mean_ft + margin_of_error_ft)

# In kết quả
print("Khoảng tin cậy của giá trị trung bình cho FT:")
print(confidence_interval_ft)