import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Đọc dữ liệu từ file Excel
file_path = 'C:/Users/MLMachine/Desktop/datasets.xlsx'
df = pd.read_excel(file_path)

# Chuyển đổi cột 'Price' về số (loại bỏ dấu chấm)
df['Price'] = df['Price'].str.replace('.', '').astype(int)

# Tính toán ma trận tương quan cho các cột số
numeric_df = df.select_dtypes(include=[float, int])
correlation_matrix = numeric_df.corr()

# Vẽ heatmap để hiển thị ma trận tương quan
plt.figure(figsize=(12, 8))  # Điều chỉnh kích thước cho phù hợp
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', square=True, cbar_kws={"shrink": .8})
plt.title('Correlation Matrix of Numerical Attributes')
plt.tight_layout()  # Tối ưu hóa layout cho các nhãn không bị chồng chéo
plt.show()
