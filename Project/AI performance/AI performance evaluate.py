import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix

# 從CSV文件讀取數據
df = pd.read_csv("./Project/AI performance/psudo_result.csv")  # 將'your_data.csv'替換為你的CSV文件路徑

# 設定閾值
threshold = 0.5
print(f'Threshold: {threshold}')

# 將 "Ground truth" 列轉換為二進制標籤
df['Ground truth'] = df['Ground truth'].apply(lambda x: 1 if x == "Sick" else 0)

# 計算混淆矩陣
conf_matrix = confusion_matrix(df['Ground truth'], df['AI pred'] >= threshold)

# 提取混淆矩陣中的值
TN, FP, FN, TP = conf_matrix.ravel()

# 可視化混淆矩陣
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.show()

# 輸出 TP, TN, FP, FN
print(f'TP: {TP}')
print(f'TN: {TN}')
print(f'FP: {FP}')
print(f'FN: {FN}')

# 計算準確率
accuracy = (TP + TN) / (TP + TN + FP + FN)
print(f'Accuracy: {accuracy:.2%}')

# 計算精確率
precision = TP / (TP + FP)
print(f'Precision: {precision:.2%}')

# 計算召回率
recall = TP / (TP + FN)
print(f'Recall: {recall:.2%}')

# 計算F1分數
f1_score = 2 * precision * recall / (precision + recall)
print(f'F1 Score: {f1_score:.2%}')
