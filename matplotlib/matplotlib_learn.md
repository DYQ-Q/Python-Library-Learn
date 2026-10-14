# 1. Matplotlib 简介

Matplotlib 是 Python 中最常用的：

```text
数据可视化库
```

主要用于：

* 折线图
* 散点图
* 柱状图
* 直方图
* 饼图
* 等高线图
* 3D 图
* 图像显示

与 NumPy 配合：

```text
NumPy 提供数据
Matplotlib 绘制图形
```

例如：

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,3])
y = np.array([1,4,9])

plt.plot(x, y)
plt.show()
```

结果：

```text
显示一个折线图窗口
```

---

# 2. 安装

## 安装 Matplotlib

```bash
pip install matplotlib
```

---

## 测试安装

```python
import matplotlib.pyplot as plt

print(plt.__version__)
```

---

# 3. Matplotlib 的核心思想

Matplotlib 的核心：

```text
图形元素对象化 + 状态机接口 / 面向对象接口
```

两种接口：

```text
pyplot 状态机（快速绘图）
Axes 面向对象（精细控制）
```

例如：

pyplot 风格：

```python
plt.plot([1,2,3], [1,4,9])
plt.show()
```

面向对象风格：

```python
fig, ax = plt.subplots()
ax.plot([1,2,3], [1,4,9])
plt.show()
```

---

# 4. 基本绘图：plot()

---

## 绘制折线图

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y)
plt.show()
```

---

## 设置线条样式

```python
plt.plot(x, y, color='red', linestyle='--', linewidth=2, marker='o', markersize=4)
plt.show()
```

---

## 多条曲线

```python
y2 = np.cos(x)
plt.plot(x, y, label='sin')
plt.plot(x, y2, label='cos')
plt.legend()
plt.show()
```

---

# 5. 散点图：scatter()

```python
x = np.random.randn(100)
y = np.random.randn(100)

plt.scatter(x, y, alpha=0.5, c='blue')
plt.show()
```

---

# 6. 柱状图：bar()

```python
categories = ['A', 'B', 'C']
values = [10, 24, 17]

plt.bar(categories, values, color=['red','green','blue'])
plt.show()
```

---

## 水平柱状图：barh()

```python
plt.barh(categories, values)
plt.show()
```

---

# 7. 直方图：hist()

```python
data = np.random.randn(1000)

plt.hist(data, bins=30, edgecolor='black', alpha=0.7)
plt.show()
```

---

# 8. 饼图：pie()

```python
sizes = [25, 35, 20, 20]
labels = ['A', 'B', 'C', 'D']

plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.axis('equal')
plt.show()
```

---

# 9. 子图：subplot() / subplots()

---

## subplot() 网格

```python
plt.subplot(2,2,1)
plt.plot([1,2],[1,4])

plt.subplot(2,2,2)
plt.scatter([1,2],[1,4])

plt.subplot(2,2,3)
plt.bar([1,2],[1,4])

plt.subplot(2,2,4)
plt.hist([1,2,1,2])

plt.tight_layout()
plt.show()
```

---

## subplots() 面向对象

```python
fig, axes = plt.subplots(2,2, figsize=(8,6))

axes[0,0].plot([1,2],[1,4])
axes[0,1].scatter([1,2],[1,4])
axes[1,0].bar([1,2],[1,4])
axes[1,1].hist([1,2,1,2])

plt.tight_layout()
plt.show()
```

---

# 10. 图表装饰

---

## 标题、标签、图例

```python
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y, label='sin(x)')
plt.title('Sine Wave')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()
```

---

## 设置坐标轴范围

```python
plt.xlim(0, 10)
plt.ylim(-1.5, 1.5)
```

---

## 刻度设置

```python
plt.xticks(np.arange(0, 11, 2))
plt.yticks([-1, 0, 1])
```

---

# 11. 保存图形

```python
plt.plot([1,2,3], [1,4,9])
plt.savefig('plot.png', dpi=300, bbox_inches='tight')
```

支持的格式：

```text
png, pdf, svg, jpg, eps 等
```

---

# 12. 样式与美化

---

## 内置样式

```python
print(plt.style.available)
```

```python
plt.style.use('ggplot')
plt.plot([1,2,3], [1,4,9])
plt.show()
```

---

## 自定义颜色

```python
colors = ['#1f77b4', '#ff7f0e', '#2ca02c']
```

---

# 13. 3D 绘图

```python
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = np.arange(-5, 5, 0.25)
y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))

ax.plot_surface(X, Y, Z, cmap='viridis')
plt.show()
```

---

# 14. 图像显示：imshow()

```python
import matplotlib.image as mpimg

img = mpimg.imread('image.jpg')
plt.imshow(img)
plt.axis('off')
plt.show()
```

或显示数组：

```python
data = np.random.rand(10,10)
plt.imshow(data, cmap='hot')
plt.colorbar()
plt.show()
```

---

# 15. 箱线图：boxplot()

```python
data = [np.random.randn(100), np.random.randn(100)+1]
plt.boxplot(data, labels=['Group1', 'Group2'])
plt.show()
```

---

# 16. 填充图：fill_between()

```python
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1, label='sin')
plt.plot(x, y2, label='cos')
plt.fill_between(x, y1, y2, where=(y1>y2), color='red', alpha=0.3)
plt.fill_between(x, y1, y2, where=(y1<=y2), color='blue', alpha=0.3)
plt.legend()
plt.show()
```

---

# 17. 极坐标图

```python
theta = np.linspace(0, 2*np.pi, 100)
r = 1 + 0.5*np.sin(3*theta)

plt.subplot(111, projection='polar')
plt.plot(theta, r)
plt.show()
```

---

# 18. 动画

```python
import matplotlib.animation as animation

fig, ax = plt.subplots()
x = np.linspace(0, 2*np.pi, 100)
line, = ax.plot(x, np.sin(x))

def animate(i):
    line.set_ydata(np.sin(x + i/10))
    return line,

ani = animation.FuncAnimation(fig, animate, frames=100, interval=50)
plt.show()
```

---

# 19. 文本标注

```python
plt.plot([1,2,3], [1,4,9])
plt.text(2, 5, 'peak', fontsize=12, ha='center')
plt.annotate('maximum', xy=(3,9), xytext=(2.5,7),
             arrowprops=dict(facecolor='black', shrink=0.05))
plt.show()
```

---

# 20. 常用图形对比

| 图形类型 | 函数 | 用途 |
| ------ | ---- | ---- |
| 折线图 | plot() | 趋势 |
| 散点图 | scatter() | 分布 |
| 柱状图 | bar() | 比较 |
| 直方图 | hist() | 分布统计 |
| 饼图 | pie() | 占比 |
| 箱线图 | boxplot() | 统计摘要 |
| 等高线 | contour() | 三维曲面 |
| 3D曲面 | plot_surface() | 三维关系 |

---

# 21. Matplotlib 与 NumPy/SymPy 的区别

| 功能 | Matplotlib | NumPy | SymPy |
| ---- | ---------- | ----- | ----- |
| 主要用途 | 可视化 | 数值计算 | 符号计算 |
| 数据类型 | 数组/图像 | ndarray | 符号表达式 |
| 输出 | 图形窗口/文件 | 数值数组 | 符号表达式 |

---

# 22. 常见应用

---

## 数据探索

* 分布可视化
* 相关性散点图

---

## 科学论文

* 高质量图表
* 多子图排版

---

## 机器学习

* 损失曲线
* 混淆矩阵热图

---

## 信号处理

* 频谱图
* 时域波形

---

# 23. 常见问题

---

## 1. 图形不显示

错误：

```text
代码运行完没有窗口
```

解决方法：

```python
plt.show()  # 必须调用
```

或 Jupyter 中：

```python
%matplotlib inline
```

---

## 2. 中文乱码

```python
plt.rcParams['font.sans-serif'] = ['SimHei']  # 或 ['Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False
```

---

## 3. 负号显示为方块

同上设置 `axes.unicode_minus = False`

---

## 4. 图形保存为空白

原因：`savefig()` 在 `show()` 之后调用。

解决：

```python
plt.savefig('plot.png')  # 先保存
plt.show()                # 后显示
```

---

# 24. 推荐学习路线

```text
安装与基本绘图
↓
折线图、散点图
↓
柱状图、直方图、饼图
↓
子图与布局
↓
图表装饰（标题、标签、图例、网格）
↓
保存与样式
↓
3D 绘图
↓
动画与交互
```

---

# 25. 推荐练习项目

## 初级

* 正弦/余弦曲线绘制
* 随机数直方图

---

## 中级

* 多子图股票K线图
* 气温变化折线图加填充

---

## 高级

* 实时数据动态更新动画
* 三维曲面与等高线叠加
* 自定义绘图函数库封装