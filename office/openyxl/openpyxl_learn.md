# openpyxl 学习笔记

> 目录：[1. 简介](#1-openpyxl-简介) | [2. 安装](#2-安装) | [3. 核心概念](#3-核心概念) | [4. 基本操作](#4-基本操作) | [5. 读取数据](#5-读取数据) | [6. 写入数据](#6-写入数据) | [7. 工作表操作](#7-工作表操作) | [8. 单元格样式](#8-单元格样式) | [9. 公式](#9-公式) | [10. 图表与图片](#10-图表与图片) | [11. 高级功能](#11-高级功能) | [12. 实战案例](#12-实战案例) | [13. 性能模式](#13-性能模式大文件处理) | [14. 常见坑 FAQ](#14-常见坑与-faq)

---

# 1. openpyxl 简介

openpyxl 是 Python 中最常用的：

```text
Excel 读写库
```

主要用于：

* 读写 `.xlsx` / `.xlsm` / `.xltm` 文件（Office 2007+ 格式）
* 操作单元格、行、列、合并单元格
* 设置样式（字体、填充色、边框、对齐）
* 写入公式、生成图表、插入图片
* 数据验证、条件格式、冻结窗格
* 批量生成 / 汇总 Excel 报表

与其他库对比：

```text
openpyxl    : 通用读写，支持样式/图表/公式，最常用
pandas      : 数据分析更快，但样式控制弱（底层也依赖 openpyxl）
xlwings     : 需要操作"已打开的 Excel"或调用 VBA 时使用
xlrd / xlwt : 只支持旧版 .xls 格式，已过时不推荐
```

支持情况：

```text
✅ 支持 : .xlsx  .xlsm  .xltm
❌ 不支持: .xls（旧格式，需要 xlrd）
```

---

# 2. 安装

## 安装 openpyxl

```bash
pip install openpyxl
```

## 测试安装

```python
import openpyxl
print(openpyxl.__version__)   # 例如 3.1.2
```

---

# 3. 核心概念

openpyxl 的对象层级结构（理解这个结构，一切操作就通了）：

```text
Workbook（工作簿 = 一个 .xlsx 文件）
 └── Worksheet（工作表 = 文件底部的 Sheet 标签，可以有很多个）
      └── Cell（单元格 = 具体的一格，如 A1、B2）
           └── Value / Style（单元格的值和样式）
```

三个核心对象：

| 对象 | 类 | 说明 |
|------|----|------|
| 工作簿 | `Workbook` / `load_workbook()` 返回的对象 | 对应一个 Excel 文件 |
| 工作表 | `Worksheet` | 通过 `wb.active`、`wb["表名"]` 获取 |
| 单元格 | `Cell` | 通过 `ws["A1"]`、`ws.cell(row, column)` 获取 |

单元格定位方式：

```text
A1 表示法 : 字母是列（A=第1列），数字是行（1=第1行）
坐标       : ws["A1"]          ← 最直观
行列号     : ws.cell(row=1, column=1)   ← 适合循环
```

---

# 4. 基本操作

## 4.1 创建新工作簿

```python
from openpyxl import Workbook

wb = Workbook()          # 创建空工作簿（自带一个 Sheet）
ws = wb.active           # 获取当前活动的工作表
ws.title = "销售数据"     # 给工作表改名
wb.save("demo.xlsx")     # 保存到文件（必须调用，否则白写！）
```

## 4.2 打开已有文件

```python
from openpyxl import load_workbook

wb = load_workbook("demo.xlsx")              # 打开已有文件
wb = load_workbook("demo.xlsx", data_only=True)  # 取公式的"计算结果值"
```

## 4.3 保存与另存为

```python
wb.save("demo.xlsx")        # 覆盖保存
wb.save("demo_v2.xlsx")     # 另存为（原文件不动）
```

> ⚠️ 注意：如果文件正被 Excel 打开着，`save()` 会报 `PermissionError`，先关闭 Excel 再保存。

---

# 5. 读取数据

## 5.1 读取单元格的值

```python
from openpyxl import load_workbook

wb = load_workbook("demo.xlsx")
ws = wb["销售数据"]

# 三种等价的读取方式
v1 = ws["A1"].value                    # 用 A1 表示法（最直观）
v2 = ws.cell(row=1, column=1).value    # 用行列号（适合循环）
v3 = ws["A1"]["value"]                 # 同上，不常用

print(v1, v2, v3)    # 产品 产品 产品
```

## 5.2 单元格的常用属性

```python
cell = ws["B2"]

print(cell.value)        # 单元格的值
print(cell.row)          # 所在行号（第几行）
print(cell.column)       # 所在列号（数字，如 2）
print(cell.coordinate)   # 坐标字符串，如 "B2"
print(cell.data_type)    # 数据类型（'s'=字符串 'n'=数字 等）
```

## 5.3 遍历数据（最常用！）

```python
# 方式一：iter_rows 按行遍历（推荐）
for row in ws.iter_rows(min_row=1, max_row=4, min_col=1, max_col=3):
    for cell in row:
        print(cell.value, end=" ")
    print()

# 方式二：只要值，不要 Cell 对象（更简洁，推荐）
for row in ws.iter_rows(values_only=True):
    print(row)           # ('产品', '销量', '单价') ...

# 方式三：按列遍历
for col in ws.iter_cols(values_only=True):
    print(col)
```

## 5.4 按行 / 按列整体获取

```python
# 取第 2 行（返回 Cell 元组）
row_cells = ws[2]

# 取 A 列
col_cells = ws["A"]

# 表格的所有行（二维结构）
all_rows = ws.rows
for row in all_rows:
    print([c.value for c in row])
```

## 5.5 获取表格尺寸

```python
print(ws.max_row)       # 最大行号（有内容的最下面一行）
print(ws.max_column)    # 最大列号
print(ws.dimensions)    # 数据范围，如 "A1:C4"
```

## 5.6 空值处理

```python
cell = ws["C10"]
print(cell.value)       # 空单元格的 value 是 None，注意判空

value = ws["C10"].value or 0     # 常用技巧：None 转默认值
```

---

# 6. 写入数据

## 6.1 三种写入方式

```python
ws["A1"] = "姓名"                          # 方式一：直接赋值（直观）
ws.cell(row=2, column=1, value="小明")      # 方式二：cell() 带值写入
ws.cell(row=3, column=1).value = "小红"     # 方式三：先取 cell 再赋值
```

## 6.2 append()：追加一行（推荐！）

`append` 自动写到表格最后一行的下一行，最适合循环写入：

```python
ws.append(["产品", "销量", "单价"])          # 自动追加到下一行
ws.append(["键盘", 120, 199])
ws.append(["鼠标", 200, 89])

# 配合列表批量写入
data = [("显示器", 45, 1299), ("音箱", 30, 399)]
for item in data:
    ws.append(item)
```

## 6.3 插入 / 删除行和列

```python
ws.insert_rows(2)       # 在第 2 行前插入一行
ws.insert_rows(2, 3)    # 在第 2 行前插入 3 行
ws.delete_rows(2)       # 删除第 2 行
ws.delete_rows(2, 5)    # 从第 2 行开始删除 5 行

ws.insert_cols(3)       # 在第 3 列前插入一列
ws.delete_cols(3)       # 删除第 3 列
```

## 6.4 写入注意事项

```text
① 写入的值可以是: str / int / float / bool / datetime
② 数字会自动识别类型: ws["A1"] = 123 → Excel 里是数字
③ 想强制写文本: ws["A1"] = "'123"（前面加单引号，Excel 的惯例）
④ 改完必须 save() 才生效
```

---

# 7. 工作表操作

## 7.1 获取工作表

```python
ws = wb.active              # 当前活动的工作表（打开文件时选中的那个）
ws = wb["销售数据"]          # 按名字获取（最常用）
ws = wb.worksheets[0]       # 按索引获取（第一个）
```

## 7.2 工作簿的 Sheet 信息

```python
print(wb.sheetnames)        # 所有表名列表 ['销售数据', 'Sheet']
print(wb.active)            # 当前活动表
print(len(wb.worksheets))   # 表的数量
```

## 7.3 创建 / 删除 / 复制工作表

```python
# 创建
ws2 = wb.create_sheet("汇总")              # 追加到最后
ws3 = wb.create_sheet("明细", 0)           # 插入到第 0 个位置（最前面）

# 删除
wb.remove(wb["Sheet"])                     # 方式一（推荐）
del wb["Sheet"]                            # 方式二

# 复制
new_ws = wb.copy_worksheet(wb["销售数据"])   # 复制到同一工作簿最后
```

## 7.4 工作表的其他属性

```python
ws.title = "新名字"          # 重命名
ws.sheet_properties.tabColor = "FF0000"   # 标签颜色（红色）
print(ws.max_row, ws.max_column)          # 尺寸
```

---

# 8. 单元格样式

样式相关的类都在 `openpyxl.styles` 里：

```python
from openpyxl.styles import Font, PatternFill, Border, Side, Alignment
```

## 8.1 Font 字体

```python
Font(bold=True)                          # 加粗
Font(size=14, name="微软雅黑")            # 字号 + 字体名
Font(color="FF0000")                     # 红色字（RGB 十六进制）
Font(italic=True, underline="single")    # 斜体 + 下划线

cell.font = Font(bold=True, size=12, color="FFFFFF")
```

## 8.2 PatternFill 填充色（背景色）

```python
PatternFill(start_color="4472C4", end_color="4472C4", fill_type="solid")

# fill_type 常用 "solid"（纯色填充）
cell.fill = PatternFill("solid", start_color="FFD966")   # 黄色背景（简写）
```

## 8.3 Border 边框

```python
thin = Side(style="thin", color="000000")      # 一条细线
double = Side(style="double", color="FF0000")  # 双线

cell.border = Border(
    left=thin, right=thin, top=thin, bottom=thin   # 四个方向分别设置
)
```

`style` 可选值：`thin` 细线 / `medium` 中等 / `thick` 粗线 / `dotted` 点线 / `double` 双线。

## 8.4 Alignment 对齐

```python
Alignment(horizontal="center", vertical="center")   # 水平 + 垂直居中
Alignment(horizontal="center", vertical="center", wrap_text=True)  # 自动换行

cell.alignment = Alignment(horizontal="center", vertical="center")
```

`horizontal`：`left` / `center` / `right`；`vertical`：`top` / `center` / `bottom`。

## 8.5 完整样式示例

```python
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Border, Side, Alignment

wb = Workbook()
ws = wb.active
ws.title = "样式演示"

thin = Side(style="thin", color="000000")
border = Border(left=thin, right=thin, top=thin, bottom=thin)

ws["A1"] = "员工信息表"
ws["A1"].font = Font(bold=True, size=16, color="FFFFFF")
ws["A1"].fill = PatternFill("solid", start_color="4472C4")
ws["A1"].alignment = Alignment(horizontal="center", vertical="center")

ws["A2"] = "张三"
ws["A2"].border = border

wb.save("style_demo.xlsx")
```

## 8.6 行高与列宽

```python
ws.row_dimensions[1].height = 30      # 第 1 行行高 30
ws.column_dimensions["A"].width = 20  # A 列宽 20

# 隐藏行 / 列
ws.row_dimensions[2].hidden = True
ws.column_dimensions["B"].hidden = True
```

> 💡 列宽单位约为"字符数"（8 ≈ Excel 默认宽度），行高单位是磅。

## 8.7 数字格式（number_format）

```python
from datetime import datetime

ws["B2"] = 1234.5678
ws["B2"].number_format = "0.00"          # 保留 2 位小数 → 1234.57
ws["B2"].number_format = "#,##0"         # 千分位 → 1,235
ws["B2"].number_format = "0%"            # 百分比 → 123457%

ws["C2"] = datetime(2024, 6, 1)
ws["C2"].number_format = "yyyy-mm-dd"    # → 2024-06-01
ws["C2"].number_format = "yyyy/mm/dd hh:mm"   # → 2024/06/01 00:00

ws["D2"] = 123
ws["D2"].number_format = "¥#,##0"        # 货币 → ¥123
```

## 8.8 合并单元格

```python
ws.merge_cells("A1:C1")          # 合并 A1~C1（值写在左上角 A1）
ws.merge_cells(start_row=2, start_column=1, end_row=2, end_column=3)  # 行列号写法

ws.unmerge_cells("A1:C1")        # 取消合并
```

合并后只有左上角单元格能赋值：

```python
ws["A1"] = "合并标题"     # ✅ 正确
ws["B1"] = "xx"          # ❌ 报错（B1 已被合并，是 MergedCell 只读）
```

---

# 9. 公式

## 9.1 写入公式

公式就是以 `=` 开头的字符串，openpyxl 原样写入，Excel 打开时计算：

```python
from openpyxl import Workbook

wb = Workbook()
ws = wb.active

ws["A1"] = 10
ws["A2"] = 20
ws["A3"] = "=SUM(A1:A2)"       # 写公式：求和
ws["A4"] = "=AVERAGE(A1:A2)"   # 平均值
ws["A5"] = "=IF(A3>25, \"达标\", \"不达标\")"   # 条件判断
ws["A6"] = "=COUNTIF(A1:A2, \">15\")"          # 条件计数
ws["A7"] = "=VLOOKUP(...)"     # 查找（用法与 Excel 相同）

wb.save("formula.xlsx")
```

常用公式速查：

```text
=SUM(A1:A10)              求和
=AVERAGE(A1:A10)          平均值
=MAX/MIN(A1:A10)          最大 / 最小值
=COUNT(A1:A10)            计数（数字个数）
=COUNTIF(A1:A10, ">5")    条件计数
=SUMIF(A:A, "键盘", B:B)  条件求和
=IF(A1>10, "是", "否")    条件判断
=VLOOKUP(F2, A:B, 2, 0)   纵向查找
=CONCATENATE(A1, B1)      拼接文本（或 A1&B1）
=TODAY()                  今天日期
```

## 9.2 读取公式的计算结果（重要！）

```python
# 情况一：默认模式 → 读到的是"公式字符串"
wb = load_workbook("formula.xlsx")
print(wb.active["A3"].value)      # '=SUM(A1:A2)'（不是结果！）

# 情况二：data_only=True → 读到"缓存的结果值"
wb = load_workbook("formula.xlsx", data_only=True)
print(wb.active["A3"].value)      # 30（前提：Excel 打开保存过一次）
```

> ⚠️ 大坑：`data_only=True` 读到的是 Excel 上次保存时的**缓存值**。
> - 如果文件由 openpyxl 生成且从未用 Excel 打开保存过 → 缓存不存在，读到 `None`！
> - 解决：用 Excel 打开文件保存一次，或用 `formulas` / `pycel` 等库在 Python 里计算公式。

## 9.3 公式中的引用规则

```text
A1        相对引用（复制公式时会跟着变）
$A$1      绝对引用（锁定，复制不变）—— 加 $ 的部分锁定
$A1       列锁定
A$1       行锁定
```

---

# 10. 图表与图片

## 10.1 柱状图 BarChart

```python
from openpyxl import Workbook
from openpyxl.chart import BarChart, Reference

wb = Workbook()
ws = wb.active

# 准备数据
ws.append(["产品", "销量"])
ws.append(["键盘", 120])
ws.append(["鼠标", 200])
ws.append(["显示器", 45])

# 创建柱状图
chart = BarChart()
chart.type = "col"           # col=竖向柱状图, bar=横向条形图
chart.title = "产品销量"
chart.y_axis.title = "销量"
chart.x_axis.title = "产品"

# 引用数据：数据在 B1~B4，分类名在 A2~A4
data = Reference(ws, min_col=2, min_row=1, max_row=4)
cats = Reference(ws, min_col=1, min_row=2, max_row=4)
chart.add_data(data, titles_from_data=True)   # 第一行作为系列名
chart.set_categories(cats)

ws.add_chart(chart, "D2")    # 图表放在 D2 位置
wb.save("chart_demo.xlsx")
```

## 10.2 折线图 LineChart / 饼图 PieChart

```python
from openpyxl.chart import LineChart, PieChart, Reference

line = LineChart()           # 用法与 BarChart 相同
line.title = "月度趋势"

pie = PieChart()             # 饼图
pie.title = "占比分布"

# 同样用 Reference 引用数据后 add_data + set_categories
```

其他图表：`ScatterChart` 散点图、`AreaChart` 面积图、`RadarChart` 雷达图。

## 10.3 插入图片

```python
from openpyxl.drawing.image import Image

img = Image("photo.png")     # 本地图片（依赖 Pillow 库处理格式）
img.width = 400              # 宽（像素）
img.height = 300             # 高（像素）
ws.add_image(img, "A5")      # 放到 A5 位置

wb.save("with_image.xlsx")
```

> 💡 插入 PNG/JPG 需要 `pip install pillow`。

---

# 11. 高级功能

## 11.1 冻结窗格（固定首行 / 首列）

```python
ws.freeze_panes = "A2"       # 冻结第 1 行（滚动时表头不动）
ws.freeze_panes = "B1"       # 冻结 A 列
ws.freeze_panes = "B2"       # 同时冻结第 1 行和 A 列
ws.freeze_panes = None       # 取消冻结
```

记忆：冻结线在**指定单元格的上方和左侧**。

## 11.2 自动筛选

```python
ws.auto_filter.ref = "A1:C10"    # 给 A1~C10 加筛选按钮
ws.auto_filter.ref = ws.dimensions   # 对整个数据区加筛选
```

## 11.3 数据验证（下拉列表）

```python
from openpyxl.worksheet.datavalidation import DataValidation

# 创建下拉列表验证
dv = DataValidation(type="list", formula1='"是,否"', allow_blank=True)
dv.error = "只能输入 是 或 否"
dv.errorTitle = "输入错误"
ws.add_data_validation(dv)

dv.add("C2:C100")            # 应用到 C2~C100（单元格里出现下拉箭头）
```

其他验证类型：`whole` 整数、`decimal` 小数、`date` 日期、`length` 文本长度。

## 11.4 条件格式

```python
from openpyxl.formatting.rule import CellIsRule, ColorScaleRule

# 数值大于 100 时标红背景
red_fill = PatternFill("solid", start_color="FFC7CE")
ws.conditional_formatting.add(
    "B2:B100",
    CellIsRule(operator="greaterThan", formula=["100"], fill=red_fill)
)

# 颜色渐变（数值越大越绿）
ws.conditional_formatting.add(
    "B2:B100",
    ColorScaleRule(
        start_type="min", start_color="FFFFFF",
        end_type="max", end_color="63BE7B",
    )
)
```

## 11.5 保护工作表

```python
ws.protection.sheet = True                  # 开启保护
ws.protection.password = "123456"           # 设密码
ws.protection.sheet = False                 # 取消保护
```

---

# 12. 实战案例

## 案例 1：生成带样式的销售数据表

（即项目里的 `openpyxl_learn.py`，完整代码）

```python
from openpyxl import Workbook, load_workbook
from openpyxl.styles import Font, PatternFill

# ===== 写 Excel =====
wb = Workbook()
ws = wb.active
ws.title = "销售数据"

# 表头：加粗白字 + 蓝色背景
header_font = Font(bold=True, color="FFFFFF")
header_fill = PatternFill(start_color="4472C4", end_color="4472C4", fill_type="solid")

for col, title in enumerate(["产品", "销量", "单价"], start=1):
    cell = ws.cell(row=1, column=col, value=title)
    cell.font = header_font
    cell.fill = header_fill

# 写数据
data = [("键盘", 120, 199), ("鼠标", 200, 89), ("显示器", 45, 1299)]
for row, item in enumerate(data, start=2):
    for col, value in enumerate(item, start=1):
        ws.cell(row=row, column=col, value=value)

wb.save("sales.xlsx")

# ===== 读 Excel =====
wb = load_workbook("sales.xlsx", data_only=True)
ws = wb["销售数据"]
for row in ws.iter_rows(min_row=2, values_only=True):
    print(row)          # ('键盘', 120, 199) ...
```

## 案例 2：汇总多个 Excel 文件

场景：目录下有 `1月.xlsx`、`2月.xlsx`……把数据汇总到一个文件：

```python
from pathlib import Path
from openpyxl import Workbook, load_workbook

summary = Workbook()
summary_ws = summary.active
summary_ws.title = "汇总"
summary_ws.append(["月份", "产品", "销量", "单价"])    # 总表头

for file in Path(".").glob("*月.xlsx"):
    month = file.stem                    # 文件名，如 "1月"
    wb = load_workbook(file, data_only=True)
    ws = wb.active
    for row in ws.iter_rows(min_row=2, values_only=True):   # 跳过表头
        summary_ws.append([month, *row])                    # 前面加上月份

summary.save("汇总.xlsx")
```

## 案例 3：给已有表格补样式（边框 + 居中 + 列宽）

```python
from openpyxl import load_workbook
from openpyxl.styles import Border, Side, Alignment

wb = load_workbook("sales.xlsx")
ws = wb.active

thin = Side(style="thin")
border = Border(left=thin, right=thin, top=thin, bottom=thin)
center = Alignment(horizontal="center", vertical="center")

for row in ws.iter_rows(min_row=1, max_row=ws.max_row, max_col=ws.max_column):
    for cell in row:
        cell.border = border
        cell.alignment = center

for col in ["A", "B", "C"]:
    ws.column_dimensions[col].width = 15

wb.save("sales_美化.xlsx")
```

---

# 13. 性能模式（大文件处理）

普通模式会把整个文件读进内存，几十万行的大文件要用专用模式：

## 13.1 read_only：只读模式（省内存）

```python
from openpyxl import load_workbook

wb = load_workbook("big.xlsx", read_only=True)   # 只读，内存占用极小
ws = wb.active

for row in ws.iter_rows(values_only=True):       # 流式逐行读取
    print(row)

wb.close()       # read_only 模式必须手动 close()！
```

限制：不能写入、不能取 `ws["A1"]`（只能迭代）、`max_row` 可能为 None。

## 13.2 write_only：只写模式（速度快）

```python
from openpyxl import Workbook

wb = Workbook(write_only=True)      # 只写模式（没有 active 工作表）
ws = wb.create_sheet()              # 必须手动建 sheet

ws.append(["姓名", "年龄"])          # 只能用 append，不能随机访问
ws.append(["小明", 18])

wb.save("big_write.xlsx")
```

限制：只能 `append`、不能读、不能回头改已写的单元格。

## 13.3 三种模式对比

| 模式 | 参数 | 适用场景 | 内存 |
|------|------|----------|------|
| 普通模式 | 默认 | 读写小文件（<几万行） | 全部加载 |
| 只读模式 | `read_only=True` | 读大文件 | 极小（流式） |
| 只写模式 | `write_only=True` | 生成大文件 | 极小（流式） |

---

# 14. 常见坑与 FAQ

**Q1：`data_only=True` 读公式结果是 None？**

```text
原因: openpyxl 生成的新文件没有公式缓存值
解决: 用 Excel 打开该文件保存一次，之后 data_only 才能读到结果
```

**Q2：保存时报 PermissionError？**

```text
原因: 文件正被 Excel 打开着（Excel 会锁文件）
解决: 先关闭 Excel 再运行脚本
```

**Q3：能读写 .xls 吗？**

```text
不能。openpyxl 只支持 .xlsx/.xlsm/.xltm
旧格式需要 xlrd（读），且新版 xlrd 已不支持 .xls 以外的格式
推荐: 先用 Excel/WPS 把 .xls 另存为 .xlsx
```

**Q4：读到的日期是 datetime 对象 / 数字？**

```text
Excel 内部日期是数字，openpyxl 会转成 datetime.datetime
格式化输出: value.strftime("%Y-%m-%d")
注意: 表格里写成文本的日期不会自动转换
```

**Q5：删除行后样式错乱？**

```text
openpyxl 的 insert/delete 不自动搬移样式和合并单元格
解决: 复杂表格尽量"新建再写"，而不是在复杂表上删改
```

**Q6：合并单元格除了左上角都不能赋值？**

```text
合并后其余格子是 MergedCell（只读），赋值报 AttributeError
只有左上角（如 A1）能写值
```

**Q7：单元格取到的值有空格 / 换行？**

```text
cell.value 原样返回 Excel 里的内容（含前后空格）
处理: str(cell.value).strip() 后再使用，并注意 None 判空
```

---