import pandas as pd
import numpy as np

# Tải dữ liệu
file_path = 'loan_data_payment.csv'
loan_data = pd.read_csv(file_path)
loan_data.head()
loan_data['credit_policy'].value_counts()
# Xóa các cột đã chỉ định
loan_data_cleaned = loan_data.drop([ 'credit_policy','days_with_cr_line','revol_util','inq_last_6mths'], axis=1)

# Xóa các hàng có giá trị bị thiếu
loan_data_cleaned = loan_data_cleaned.dropna()

# Xử lý giá trị 0 trong cột annual_inc trước khi tính logarit
loan_data_cleaned = loan_data_cleaned[loan_data_cleaned['log_annual_inc'] > 0]

# Tính logarit của thu nhập hàng năm và tạo cột mới sử dụng
loan_data_cleaned.loc[:, 'log_annual_inc'] = np.log10(loan_data_cleaned['log_annual_inc'])

# Kiểm tra thông tin, hiển thị dữ liệu sau khi làm sạch, và đếm số giá trị bị thiếu
loan_data_cleaned.info(), loan_data_cleaned.head(), loan_data_cleaned.isnull().sum()

# Lưu dữ liệu đã làm sạch vào tệp CSV mới
loan_data_cleaned.to_csv('loan_data_cleaned.csv', index=False)