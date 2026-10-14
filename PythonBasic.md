# 1. Python 简介

Python 是当前最常用的：

```text
通用高级编程语言
```

由 Guido van Rossum 于 1991 年发布，主要用于：

* 脚本编写
* 数据分析
* 人工智能
* Web 开发
* 自动化运维
* 科学计算

与其他语言对比：

```text
C/C++  ：编译型，性能高，语法复杂
Java   ：编译型，跨平台，冗长
Python ：解释型，语法简洁，生态丰富
```

例如：

C：

```c
#include <stdio.h>
int main() {
    printf("Hello\n");
    return 0;
}
```

Python：

```python
print("Hello")
```

---

# 2. 安装与运行

## 2.1 安装 Python

### Windows

```text
访问 https://www.python.org/downloads/
下载安装包，勾选 "Add Python to PATH"
```

### macOS

```bash
brew install python
```

### Linux

```bash
sudo apt install python3   # Ubuntu/Debian
```

---

## 2.2 验证安装

```bash
python --version
python3 --version
```

输出：

```text
Python 3.12.0
```

---

## 2.3 运行 Python 的三种方式

### 交互式解释器

```bash
python
```

```python
>>> print("Hello")
Hello
```

### 脚本文件

创建 `hello.py`：

```python
print("Hello, World!")
```

运行：

```bash
python hello.py
```

### IDE / 编辑器

```text
• VS Code
• PyCharm
• Jupyter Notebook
• IDLE（自带）
```

---

# 3. 变量与数据类型

## 3.1 变量

Python 是动态类型语言，变量无需声明类型。

```python
x = 10          # 整数
y = 3.14        # 浮点数
name = "Alice"  # 字符串
flag = True     # 布尔值
```

变量命名规则：

```text
• 只能包含字母、数字、下划线
• 不能以数字开头
• 区分大小写
• 不能使用关键字（如 if、for、class）
```

---

## 3.2 基本数据类型

| 类型     | 说明   | 示例                     |
| -------- | ------ | ------------------------ |
| int      | 整数   | `10`, `-3`, `0`    |
| float    | 浮点数 | `3.14`, `-0.5`       |
| str      | 字符串 | `"hello"`, `'world'` |
| bool     | 布尔值 | `True`, `False`      |
| NoneType | 空值   | `None`                 |

---

## 3.3 查看类型

```python
x = 10
print(type(x))   # <class 'int'>
```

---

## 3.4 类型转换

```python
int("123")       # 123
float("3.14")    # 3.14
str(100)         # "100"
bool(0)          # False
bool(1)          # True
```

---

# 4. 运算符

## 4.1 算术运算符

```python
a = 10
b = 3

print(a + b)    # 13  加
print(a - b)    # 7   减
print(a * b)    # 30  乘
print(a / b)    # 3.333...  除
print(a // b)   # 3   整除
print(a % b)    # 1   取余
print(a ** b)   # 1000  幂
```

---

## 4.2 比较运算符

```python
print(3 > 2)     # True
print(3 < 2)     # False
print(3 == 3)    # True
print(3 != 2)    # True
print(3 >= 3)    # True
print(3 <= 2)    # False
```

---

## 4.3 逻辑运算符

```python
print(True and False)   # False
print(True or False)    # True
print(not True)         # False
```

---

## 4.4 赋值运算符

```python
x = 10
x += 5   # x = x + 5  → 15
x -= 3   # x = x - 3  → 12
x *= 2   # x = x * 2  → 24
x /= 4   # x = x / 4  → 6.0
```

---

# 5. 字符串

## 5.1 定义字符串

```python
s1 = "hello"
s2 = 'world'
s3 = """多行
字符串"""
```

---

## 5.2 字符串操作

```python
s = "Hello"

print(len(s))           # 5  长度
print(s.upper())        # HELLO
print(s.lower())        # hello
print(s[0])             # H  索引
print(s[1:3])           # el  切片
print(s + " World")     # Hello World  拼接
print(s * 3)            # HelloHelloHello  重复
```

---

## 5.3 格式化字符串（f-string）

```python
name = "Alice"
age = 20

print(f"我是 {name}，今年 {age} 岁")
```

输出：

```text
我是 Alice，今年 20 岁
```

---

## 5.4 常用字符串方法

```python
s = "hello world"

s.split()            # ['hello', 'world']
s.replace("world", "python")  # "hello python"
s.find("world")      # 6
s.startswith("hello") # True
s.strip()            # 去除两端空白
s.join(["a", "b"])   # 用 s 连接列表
```

---

# 6. 列表、元组、字典、集合

## 6.1 列表（list）

可变有序序列。

```python
lst = [1, 2, 3, 4]

lst.append(5)        # 添加元素 → [1,2,3,4,5]
lst.insert(0, 0)     # 指定位置插入 → [0,1,2,3,4,5]
lst.remove(3)        # 删除元素
lst.pop()            # 删除最后一个
print(lst[0])        # 索引
print(lst[1:3])      # 切片
print(len(lst))      # 长度
```

---

## 6.2 元组（tuple）

不可变有序序列。

```python
tup = (1, 2, 3)

print(tup[0])        # 1
# tup[0] = 10        # 错误：元组不可修改
```

---

## 6.3 字典（dict）

键值对集合。

```python
person = {"name": "Alice", "age": 20}

print(person["name"])       # Alice
person["age"] = 21          # 修改
person["city"] = "Beijing"  # 新增
del person["city"]          # 删除

print(person.keys())        # 所有键
print(person.values())      # 所有值
print(person.items())       # 所有键值对
```

---

## 6.4 集合（set）

无序不重复集合。

```python
s = {1, 2, 3, 3}
print(s)              # {1, 2, 3}

s.add(4)
s.remove(1)
print(s)              # {2, 3, 4}
```

---

# 7. 条件语句

## 7.1 if / elif / else

```python
score = 85

if score >= 90:
    print("优秀")
elif score >= 60:
    print("及格")
else:
    print("不及格")
```

---

## 7.2 单行 if

```python
x = 10
result = "大" if x > 5 else "小"
print(result)   # 大
```

---

## 7.3 逻辑组合

```python
age = 20
if age >= 18 and age < 60:
    print("成年人")
```

---

# 8. 循环

## 8.1 for 循环

```python
for i in range(5):
    print(i)
```

输出：

```text
0
1
2
3
4
```

---

## 8.2 遍历列表

```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
```

---

## 8.3 遍历字典

```python
person = {"name": "Alice", "age": 20}

for key, value in person.items():
    print(key, value)
```

---

## 8.4 while 循环

```python
i = 0
while i < 5:
    print(i)
    i += 1
```

---

## 8.5 break 与 continue

```python
for i in range(10):
    if i == 5:
        break        # 跳出循环
    if i % 2 == 0:
        continue     # 跳过本次
    print(i)
```

---

## 8.6 range() 用法

```python
range(5)         # 0,1,2,3,4
range(1, 5)      # 1,2,3,4
range(0, 10, 2)  # 0,2,4,6,8
```

---

# 9. 函数

## 9.1 定义函数

```python
def greet():
    print("Hello")

greet()   # 调用
```

---

## 9.2 带参数的函数

```python
def greet(name):
    print(f"Hello, {name}")

greet("Alice")
```

---

## 9.3 带返回值的函数

```python
def add(a, b):
    return a + b

result = add(3, 5)
print(result)   # 8
```

---

## 9.4 默认参数

```python
def greet(name="World"):
    print(f"Hello, {name}")

greet()          # Hello, World
greet("Alice")   # Hello, Alice
```

---

## 9.5 关键字参数

```python
def introduce(name, age):
    print(f"{name} is {age}")

introduce(age=20, name="Alice")
```

---

## 9.6 可变参数

```python
# *args：任意数量的位置参数（元组）
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3))   # 6
```

```python
# **kwargs：任意数量的关键字参数（字典）
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

print_info(name="Alice", age=20)
```

---

## 9.7 多返回值

```python
def get_min_max(lst):
    return min(lst), max(lst)

low, high = get_min_max([3, 1, 4, 1, 5])
print(low, high)   # 1 5
```

---

## 9.8 匿名函数 lambda

```python
square = lambda x: x ** 2
print(square(5))   # 25
```

常用场景：

```python
nums = [3, 1, 4, 1, 5]
sorted_nums = sorted(nums, key=lambda x: -x)
print(sorted_nums)   # [5, 4, 3, 1, 1]
```

---

## 9.9 函数文档字符串

```python
def add(a, b):
    """返回两个数的和"""
    return a + b

print(add.__doc__)   # 返回两个数的和
help(add)
```

---

# 10. 模块与 import

## 10.1 什么是模块

```text
模块 = 一个 .py 文件
包   = 包含多个模块的目录（含 __init__.py）
```

---

## 10.2 导入模块

```python
import math

print(math.sqrt(16))   # 4.0
print(math.pi)         # 3.141592653589793
```

---

## 10.3 导入特定成员

```python
from math import sqrt, pi

print(sqrt(16))   # 4.0
print(pi)         # 3.141592653589793
```

---

## 10.4 给模块起别名

```python
import numpy as np
import pandas as pd

arr = np.array([1, 2, 3])
```

---

## 10.5 导入所有成员（不推荐）

```python
from math import *

print(sqrt(16))
```

---

## 10.6 自定义模块

创建 `mymodule.py`：

```python
def hello():
    print("Hello from module")

PI = 3.14159
```

在另一个文件中：

```python
import mymodule

mymodule.hello()
print(mymodule.PI)
```

---

## 10.7 主程序判断

```python
# mymodule.py
def main():
    print("主程序执行")

if __name__ == "__main__":
    main()
```

说明：

```text
__name__ == "__main__" 时表示直接运行该文件
被 import 时不会执行 main()
```

---

## 10.8 常用标准库模块

| 模块        | 用途         |
| ----------- | ------------ |
| math        | 数学函数     |
| random      | 随机数       |
| datetime    | 日期时间     |
| os          | 操作系统接口 |
| sys         | 系统参数     |
| json        | JSON 解析    |
| re          | 正则表达式   |
| time        | 时间         |
| collections | 高级数据结构 |

示例：

```python
import random
print(random.randint(1, 10))   # 1~10 随机整数

import datetime
print(datetime.datetime.now())

import json
data = json.loads('{"name": "Alice"}')
print(data["name"])
```

---

# 11. 异常处理

## 11.1 try / except

```python
try:
    x = 10 / 0
except ZeroDivisionError:
    print("除数不能为零")
```

---

## 11.2 捕获多种异常

```python
try:
    x = int("abc")
except (ValueError, TypeError) as e:
    print(f"错误：{e}")
```

---

## 11.3 try / except / else / finally

```python
try:
    x = 10 / 2
except ZeroDivisionError:
    print("错误")
else:
    print("成功")        # 无异常时执行
finally:
    print("总是执行")    # 无论是否有异常
```

---

## 11.4 主动抛出异常

```python
def check_age(age):
    if age < 0:
        raise ValueError("年龄不能为负数")
    return age
```

---

# 12. 文件操作

## 12.1 读取文件

```python
with open("data.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)
```

---

## 12.2 逐行读取

```python
with open("data.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())
```

---

## 12.3 写入文件

```python
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("Hello\n")
    f.write("World\n")
```

---

## 12.4 追加内容

```python
with open("output.txt", "a", encoding="utf-8") as f:
    f.write("追加内容\n")
```

---

## 12.5 文件模式

| 模式 | 说明                    |
| ---- | ----------------------- |
| r    | 只读（默认）            |
| w    | 写入（覆盖）            |
| a    | 追加                    |
| r+   | 读写                    |
| b    | 二进制模式（如 rb、wb） |

---

# 13. 类与对象

## 13.1 定义类

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"我是 {self.name}，今年 {self.age} 岁")

p = Person("Alice", 20)
p.greet()
```

---

## 13.2 属性与方法

```python
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

c = Circle(5)
print(c.area())   # 78.5
```

---

## 13.3 继承

```python
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Woof")

d = Dog()
d.speak()   # Woof
```

---

## 13.4 特殊方法

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

p1 = Point(1, 2)
p2 = Point(3, 4)
print(p1 + p2)   # (4, 6)
```

---

# 14. 常用内置函数

| 函数                  | 说明      |
| --------------------- | --------- |
| print()               | 输出      |
| input()               | 输入      |
| len()                 | 长度      |
| type()                | 类型      |
| int(), float(), str() | 类型转换  |
| range()               | 生成序列  |
| sum()                 | 求和      |
| min(), max()          | 最小/最大 |
| sorted()              | 排序      |
| enumerate()           | 索引+元素 |
| zip()                 | 并行遍历  |
| map()                 | 映射      |
| filter()              | 过滤      |
| abs()                 | 绝对值    |
| round()               | 四舍五入  |

示例：

```python
nums = [3, 1, 4, 1, 5]

print(sorted(nums))            # [1, 1, 3, 4, 5]
print(sum(nums))               # 14

for i, n in enumerate(nums):
    print(i, n)

squares = list(map(lambda x: x**2, nums))
print(squares)                 # [9, 1, 16, 1, 25]

evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)                   # [4]
```

---

# 15. 列表推导式

```python
# 基本形式
squares = [x**2 for x in range(5)]
print(squares)   # [0, 1, 4, 9, 16]

# 带条件
evens = [x for x in range(10) if x % 2 == 0]
print(evens)   # [0, 2, 4, 6, 8]

# 嵌套
matrix = [[i*j for j in range(3)] for i in range(3)]
print(matrix)   # [[0,0,0],[0,1,2],[0,2,4]]
```

字典推导式：

```python
squares = {x: x**2 for x in range(5)}
print(squares)   # {0:0, 1:1, 2:4, 3:9, 4:16}
```

---

# 16. 常见问题

## 1. IndentationError（缩进错误）

```text
Python 使用缩进表示代码块
统一使用 4 个空格，不要混用 Tab 和空格
```

---

## 2. NameError（名称未定义）

```python
print(x)   # NameError: name 'x' is not defined
```

原因：变量未定义或拼写错误。

---

## 3. TypeError（类型错误）

```python
print("abc" + 123)   # TypeError
```

解决：

```python
print("abc" + str(123))
```

---

## 4. 中文乱码

```python
with open("file.txt", "r", encoding="utf-8") as f:
    content = f.read()
```

---

## 5. 变量作用域

```python
x = 10

def func():
    global x
    x = 20

func()
print(x)   # 20
```

---


# 17. 核心语法速查

```python
# 变量
x = 10

# 字符串
s = "hello"
print(f"{s} world")

# 列表
lst = [1, 2, 3]
lst.append(4)

# 字典
d = {"a": 1}
print(d["a"])

# 条件
if x > 5:
    print("big")
else:
    print("small")

# 循环
for i in range(5):
    print(i)

# 函数
def add(a, b):
    return a + b

# 导入
import math
from math import sqrt

# 类
class Person:
    def __init__(self, name):
        self.name = name

# 异常
try:
    x = 1 / 0
except ZeroDivisionError:
    print("error")

# 文件
with open("file.txt", "r") as f:
    content = f.read()
```
