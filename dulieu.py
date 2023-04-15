import pandas as pd
# dọc file dữ liệu
df = pd.read_excel('C:\\Users\\ADMIN\\quocdan\\dulieu.xlsx', sheet_name="Sheet1")
print(df.head(20))
#đọc hàng stt 0
stt1= df.iloc[0]
for stt in stt1:
    print(stt)
# đọc cột stt 0 
stt2 = df.iloc[:,0]
for value in stt2:
    print(value)
# đọc theo vùng
stt3 = df.iloc[1:7, 2]
print(stt3)
# đọc theo giá trị 1 ô cụ thể 
stt4= df.iloc[2,4]
print(stt4)
#kiểm tra kích thước của dataframe
print(df.shape)
# tổng số lượng đầu kì
total = df.iloc[1:7,2].sum()
print(total)


