# 泰勒展开，麦克劳林形式（展开点为0）
from sympy import *
from math import e

# 泰勒展开，麦克劳林形式（展开点为0）
# expr: 要展开的表达式
# order: 展开阶数
# style: 返回形式，'expr'返回表达式，'num'返回数值
# num: 当style为'num'时，指定x的取值
def taylor_expansion(expr,order,style,num=None):
    result = 0
    x = symbols('x')
    for i in range(order):
        result += diff(expr,x,i).subs(x,0) * x**i / factorial(i)
    if style == 'expr':
        return result
    elif style == 'num':
        return result.subs(x,num)

if __name__ == '__main__':
    x = symbols('x')
    expr = exp(x)
    a = taylor_expansion(expr,20,'expr')
    b = taylor_expansion(expr,20,'num',3)
    print(a)#泰勒展开表达式
    print(b.evalf(17))#泰勒展开计算值，保留17位小数
    print(e**3)#真实值
