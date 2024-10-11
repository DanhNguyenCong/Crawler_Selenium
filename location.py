import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Đọc dữ liệu từ file Excel
file_path = 'C:/Users/MLMachine/Desktop/datasets.xlsx'
df = pd.read_excel(file_path)
# Tính số lượng xe bán ra theo từng tỉnh
location_counts = df['Location'].value_counts()

# Tạo một DataFrame mới để gán mã định danh
location_mapping = pd.DataFrame(location_counts).reset_index()
location_mapping.columns = ['Location', 'Count']

# Sắp xếp theo số lượng xe bán ra và gán mã định danh
location_mapping = location_mapping.sort_values(by='Count', ascending=False)
location_mapping['ID'] = range(1, len(location_mapping) + 1)

# Thay thế giá trị trong cột 'Location' của DataFrame gốc
df = df.merge(location_mapping[['Location', 'ID']], on='Location', how='left')
df.rename(columns={'ID': 'Location ID'}, inplace=True)

