---

# 1. NumPy 简介

NumPy 是 Python 中最常用的：

```text
数值计算库
```

主要用于：

* 多维数组（ndarray）
* 向量化运算
* 数学函数
* 线性代数
* 随机数生成
* 傅里叶变换
* 信号处理
* 图像处理

与 SymPy 不同：

```text
SymPy 主要做符号计算
NumPy 主要做数值计算
```

例如：

SymPy：

```python
from sympy import symbols
x = symbols('x')
print(x + x)
```

结果：

```python
2*x
```

NumPy：

```python
import numpy as np
a = np.array([1,2])
print(a + a)
```

结果：

```python
[2 4]
```

因为：

```text
NumPy 直接操作数值数组
```

---

# 2. 安装

## 安装 NumPy

```bash
pip install numpy
```

---

## 测试安装

```python
import numpy as np

print(np.__version__)
```

---

# 3. NumPy 的核心思想

NumPy 的核心：

```text
多维数组对象 + 向量化计算
```

例如：

```python
import numpy as np

arr = np.array([1,2,3])
print(arr * 2)
```

结果：

```python
[2 4 6]
```

而不是用循环。

因此：

* 速度快（底层 C/Fortran）
* 代码简洁
* 支持广播（broadcasting）

---

# 4. 创建数组

---

## array()

从列表创建。

```python
import numpy as np

a = np.array([1,2,3])
print(a)
```

结果：

```python
[1 2 3]
```

---

## 多维数组

```python
b = np.array([[1,2],[3,4]])
print(b)
```

结果：

```python
[[1 2]
 [3 4]]
```

---

## 常用创建函数

```python
zeros = np.zeros((2,3))
ones = np.ones((2,3))
eye = np.eye(3)
full = np.full((2,2), 7)
arange = np.arange(0,10,2)
linspace = np.linspace(0,1,5)
random = np.random.rand(2,3)

print("zeros:\n", zeros)
print("ones:\n", ones)
print("eye:\n", eye)
print("full:\n", full)
print("arange:", arange)
print("linspace:", linspace)
print("random:\n", random)
```

结果（random 每次不同）：

```text
zeros:
 [[0. 0. 0.]
 [0. 0. 0.]]
ones:
 [[1. 1. 1.]
 [1. 1. 1.]]
eye:
 [[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
full:
 [[7 7]
 [7 7]]
arange: [0 2 4 6 8]
linspace: [0.   0.25 0.5  0.75 1.  ]
random:
 [[0.123 0.456 0.789]
 [0.321 0.654 0.987]]
```

---

# 5. 数组属性

```python
a = np.array([[1,2,3],[4,5,6]])
print("shape:", a.shape)
print("dtype:", a.dtype)
print("size:", a.size)
print("ndim:", a.ndim)
```

结果：

```python
shape: (2, 3)
dtype: int64
size: 6
ndim: 2
```

---

# 6. 索引与切片

---

## 基本索引

```python
a = np.array([10,20,30,40])
print(a[0])
print(a[-1])
```

结果：

```python
10
40
```

---

## 二维索引

```python
b = np.array([[1,2,3],[4,5,6]])
print(b[0,1])
print(b[1,:])
```

结果：

```python
2
[4 5 6]
```

---

## 切片

```python
print(a[1:3])
print(b[:,0:2])
```

结果：

```python
[20 30]
[[1 2]
 [4 5]]
```

---

# 7. 形状操作

---

## reshape()

```python
a = np.arange(6)
b = a.reshape(2,3)
print(b)
```

结果：

```python
[[0 1 2]
 [3 4 5]]
```

---

## flatten() / ravel()

```python
print(b.flatten())
```

结果：

```python
[0 1 2 3 4 5]
```

---

## transpose() 或 .T

```python
print(b.T)
```

结果：

```python
[[0 3]
 [1 4]
 [2 5]]
```

---

# 8. 数组运算

---

## 逐元素运算

```python
a = np.array([1,2,3])
b = np.array([4,5,6])

print(a + b)
print(a * b)
print(a ** 2)
```

结果：

```python
[5 7 9]
[ 4 10 18]
[1 4 9]
```

---

## 广播

```python
print(a + 10)
```

结果：

```python
[11 12 13]
```

---

## 数学函数

```python
print(np.sin(a))
print(np.exp(a))
print(np.sqrt(a))
```

结果：

```python
[0.84147098 0.90929743 0.14112001]
[ 2.71828183  7.3890561  20.08553692]
[1.         1.41421356 1.73205081]
```

---

# 9. 聚合函数

```python
a = np.array([[1,2],[3,4]])
print("sum:", np.sum(a))
print("mean:", np.mean(a))
print("max:", np.max(a))
print("min:", np.min(a))
print("std:", np.std(a))
print("sum axis=0:", np.sum(a, axis=0))
print("sum axis=1:", np.sum(a, axis=1))
```

结果：

```python
sum: 10
mean: 2.5
max: 4
min: 1
std: 1.118033988749895
sum axis=0: [4 6]
sum axis=1: [3 7]
```

---

# 10. 线性代数

---

## dot() 矩阵乘法

```python
A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])
print(np.dot(A,B))
```

结果：

```python
[[19 22]
 [43 50]]
```

或使用 `@` 运算符：

```python
print(A @ B)
```

---

## 行列式

```python
print(np.linalg.det(A))
```

结果：

```python
-2.0000000000000004
```

---

## 逆矩阵

```python
print(np.linalg.inv(A))
```

结果：

```python
[[-2.   1. ]
 [ 1.5 -0.5]]
```

---

## 特征值/特征向量

```python
eigvals, eigvecs = np.linalg.eig(A)
print("特征值:", eigvals)
print("特征向量:\n", eigvecs)
```

结果：

```python
特征值: [-0.37228132  5.37228132]
特征向量:
 [[-0.82456484 -0.41597356]
 [ 0.56576746 -0.90937671]]
```

---

# 11. 随机数

---

## rand() 均匀分布

```python
print(np.random.rand(3))
```

结果：

```python
[0.123 0.456 0.789]
```

---

## randn() 正态分布

```python
print(np.random.randn(2,2))
```

---

## randint() 整数随机

```python
print(np.random.randint(0,10,size=5))
```

---

## 设置种子

```python
np.random.seed(42)
print(np.random.rand(3))
```

结果（固定）：

```python
[0.37454012 0.95071431 0.73199394]
```

---

# 12. 保存与读取

---

## save() / load()

```python
a = np.array([1,2,3])
np.save('array.npy', a)
b = np.load('array.npy')
print(b)
```

结果：

```python
[1 2 3]
```

---

## savetxt() / loadtxt()

```python
np.savetxt('array.txt', a)
c = np.loadtxt('array.txt')
print(c)
```

结果：

```python
[1. 2. 3.]
```

---

# 13. NumPy 与 SymPy 的区别

| 功能   | NumPy | SymPy |
| ---- | ----- | ----- |
| 计算类型 | 数值计算  | 符号计算  |
| 精度   | 浮点近似  | 理论精确  |
| 求导   | 不支持   | 支持    |
| 积分   | 不支持   | 支持    |
| 方程求解 | 有限支持  | 支持    |
| 速度   | 很快    | 较慢    |

---

# 14. 常见应用

---

## 科学计算

* 数据处理
* 数值模拟

---

## 机器学习

* 特征矩阵
* 模型参数

---

## 图像处理

* 像素数组
* 变换

---

## 信号处理

* 滤波
* FFT

---

# 15. 常见问题

---

## 1. 混淆 Python 列表与 NumPy 数组

错误：

```text
列表乘法是重复，不是逐元素运算
```

正确：

```python
np.array([1,2]) * 2   # [2,4]
[1,2] * 2             # [1,2,1,2]
```

---

## 2. 忘记导入 numpy

错误：

```text
NameError: name 'np' is not defined
```

---

## 3. 形状不匹配

错误：

```text
ValueError: operands could not be broadcast together
```

---

# 16. 推荐学习路线

```text
array 创建
↓
索引与切片
↓
形状操作
↓
数学运算
↓
聚合函数
↓
广播机制
↓
线性代数
↓
随机数
↓
文件读写
```

---

# 17. 推荐练习项目

## 初级

* 数组统计分析
* 矩阵乘法计算器

---

## 中级

* 图像灰度化与翻转
* 多项式拟合

---

## 高级

* 神经网络前向传播
* 快速傅里叶变换（FFT）滤波
* 蒙特卡洛模拟

