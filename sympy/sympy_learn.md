# SymPy 学习笔记

---

# 1. SymPy 简介

SymPy 是 Python 中最常用的：

```text
符号数学库
```

主要用于：

* 代数计算
* 微积分
* 方程求解
* 矩阵运算
* 级数展开
* 极限计算
* 微分方程
* 符号推导

与 NumPy 不同：

```text
NumPy 主要做数值计算
SymPy 主要做符号计算
```

例如：

NumPy：

```python
2 + 3
```

得到：

```python
5
```

而 SymPy：

```python
x + x
```

得到：

```python
2*x
```

因为：

```text
x 是符号
不是数值
```

---

# 2. 安装

## 安装 SymPy

```bash
pip install sympy
```

---

## 测试安装

```python
import sympy

print(sympy.__version__)
```

---

# 3. SymPy 的核心思想

SymPy 的核心：

```text
数学表达式对象化
```

例如：

```python
x + y
```

不是普通文本。

而是：

```text
数学表达式对象
```

因此：

可以：

* 化简
* 求导
* 积分
* 求极限
* 求解方程

---

# 4. 定义符号

---

## symbols()

定义数学符号。

```python
from sympy import symbols

x = symbols('x')
```

---

## 定义多个符号

```python
x, y, z = symbols('x y z')
```

---

# 5. 创建表达式

```python
from sympy import *

x = symbols('x')

expr = x**2 + 2*x + 1

print(expr)
```

输出：

```python
x**2 + 2*x + 1
```

---

# 6. simplify()

化简表达式。

```python
from sympy import *

x = symbols('x')

expr = (x**2 - 1)/(x - 1)

print(simplify(expr))
```

结果：

```python
x + 1
```

---

# 7. expand()

展开表达式。

```python
from sympy import *

x = symbols('x')

expr = (x + 1)**3

print(expand(expr))
```

结果：

```python
x**3 + 3*x**2 + 3*x + 1
```

---

# 8. factor()

因式分解。

```python
from sympy import *

x = symbols('x')

expr = x**2 + 2*x + 1

print(factor(expr))
```

结果：

```python
(x + 1)**2
```

---

# 9. subs()

表达式代入。

---

## 单变量代入

```python
from sympy import *

x = symbols('x')

expr = x**2 + 1

print(expr.subs(x, 2))
```

结果：

```python
5
```

---

## 多变量代入

```python
x, y = symbols('x y')

expr = x + y

print(expr.subs({

    x:1,

    y:2
}))
```

结果：

```python
3
```

---

# 10. evalf()

数值计算。

```python
from sympy import *

x = pi

print(x.evalf())
```

结果：

```python
3.141592653...
```

---

## 指定精度

```python
print(pi.evalf(50))
```

---

# 11. solve()

求解方程。

---

## 一元方程

```python
from sympy import *

x = symbols('x')

eq = x**2 - 4

print(solve(eq, x))
```

结果：

```python
[-2, 2]
```

---

## 多元方程组

```python
x, y = symbols('x y')

eq1 = x + y - 3

eq2 = x - y - 1

print(solve(

    (eq1, eq2),

    (x, y)
))
```

结果：

```python
{x:2, y:1}
```

---

# 12. 微分

---

## diff()

求导。

```python
from sympy import *

x = symbols('x')

expr = x**3

print(diff(expr, x))
```

结果：

```python
3*x**2
```

---

## 高阶导数

```python
print(diff(expr, x, 2))
```

结果：

```python
6*x
```

---

# 13. 积分

---

## integrate()

积分。

```python
from sympy import *

x = symbols('x')

expr = x**2

print(integrate(expr, x))
```

结果：

```python
x**3/3
```

---

## 定积分

```python
print(

    integrate(

        expr,

        (x,0,1)
    )
)
```

结果：

```python
1/3
```

---

# 14. 极限

---

## limit()

求极限。

```python
from sympy import *

x = symbols('x')

expr = sin(x)/x

print(limit(expr, x, 0))
```

结果：

```python
1
```

---

# 15. 无穷级数

---

## series()

泰勒展开。

```python
from sympy import *

x = symbols('x')

expr = sin(x)

print(series(expr, x, 0, 6))
```

结果：

```python
x - x**3/6 + x**5/120 + O(x**6)
```

---

# 16. 矩阵

---

## Matrix()

创建矩阵。

```python
from sympy import *

A = Matrix([

    [1,2],

    [3,4]
])

print(A)
```

---

## 矩阵乘法

```python
A = Matrix([

    [1,2],

    [3,4]
])

B = Matrix([

    [5,6],

    [7,8]
])

print(A*B)
```

---

## 行列式

```python
print(A.det())
```

---

## 逆矩阵

```python
print(A.inv())
```

---

# 17. 特征值与特征向量

---

## eigenvals()

特征值。

```python
print(A.eigenvals())
```

---

## eigenvects()

特征向量。

```python
print(A.eigenvects())
```

---

# 18. 微分方程

---

## dsolve()

求解微分方程。

```python
from sympy import *

x = symbols('x')

f = Function('f')

eq = Eq(

    f(x).diff(x),

    f(x)
)

print(dsolve(eq))
```

结果：

```python
Eq(f(x), C1*exp(x))
```

---

# 19. Latex 输出

SymPy 可以直接生成 LaTeX。

---

## latex()

```python
from sympy import *

x = symbols('x')

expr = integrate(

    sin(x),

    x
)

print(latex(expr))
```

结果：

```python
- \\cos{\\left(x \\right)}
```

---

# 20. pretty_print()

美化输出。

```python
from sympy import *

x = symbols('x')

expr = integrate(

    sin(x),

    x
)

pprint(expr)
```

---

# 21. 数学常量

---

## pi

```python
print(pi)
```

---

## E

```python
print(E)
```

---

## oo

无穷大。

```python
print(oo)
```

---

# 22. 常见数学函数

---

## 三角函数

```python
sin(x)

cos(x)

tan(x)
```

---

## 指数函数

```python
exp(x)
```

---

## 对数函数

```python
log(x)
```

---

## 开方

```python
sqrt(x)
```

---

# 23. lambdify()

将 SymPy 表达式转为数值函数。

这是：

```text
SymPy 与 NumPy 的重要桥梁
```

---

## 示例

```python
from sympy import *

x = symbols('x')

expr = x**2 + 1

f = lambdify(

    x,

    expr
)

print(f(3))
```

结果：

```python
10
```

---

# 24. SymPy 与 NumPy 的区别

| 功能     | SymPy    | NumPy    |
| -------- | -------- | -------- |
| 计算类型 | 符号计算 | 数值计算 |
| 精度     | 理论精确 | 浮点近似 |
| 求导     | 支持     | 不支持   |
| 积分     | 支持     | 不支持   |
| 方程求解 | 支持     | 有限支持 |
| 速度     | 较慢     | 很快     |

---

# 25. 常见应用

---

## 数学教学

* 高数
* 线代
* 微积分

---

## 科研计算

* 符号推导
* 理论验证

---

## 控制系统

* 传递函数
* 拉普拉斯变换

---

## 机器人学

* 运动学推导
* 雅可比矩阵

---

# 26. 常见问题

---

## 1. 忘记定义 symbols

错误：

```text
NameError
```

---

## 2. 使用普通 math 库

错误：

```text
TypeError
```

应使用：

```python
sympy.sin()

而不是

math.sin()
```

---

## 3. 符号与数值混淆

SymPy 的：

```text
x
```

不是普通变量。

而是：

```text
数学符号对象
```

---

