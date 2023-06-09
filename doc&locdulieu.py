import pandas as pd
# đọc toàn bộ dữ liệu  
data = pd.read_excel("C:\\Users\ADMIN\\quocdan\\ds_salaries.xlsx")
print("đọc toàn bộ đữ liệu \n",data) # in ra dữ liệu

print(" đọc ra 100 dòng dữ liệu \n",data.head(100))# đọc ra 100 dòng dữ liệu trong data

# tóm tắc ngắn ngọn các thông tin của dữ liệu
print("tóm tắc ngắn gọn các thông tin của dữ liệu \n\n",data.info())

# đếm xem có bao nhiêu giá trị duy nhất trong mỗi cột (nhằm đánh giá độ đa dạng của dữ liệu)
print("đếm xem có bao nhiêu giá trị duy nhất trong mỗi cột:\n\n", data.nunique())

# đếm số lần xuất hiện các giá trị duy nhất trong cột "work_year" và "salary"
print("in ra số lần xuất hiện các giá trị duy nhất trong các cột \n",data[['work_year', 'salary']].value_counts())

# đếm xem có tổng bao nhiêu giá trị bị thiếu trong mỗi cột dữ liệu
print("in ta tổng số giá trị thiếu trong mỗi cột của dữ liệu \n\n",data.isna().sum())

#lọc dữ liệu
# lọc ra các ngành nghề có mức lương lớn hơn 100000 usd
data_loc1 = data[data['salary_in_usd'] > 100000]
print('lọc ra các các ngành nghề có mức lương lớn hơn 100000usd \n',data_loc1)

# lọc ra các công ty size L và công ty đó đến từ US
data_loc2 =data[(data['company_size'] == 'L') & (data['company_location'] == 'US')]
print("các công ty size L và công ty đó đến từ US \n",data_loc2)