# 1. SciPy 简介

SciPy 是 Python 中最常用的：

```text
科学计算库
```

基于 NumPy 构建，主要用于：

* 数值积分
* 优化与求根
* 插值
* 线性代数
* 统计分布
* 信号处理
* 稀疏矩阵
* 图像处理
* 常微分方程求解
* 特殊函数

与 NumPy 的关系：

```text
NumPy 提供数组和基本运算
SciPy 提供高级科学计算算法
```

例如：

```python
import numpy as np
from scipy import integrate

result, error = integrate.quad(lambda x: np.sin(x), 0, np.pi)
print(result)
```

结果：

```python
2.0
```

---

# 2. 安装

## 安装 SciPy

```bash
pip install scipy
```

---

## 测试安装

```python
import scipy
print(scipy.__version__)
```

---

# 3. SciPy 的核心结构

SciPy 按功能分为多个子模块：

| 模块 | 功能 |
| ---- | ---- |
| scipy.optimize | 优化、求根、曲线拟合 |
| scipy.integrate | 数值积分、ODE 求解 |
| scipy.interpolate | 插值（一维/多维） |
| scipy.linalg | 线性代数扩展 |
| scipy.stats | 统计分布、假设检验 |
| scipy.signal | 信号处理（滤波、卷积） |
| scipy.sparse | 稀疏矩阵 |
| scipy.spatial | 空间算法（KDTree，距离） |
| scipy.fft | 傅里叶变换 |
| scipy.special | 特殊函数（贝塞尔、伽马等） |
| scipy.ndimage | 多维图像处理 |
| scipy.io | 读取 Matlab、IDL、WAV 等文件 |

---

# 4. 优化与求根：scipy.optimize

---

## 单变量求根：root_scalar()

```python
from scipy import optimize

def f(x):
    return x**2 - 4

sol = optimize.root_scalar(f, bracket=[0,3])
print(sol.root)
```

结果：

```python
2.0
```

---

## 多变量方程组求根：root()

```python
def eqs(vars):
    x, y = vars
    return [x + y - 3, x - y - 1]

sol = optimize.root(eqs, [0,0])
print(sol.x)
```

结果：

```python
[2. 1.]
```

---

## 函数最小值：minimize()

```python
def f(x):
    return (x[0]-1)**2 + (x[1]-2)**2

res = optimize.minimize(f, [0,0])
print(res.x)
```

结果：

```python
[0.99999999 1.99999999]
```

---

## 曲线拟合：curve_fit()

```python
xdata = np.array([0,1,2,3])
ydata = np.array([1,2,0,4])

def model(x, a, b, c):
    return a * x**2 + b * x + c

popt, pcov = optimize.curve_fit(model, xdata, ydata)
print(popt)
```

结果示例：

```python
[ 0.5 -1.5  1. ]
```

---

# 5. 数值积分：scipy.integrate

---

## 定积分：quad()

```python
from scipy import integrate

result, error = integrate.quad(lambda x: np.exp(-x**2), -np.inf, np.inf)
print(result)
```

结果：

```python
1.7724538509055159
```

---

## 二重积分：dblquad()

```python
f = lambda y, x: x*y
result, error = integrate.dblquad(f, 0, 1, lambda x: 0, lambda x: 1-x)
print(result)
```

结果：

```python
0.041666666666666664
```

---

## 常微分方程初值问题：solve_ivp()

```python
def ode(t, y):
    return [y[1], -y[0]]  # y'' + y = 0

sol = integrate.solve_ivp(ode, [0, 10], [1, 0], t_eval=np.linspace(0,10,100))
print(sol.t[:5])
print(sol.y[0,:5])
```

结果：

```python
[0.         0.1010101  0.2020202  0.3030303  0.4040404 ]
[1.         0.99488394 0.97967068 0.9546855  0.92051786]
```

---

# 6. 插值：scipy.interpolate

---

## 一维插值：interp1d()

```python
from scipy import interpolate

x = np.linspace(0, 10, 5)
y = np.sin(x)
f_linear = interpolate.interp1d(x, y, kind='linear')
f_cubic = interpolate.interp1d(x, y, kind='cubic')

x_new = np.linspace(0, 10, 50)
y_new = f_cubic(x_new)
print(y_new[:5])
```

---

## 样条插值：CubicSpline

```python
cs = interpolate.CubicSpline(x, y)
print(cs(2.5))
```

---

## 多维插值：griddata

```python
points = np.random.rand(100, 2)
values = np.sin(points[:,0]) * np.cos(points[:,1])
xi = np.array([[0.5, 0.5], [0.2, 0.8]])
result = interpolate.griddata(points, values, xi, method='cubic')
print(result)
```

---

# 7. 线性代数：scipy.linalg

SciPy 的线性代数比 NumPy 更全面：

```python
from scipy import linalg

A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])
```

---

## 解线性方程

```python
b = np.array([1,2])
x = linalg.solve(A, b)
print(x)
```

结果：

```python
[0.  0.5]
```

---

## 矩阵指数

```python
expA = linalg.expm(A)
print(expA)
```

---

## 奇异值分解

```python
U, s, Vh = linalg.svd(A)
print(s)
```

结果：

```python
[5.4649857  0.36596619]
```

---

## 最小二乘解

```python
x, res, rk, s = linalg.lstsq(A, b)
print(x)
```

---

# 8. 统计：scipy.stats

---

## 常用概率分布

```python
from scipy import stats

# 正态分布
rvs = stats.norm.rvs(loc=0, scale=1, size=1000)
pdf = stats.norm.pdf(0, loc=0, scale=1)
cdf = stats.norm.cdf(0, loc=0, scale=1)
print(pdf, cdf)
```

结果：

```python
0.3989422804014327 0.5
```

---

## 描述统计

```python
data = np.random.randn(100)
print(stats.describe(data))
```

结果示例：

```python
DescribeResult(nobs=100, minmax=(-2.5, 2.3), mean=0.05, variance=0.98, skewness=0.1, kurtosis=0.2)
```

---

## t 检验

```python
a = np.random.randn(20)
b = np.random.randn(20,)
t_stat, p_value = stats.ttest_ind(a, b)
print(p_value)
```

---

## 线性回归

```python
x = np.arange(10)
y = 2*x + 1 + np.random.randn(10)
slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
print(slope, intercept)
```

---

# 9. 信号处理：scipy.signal

---

## 卷积

```python
from scipy import signal

a = [1, 2, 3]
b = [4, 5, 6]
c = signal.convolve(a, b)
print(c)
```

结果：

```python
[ 4 13 28 27 18]
```

---

## 滤波：设计低通滤波器

```python
b, a = signal.butter(4, 0.2, 'low')  # 归一化截止频率 0.2
t = np.linspace(0, 1, 500)
x = np.sin(2*np.pi*5*t) + 0.5*np.random.randn(500)
y = signal.filtfilt(b, a, x)
```

---

## 频谱图

```python
f, t, Sxx = signal.spectrogram(x, fs=1000)
```

---

# 10. 稀疏矩阵：scipy.sparse

---

## 创建稀疏矩阵

```python
from scipy import sparse

row = np.array([0,1,2])
col = np.array([1,2,0])
data = np.array([1,2,3])
sp_mat = sparse.coo_matrix((data, (row, col)), shape=(3,3))
print(sp_mat.toarray())
```

结果：

```python
[[0 1 0]
 [0 0 2]
 [3 0 0]]
```

---

## 稀疏线性代数

```python
from scipy.sparse.linalg import spsolve
b = np.array([1,1,1])
x = spsolve(sp_mat.tocsr(), b)
print(x)
```

---

# 11. 空间算法：scipy.spatial

---

## KDTree 最近邻

```python
from scipy import spatial

points = np.random.rand(10, 2)
tree = spatial.KDTree(points)
dist, idx = tree.query([0.5, 0.5], k=3)
print(idx)
```

---

## 距离计算

```python
dist = spatial.distance.euclidean([0,0], [3,4])
print(dist)
```

结果：

```python
5.0
```

---

# 12. 傅里叶变换：scipy.fft

SciPy 的 fft 模块与 NumPy 类似，但功能更全：

```python
from scipy import fft

t = np.linspace(0, 1, 500)
x = np.sin(2*np.pi*50*t) + 0.5*np.sin(2*np.pi*120*t)
yf = fft.fft(x)
freq = fft.fftfreq(len(x), t[1]-t[0])
print(freq[:5])
```

---

# 13. 特殊函数：scipy.special

```python
from scipy import special

# 贝塞尔函数
print(special.jv(0, 1))

# 伽马函数
print(special.gamma(5))

# 误差函数
print(special.erf(1))
```

结果：

```python
0.7651976865579666
24.0
0.8427007929497149
```

---

# 14. 图像处理：scipy.ndimage

```python
from scipy import ndimage
import matplotlib.pyplot as plt

# 创建简单图像
img = np.zeros((100,100))
img[40:60, 40:60] = 1

# 高斯滤波
img_smooth = ndimage.gaussian_filter(img, sigma=2)

# 旋转
img_rot = ndimage.rotate(img, 45, reshape=False)

# 边缘检测
img_edges = ndimage.sobel(img)
```

---

# 15. 文件 IO：scipy.io

---

## 读取 Matlab 文件

```python
from scipy import io

# 写入示例
io.savemat('data.mat', {'x': np.array([1,2,3])})

# 读取
mat = io.loadmat('data.mat')
print(mat['x'])
```

结果：

```python
[[1 2 3]]
```

---

## 读取 WAV 文件

```python
from scipy.io import wavfile

fs, data = wavfile.read('audio.wav')
print(fs, data.shape)
```

---

# 16. SciPy 与其他库的对比

| 功能 | SciPy | NumPy | SymPy |
| ---- | ----- | ----- | ----- |
| 数值积分 | ✅ | ❌ | ✅(符号) |
| 优化求解 | ✅ | 有限 | ✅(符号) |
| 插值 | ✅ | ❌ | ❌ |
| 统计分布 | ✅ | 基础 | ❌ |
| 信号处理 | ✅ | 有限 | ❌ |
| 稀疏矩阵 | ✅ | ❌ | ❌ |
| 特殊函数 | ✅ | 有限 | 部分 |
| ODE 求解 | ✅ | ❌ | ✅(符号) |

---

# 17. 常见应用

---

## 工程计算

* 控制系统仿真
* 电路分析
* 力学模拟

---

## 数据分析

* 曲线拟合
* 统计假设检验
* 插值缺失数据

---

## 信号与图像处理

* 滤波器设计
* 图像去噪
* 特征提取

---

## 机器学习预处理

* 概率分布拟合
* 距离计算
* 稀疏特征

---

# 18. 常见问题

---

## 1. 与 NumPy 函数命名冲突

错误：

```text
同时导入 from scipy import * 和 from numpy import *
```

解决：

```python
import numpy as np
import scipy as sp
```

---

## 2. 积分结果不准确

使用 `quad` 时注意被积函数奇点，可指定 `points` 参数。

---

## 3. 优化不收敛

尝试改变初始值 `x0`，或使用不同方法（method='BFGS' 等）。

---

## 4. 稀疏矩阵运算慢

尽量使用 `csr_matrix` 或 `csc_matrix` 格式进行线性代数运算。

---

# 19. 推荐学习路线

```text
安装与子模块概览
↓
优化与求根（optimize）
↓
数值积分（integrate）
↓
插值（interpolate）
↓
线性代数（linalg）
↓
统计（stats）
↓
信号处理（signal）
↓
稀疏矩阵（sparse）
↓
特殊函数与傅里叶变换
↓
图像处理与文件 IO
```

---

# 20. 推荐练习项目

## 初级

* 求解一元/多元方程
* 计算定积分与二重积分
* 数据插值与外推

---

## 中级

* 曲线拟合与参数估计
* 滤波器设计与信号滤波
* 统计假设检验（t检验、卡方检验）

---

## 高级

* 求解常微分方程组（如洛伦兹方程）
* 稀疏矩阵求解大型线性系统
* 图像去噪与边缘检测流水线
* 自定义概率分布拟合