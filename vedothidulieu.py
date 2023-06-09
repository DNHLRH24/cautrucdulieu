import pandas as pd
import numpy as np
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
import seaborn as sns

# đọc toàn bộ dữ liệu  
data = pd.read_excel("C:\\Users\ADMIN\\quocdan\\ds_salaries.xlsx")

#biểu đồ tròn thể hiện quy mô công ty trong dữ liệu dữ liệu
def bieu_do_tron_company_size(): 
   # kích thước của hình
   plt.figure(figsize = (10, 8))
   # tạo biểu đồ tròn thể hiện sự phân phối cấp độ kinh nghiệm
   data['company_size'].value_counts().plot(kind='pie', autopct='%1.1f%%', cmap='viridis')
   # thêm tiêu đề cho biểu đồ
   plt.title('Biểu đồ tròn thể hiện quy mô công ty')
   plt.show()

# biểu đồ đường thể hiện giá trị trung bình mức lương usd qua các năm  
def bieu_do_duong_mean():
   meanYearlySalary = np.array(data['salary_in_usd'].groupby(data['work_year']).mean())
   plt.xlabel('Year')
   plt.ylabel('Mean Salary')
   plt.title("Giá trị trung bình mức lương USD qua các năm")
   sns.lineplot(x=['2020', '2021', '2022', '2023'], y=meanYearlySalary)
   plt.show()

# biểu đồ cột thể hiện giá trị trung vị mức lương usd qua các năm
def bieu_do_cot_median():
   data.groupby('work_year')['salary_in_usd'].median().plot.bar()
   plt.xlabel('Year')
   plt.ylabel('Median Salary')
   plt.title('Giá trị trung vị mức lương USD qua các năm ')
   plt.show()

# biểu đồ thể hiện top 10 công việc phổ biến nhất
def alltime_top_ten():
   allTimeTopTen = data["job_title"].value_counts().nlargest(10).reset_index()
   sns.barplot(x=allTimeTopTen["job_title"], y=allTimeTopTen["index"])
   plt.title("Top 10 công việc Data Scicence phổ biến nhất")
   plt.xlabel("Count")
   plt.ylabel("Job Title")
   plt.show()

# biểu đồ thể hiện top 10 công việc phổ biến nhất 2023
def alltime_top_ten_2023():
   topTen2023 = data[data["work_year"]==2023]["job_title"].value_counts().nlargest(10).reset_index()
   sns.barplot(x=topTen2023["job_title"], y=topTen2023["index"])
   plt.title("Tóp 10 công việc Data Scicence phổ biến nhất 2023")
   plt.xlabel("Count")
   plt.ylabel("Job Title")
   plt.show()


def experience_level_vs_work_year():
    # Phân tích năm làm việc và mức độ kinh nghiệm bằng hàm pandas cross-tab
    pd.crosstab(data['work_year'],data['experience_level'], normalize = 'index').plot(kind = 'bar')
    plt.xlabel('Year')
    plt.ylabel('Mật độ xác suất')
    plt.title('Cấp độ kinh nghiệm so với năm làm việc')
    plt.xticks(rotation = 0)
    plt.show()

def cap_do_kinh_nghiem():
   fig, ax = plt.subplots()
   sns.countplot(ax = ax, data = data, x = data.experience_level)
   ax.set(xlabel='', ylabel='Counts', title='Cấp độ kinh nghiệm')
   ax.bar_label(ax.containers[0])
   plt.show()

def cot_chong_salary_in_usd_experience_level():
    # Đặt màu nền và kích thước hình
    plt.style.use('dark_background')
    plt.figure(figsize = (10, 6))
    # tạo biểu đồ
    sns.histplot(x = 'salary_in_usd', hue = 'experience_level', multiple = 'stack',
             edgecolor = '#cfd0d4', bins = 50, data = data, palette = 'viridis')
    # Tùy chỉnh tiêu đề và nhãn
    plt.grid(alpha = 0.3)
    plt.title('Phân phối tiền lương (USD) theo kinh nghiệm')
    plt.xlabel('Salary')
    plt.ylabel('Count')
    plt.show()

def tuong_quang_experience_level_company_size():
   # Tạo một bảng chéo của hai cột
    cross_tab = pd.crosstab(data['experience_level'], data['company_size'])
    # Tạo một bản đồ nhiệt bằng cách sử dụng dữ liệu bảng chéo
    plt.figure(figsize=(10, 8))
    sns.heatmap(cross_tab, annot=True, fmt="d", cmap='Blues')
    plt.xlabel('Company Size')
    plt.ylabel('Experience Level')
    plt.title('Mối quan hệ giữa Cấp độ kinh nghiệm và Quy mô công ty')
    plt.show()

def main():
    bieu_do_tron_company_size()
    bieu_do_duong_mean()
    bieu_do_cot_median()
    alltime_top_ten()
    alltime_top_ten_2023()
    experience_level_vs_work_year()
    cap_do_kinh_nghiem()
    cot_chong_salary_in_usd_experience_level()
    tuong_quang_experience_level_company_size()
if __name__=="__main__":
    main()