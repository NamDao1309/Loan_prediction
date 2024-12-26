import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder
from imblearn.over_sampling import SMOTE
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
from sklearn.model_selection import train_test_split
import joblib

# Đọc dữ liệu
loan_data = pd.read_csv('loan_data_cleaned.csv')
label_encoder = LabelEncoder()
loan_data['purpose'] = label_encoder.fit_transform(loan_data['purpose'])

X = loan_data.drop('not_fully_paid', axis=1)
y = loan_data['not_fully_paid']

# Chia dữ liệu và áp dụng SMOTE
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
smote = SMOTE(random_state=42)
X_resampled, y_resampled = smote.fit_resample(X_train, y_train)

# Chuẩn hóa dữ liệu
scaler = StandardScaler()
X_resampled = scaler.fit_transform(X_resampled)
X_test_scaled = scaler.transform(X_test)  

# Huấn luyện mô hình Random Forest
rf_model = RandomForestClassifier(random_state=42)
rf_model.fit(X_resampled, y_resampled)

# Huấn luyện mô hình Logistic Regression
lr_model = LogisticRegression(random_state=42)
lr_model.fit(X_resampled, y_resampled)

# Dự đoán trên tập kiểm tra - Random Forest
y_pred_rf = rf_model.predict(X_test_scaled)
y_prob_rf = rf_model.predict_proba(X_test_scaled)[:, 1]

# Dự đoán trên tập kiểm tra - Logistic Regression
y_pred_lr = lr_model.predict(X_test_scaled)
y_prob_lr = lr_model.predict_proba(X_test_scaled)[:, 1]

# Tính toán các chỉ số - Random Forest
conf_matrix_rf = confusion_matrix(y_test, y_pred_rf)
class_report_rf = classification_report(y_test, y_pred_rf)
accuracy_rf = accuracy_score(y_test, y_pred_rf)

# Tính toán các chỉ số - Logistic Regression
conf_matrix_lr = confusion_matrix(y_test, y_pred_lr)
class_report_lr = classification_report(y_test, y_pred_lr)
accuracy_lr = accuracy_score(y_test, y_pred_lr)

# In kết quả - Random Forest
print("Random Forest Accuracy:", accuracy_rf)
print("\nRandom Forest Confusion Matrix:\n", conf_matrix_rf)
print("\nRandom Forest Classification Report:\n", class_report_rf)

# In kết quả - Logistic Regression
print("Logistic Regression Accuracy:", accuracy_lr)
print("\nLogistic Regression Confusion Matrix:\n", conf_matrix_lr)
print("\nLogistic Regression Classification Report:\n", class_report_lr)

# Lưu mô hình 
joblib.dump(rf_model, 'rf_model.pkl')
joblib.dump(scaler, 'scaler.pkl')
joblib.dump(label_encoder, 'label_encoder.pkl')
print("Mô hình đã được lưu.")

