#这个文件里可以复制sympy_learn.md里的代码，运行观察效果
from sympy import *

x = symbols('x')

expr = sin(x)

print(series(expr, x, 0, 6))