# 1. Scikit-learn 简介

Scikit-learn（简称 sklearn）是 Python 中最常用的：

```text
机器学习库
```

基于 NumPy、SciPy 和 Matplotlib 构建，主要用于：

* 分类（Classification）
* 回归（Regression）
* 聚类（Clustering）
* 降维（Dimensionality Reduction）
* 数据预处理（Preprocessing）
* 模型选择与评估（Model Selection）

与 NumPy 不同：

```text
NumPy：数值计算，提供多维数组
SciPy：科学计算，提供数值算法
Matplotlib：数据可视化
Scikit-learn：机器学习算法与工具
```

Scikit-learn 与 NumPy/SciPy 的关系：

```text
NumPy 提供数据容器（ndarray）
SciPy 提供底层科学计算
Scikit-learn 在此基础上构建机器学习算法
```

例如：

NumPy：

```python
import numpy as np
X = np.array([[1, 2], [3, 4], [5, 6]])
y = np.array([0, 1, 0])
```

Scikit-learn：

```python
from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier()
clf.fit(X, y)          # 训练模型
pred = clf.predict([[2, 3]])  # 预测
```

---

# 2. 安装

## 安装 Scikit-learn

```bash
pip install -U scikit-learn
```

或使用 conda：

```bash
conda install scikit-learn
```

---

## 依赖项

```text
• Python >= 3.5
• NumPy >= 1.8.2
• SciPy >= 0.13.3
```

---

## 测试安装

```python
import sklearn
print(sklearn.__version__)
```

---

# 3. Scikit-learn 的核心思想

Scikit-learn 的核心设计理念：

```text
统一的 API 接口
所有算法都遵循相同的调用模式
```

核心接口：

```text
1. 估计器（Estimator）：
   - 任何可以拟合数据的对象
   - 实现 fit() 方法

2. 转换器（Transformer）：
   - 用于数据预处理和特征工程
   - 实现 fit() 和 transform() 方法

3. 预测器（Predictor）：
   - 用于监督学习任务
   - 实现 fit() 和 predict() 方法
```

---

# 4. 核心概念

## 4.1 估计器（Estimator）

估计器是所有机器学习模型的基类。

```text
任何实现了 fit() 方法的对象都称为估计器
fit() 方法从数据中学习参数
```

示例：

```python
from sklearn.linear_model import LinearRegression

model = LinearRegression()   # 创建估计器
model.fit(X, y)              # 拟合数据
```

---

## 4.2 转换器（Transformer）

转换器是用于数据预处理或特征工程的特殊估计器。

```text
实现 fit() 方法：学习转换规则
实现 transform() 方法：应用转换
```

示例：

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()        # 创建转换器
scaler.fit(X_train)              # 学习均值和标准差
X_scaled = scaler.transform(X_train)  # 转换数据
# 或一步完成
X_scaled = scaler.fit_transform(X_train)
```

常见转换器：

| 转换器 | 用途 |
| ------ | ---- |
| StandardScaler | 标准化（均值0，方差1） |
| MinMaxScaler | 归一化（缩放到 [0,1]） |
| SimpleImputer | 缺失值填充 |
| OneHotEncoder | 独热编码 |
| LabelEncoder | 标签编码 |
| PCA | 主成分分析（降维） |

---

## 4.3 预测器（Predictor）

预测器用于监督学习任务。

```text
实现 fit() 方法：在训练集上学习
实现 predict() 方法：在测试集上预测
```

示例：

```python
from sklearn.ensemble import RandomForestClassifier

clf = RandomForestClassifier()
clf.fit(X_train, y_train)        # 训练
y_pred = clf.predict(X_test)     # 预测
```

---

## 4.4 管道（Pipeline）

管道将多个估计器串联成一个完整的工作流。

```text
管道中除最后一个估计器外，其余都必须是转换器
最后一个估计器可以是任意类型（分类器、回归器等）
```

示例：

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

pipeline = Pipeline([
    ('scaler', StandardScaler()),          # 转换器
    ('classifier', LogisticRegression())   # 预测器
])

pipeline.fit(X_train, y_train)             # 一步完成训练
y_pred = pipeline.predict(X_test)          # 一步完成预测
```

管道的作用：

```text
• 便捷性：一次 fit/predict 完成全部步骤
• 联合参数调优：网格搜索可优化所有步骤的超参数
• 避免数据泄露：交叉验证时不会泄露测试集信息
```

---

# 5. 六大模块

Scikit-learn 包含六大核心任务模块：

| 模块 | 任务 | 常用算法 |
| ---- | ---- | -------- |
| 分类（Classification） | 识别对象类别 | SVM、随机森林、KNN、逻辑回归 |
| 回归（Regression） | 预测连续值 | 线性回归、岭回归、Lasso、SVR |
| 聚类（Clustering） | 自动分组 | K-Means、DBSCAN、层次聚类 |
| 降维（Dimensionality Reduction） | 减少特征数量 | PCA、t-SNE、LDA |
| 模型选择（Model Selection） | 评估与调参 | 交叉验证、网格搜索 |
| 预处理（Preprocessing） | 数据清洗与转换 | 标准化、归一化、编码 |

---

# 6. 数据预处理

## 6.1 标准化（Standardization）

将数据转换为均值为0、方差为1的标准正态分布。

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
```

---

## 6.2 归一化（Normalization）

将数据缩放到指定范围（如 [0, 1]）。

```python
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)
```

---

## 6.3 编码分类变量

将分类数据转换为数值。

```python
from sklearn.preprocessing import OneHotEncoder, LabelEncoder

# 独热编码（创建虚拟变量）
encoder = OneHotEncoder()
X_encoded = encoder.fit_transform(X_categorical)

# 标签编码（转为整数）
le = LabelEncoder()
y_encoded = le.fit_transform(y)
```

---

## 6.4 处理缺失值

```python
from sklearn.impute import SimpleImputer

# 用均值填充
imputer = SimpleImputer(strategy='mean')
X_imputed = imputer.fit_transform(X)
```

其他策略：

```text
strategy='mean'    均值填充
strategy='median'  中位数填充
strategy='most_frequent'  众数填充
strategy='constant'  常量填充
```

---

## 6.5 特征选择

选择最重要的特征子集。

```python
from sklearn.feature_selection import SelectKBest, SelectFromModel

# 选择最好的 K 个特征
selector = SelectKBest(k=5)
X_selected = selector.fit_transform(X, y)

# 基于模型选择
from sklearn.ensemble import RandomForestClassifier
selector = SelectFromModel(RandomForestClassifier())
X_selected = selector.fit_transform(X, y)
```

---

# 7. 监督学习

## 7.1 分类（Classification）

识别对象属于哪个类别。

常用算法：

| 算法 | 说明 |
| ---- | ---- |
| LogisticRegression | 逻辑回归 |
| SVC | 支持向量机分类器 |
| DecisionTreeClassifier | 决策树 |
| RandomForestClassifier | 随机森林 |
| GradientBoostingClassifier | 梯度提升树 |
| KNeighborsClassifier | K近邻 |

示例：

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# 分割数据
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 训练
clf = RandomForestClassifier(n_estimators=100)
clf.fit(X_train, y_train)

# 预测
y_pred = clf.predict(X_test)
accuracy = clf.score(X_test, y_test)
```

---

## 7.2 回归（Regression）

预测与对象相关联的连续值。

常用算法：

| 算法 | 说明 |
| ---- | ---- |
| LinearRegression | 线性回归 |
| Ridge | 岭回归（L2正则化） |
| Lasso | Lasso回归（L1正则化） |
| SVR | 支持向量机回归 |
| RandomForestRegressor | 随机森林回归 |

示例：

```python
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
```

---

# 8. 无监督学习

## 8.1 聚类（Clustering）

将相似对象自动分组。

常用算法：

| 算法 | 说明 |
| ---- | ---- |
| KMeans | K均值聚类 |
| DBSCAN | 基于密度的聚类 |
| AgglomerativeClustering | 层次聚类 |

示例：

```python
from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=3)
kmeans.fit(X)
labels = kmeans.labels_           # 每个样本的簇标签
centers = kmeans.cluster_centers_ # 簇中心
```

---

## 8.2 降维（Dimensionality Reduction）

减少随机变量的数量。

常用算法：

| 算法 | 说明 |
| ---- | ---- |
| PCA | 主成分分析 |
| t-SNE | t分布随机邻域嵌入（可视化） |
| LDA | 线性判别分析 |

示例：

```python
from sklearn.decomposition import PCA

pca = PCA(n_components=2)      # 降到2维
X_reduced = pca.fit_transform(X)
```

---

# 9. 模型选择与评估

## 9.1 划分训练集与测试集

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
```

---

## 9.2 交叉验证

```python
from sklearn.model_selection import cross_val_score

scores = cross_val_score(model, X, y, cv=5)  # 5折交叉验证
print(scores.mean(), scores.std())
```

---

## 9.3 网格搜索（超参数调优）

```python
from sklearn.model_selection import GridSearchCV

param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [3, 5, 7]
}

grid_search = GridSearchCV(
    RandomForestClassifier(),
    param_grid,
    cv=5
)
grid_search.fit(X_train, y_train)

print(grid_search.best_params_)   # 最佳参数
print(grid_search.best_score_)    # 最佳得分
```

随机搜索（更高效）：

```python
from sklearn.model_selection import RandomizedSearchCV

random_search = RandomizedSearchCV(
    model, param_distributions, n_iter=50, cv=5
)
```

---

# 10. 评估指标

## 10.1 分类指标

```python
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score,
    f1_score, confusion_matrix, classification_report
)

y_pred = model.predict(X_test)

print("准确率:", accuracy_score(y_test, y_pred))
print("精确率:", precision_score(y_test, y_pred))
print("召回率:", recall_score(y_test, y_pred))
print("F1分数:", f1_score(y_test, y_pred))
print("混淆矩阵:\n", confusion_matrix(y_test, y_pred))
print("分类报告:\n", classification_report(y_test, y_pred))
```

---

## 10.2 回归指标

```python
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

print("MSE:", mean_squared_error(y_test, y_pred))
print("MAE:", mean_absolute_error(y_test, y_pred))
print("R²:", r2_score(y_test, y_pred))
```

---

# 11. Scikit-learn 与其他库的对比

| 功能 | Scikit-learn | NumPy | SciPy | Matplotlib |
| ---- | ------------ | ----- | ----- | ---------- |
| 主要用途 | 机器学习 | 数值计算 | 科学计算 | 数据可视化 |
| 数据类型 | NumPy ndarray | ndarray | ndarray | 图形对象 |
| 机器学习算法 | ✅ 大量内置 | ❌ | 有限 | ❌ |
| 数据预处理 | ✅ | ❌ | ❌ | ❌ |
| 模型评估 | ✅ | ❌ | ❌ | ❌ |
| 深度学习 | ❌ | ❌ | ❌ | ❌ |

Scikit-learn 与深度学习库：

```text
Scikit-learn：传统机器学习算法（SVM、随机森林、线性模型等）
TensorFlow/PyTorch：深度学习（神经网络）
两者可以互补使用
```

---

# 12. 常见应用场景

| 任务 | 应用 | 推荐算法 |
| ---- | ---- | -------- |
| 分类 | 垃圾邮件识别、疾病诊断、用户行为预测 | 逻辑回归、SVM、随机森林 |
| 回归 | 房价预测、股价预测、销量预测 | 线性回归、岭回归、梯度提升 |
| 聚类 | 客户细分、图像分割、用户画像 | K-Means、DBSCAN |
| 降维 | 数据可视化、特征压缩 | PCA、t-SNE |

---

# 13. 常见问题

## 1. 数据格式要求

```text
X: (n_samples, n_features) 形状的二维数组
y: (n_samples,) 形状的一维数组
推荐使用 NumPy ndarray 或 Pandas DataFrame
```

---

## 2. 过拟合问题

```text
使用交叉验证评估模型
增加正则化参数（C、alpha）
减少模型复杂度（max_depth、n_estimators）
增加训练数据
使用特征选择
```

---

## 3. 分类问题 vs 回归问题

```text
分类：目标变量是离散的（类别）
回归：目标变量是连续的（数值）
选择算法时需匹配任务类型
```

---

## 4. 内存不足

```text
使用稀疏矩阵（scipy.sparse）
使用增量学习算法（PartialFit）
分批处理数据
```

---

# 14. 推荐学习路线

```text
安装与基本概念
↓
数据预处理（标准化、编码、填充）
↓
监督学习 - 分类（逻辑回归、SVM、随机森林）
↓
监督学习 - 回归（线性回归、岭回归）
↓
模型评估（交叉验证、评估指标）
↓
超参数调优（网格搜索、随机搜索）
↓
无监督学习（聚类、降维）
↓
管道（Pipeline）
↓
综合项目实战
```

---

# 15. 推荐练习项目

## 初级

* 鸢尾花数据集分类（Iris）
* 波士顿房价预测（回归）

---

## 中级

* 手写数字识别（MNIST）
* 泰坦尼克号生存预测
* 使用管道构建完整工作流

---

## 高级

* 特征工程与模型融合（Ensemble）
* 文本分类（使用 TfidfVectorizer）
* 自定义转换器与评估器

---

# 16. 总结与速查

## 常用导入

```python
# 预处理
from sklearn.preprocessing import StandardScaler, MinMaxScaler, OneHotEncoder
from sklearn.impute import SimpleImputer

# 模型选择
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV

# 分类
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier

# 回归
from sklearn.linear_model import LinearRegression, Ridge, Lasso

# 聚类
from sklearn.cluster import KMeans, DBSCAN

# 降维
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE

# 评估
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.metrics import mean_squared_error, r2_score

# 管道
from sklearn.pipeline import Pipeline
```

## 标准流程

```text
数据加载 → 预处理 → 划分训练/测试集 → 创建模型 → 训练 → 预测 → 评估
```