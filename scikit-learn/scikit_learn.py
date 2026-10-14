import numpy as np
import matplotlib
matplotlib.use('TkAgg')  # 或 'Qt5Agg'
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import seaborn as sns

plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'SimHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

# 1. 加载数据
# sklearn 内置了鸢尾花数据集
iris = datasets.load_iris()
X = iris.data  # 特征数据 (sepal length, sepal width, petal length, petal width)
y = iris.target  # 标签数据 (0: setosa, 1: versicolor, 2: virginica)

print(f"数据集形状: {X.shape}, 标签形状: {y.shape}")
print(f"类别名称: {iris.target_names}")

# 2. 数据划分
# 将数据划分为 80% 训练集和 20% 测试集，random_state 保证每次运行结果一致
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. 数据预处理 (特征标准化)
# 许多机器学习算法在数据缩放后表现更好
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 4. 模型训练
# 使用支持向量机分类器 (SVM)
# kernel='linear' 表示使用线性核，对于简单数据集效果很好
model = SVC(kernel='linear', random_state=42)
model.fit(X_train_scaled, y_train)

# 5. 模型预测
y_pred = model.predict(X_test_scaled)

# 6. 模型评估
print("\n--- 模型评估 ---")
accuracy = accuracy_score(y_test, y_pred)
print(f"准确率: {accuracy:.4f}")

print("\n分类报告:")
# target_names 指定类别名称，使报告更易读
print(classification_report(y_test, y_pred, target_names=iris.target_names))

# 7. 结果可视化 (混淆矩阵)
cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(8, 6))
# 使用 seaborn 绘制热力图
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
            xticklabels=iris.target_names, 
            yticklabels=iris.target_names)
plt.xlabel('预测标签')
plt.ylabel('真实标签')
plt.title('混淆矩阵 - 鸢尾花分类')
plt.show()

# 额外演示：预测单个新样本
print("\n--- 预测新样本 ---")
# 假设我们有一朵花，参数为：[5.1, 3.5, 1.4, 0.2] (这通常是 setosa)
new_sample = np.array([[5.1, 3.5, 1.4, 0.2]])
# 注意：必须使用之前训练好的 scaler 进行相同的标准化处理
new_sample_scaled = scaler.transform(new_sample)
prediction = model.predict(new_sample_scaled)
predicted_species = iris.target_names[prediction[0]]
print(f"样本特征 {new_sample[0]} 被预测为: {predicted_species}")
