# PyAutoGUI 学习笔记

---

# 1. PyAutoGUI 简介

PyAutoGUI 是 Python 中最常用的 GUI 自动化库之一。

它可以模拟：

* 鼠标操作
* 键盘输入
* 屏幕截图
* 图像识别

从而实现：

* 自动办公
* GUI 测试
* 自动点击
* 游戏脚本
* 自动化操作

本质上：

PyAutoGUI 是通过模拟“人”对电脑的操作来实现自动化。

---

# 2. 安装

## 安装库

```bash
pip install pyautogui
```

---

## 测试安装

```python
import pyautogui

print(pyautogui.position())
```

如果没有报错：

说明安装成功。

---

# 3. PyAutoGUI 工作原理

PyAutoGUI 的核心逻辑：

```text
移动鼠标
↓
点击按钮
↓
输入文本
↓
执行快捷键
```

也就是说：

它本质上是：

```text
屏幕级自动化
```

而不是：

```text
软件内部 API 控制
```

因此：

PyAutoGUI 会受到：

* 分辨率
* 窗口位置
* 屏幕遮挡

影响。

---

# 4. 坐标系统

PyAutoGUI 的所有鼠标操作都基于：

```text
屏幕坐标
```

---

## 坐标原点

屏幕左上角：

```text
(0,0)
```

---

## 坐标方向

```text
向右：x 增加
向下：y 增加
```

例如：

```text
1920×1080 显示器：

左上角：
(0,0)

右下角：
(1919,1079)
```

---

# 5. 获取鼠标坐标

## position()

获取当前鼠标坐标。

```python
import pyautogui

pos = pyautogui.position()

print(pos)
```

返回：

```python
Point(x=500, y=300)
```

---

## 实时显示鼠标坐标

```python
import pyautogui
import time

while True:

    print(pyautogui.position())

    time.sleep(0.1)
```

用途：

* 获取按钮位置
* GUI 自动化开发
* 游戏脚本开发

---

# 6. 获取屏幕分辨率

## size()

获取屏幕大小。

```python
import pyautogui

size = pyautogui.size()

print(size)
```

返回：

```python
Size(width=1920, height=1080)
```

---

# 7. 鼠标控制

鼠标控制是 PyAutoGUI 最核心的功能之一。

---

## moveTo()

移动鼠标到指定坐标。

```python
pyautogui.moveTo(
    500,
    300
)
```

---

### 平滑移动

```python
pyautogui.moveTo(
    500,
    300,

    duration=1
)
```

鼠标会在 1 秒内平滑移动。

---

## moveRel()

相对当前位置移动。

```python
pyautogui.moveRel(
    100,
    0
)
```

含义：

```text
向右移动100像素
```

---

## click()

鼠标点击。

```python
pyautogui.click()
```

---

### 点击指定坐标

```python
pyautogui.click(
    500,
    300
)
```

---

### 指定按键

```python
pyautogui.click(
    button='right'#鼠标右键点击
)
```

常见值：

```python
鼠标左键：'left'
鼠标右键：'right'
鼠标中键：'middle'
```

---

### 多次点击

```python
pyautogui.click(
    clicks=2
)
```

---

## doubleClick()

双击。

```python
pyautogui.doubleClick()
```

---

## tripleClick()

三击。

```python
pyautogui.tripleClick()
```

---

## mouseDown()

按下鼠标但不松开。

```python
pyautogui.mouseDown()
```

---

## mouseUp()

释放鼠标。

```python
pyautogui.mouseUp()
```

---

## dragTo()

拖动鼠标到指定位置。

```python
pyautogui.dragTo(
    700,
    400,

    duration=1
)
```

内部逻辑：

```text
按下鼠标
↓
移动鼠标
↓
松开鼠标
```

---

## dragRel()

相对拖动。

```python
pyautogui.dragRel(
    100,
    0
)
```

---

## scroll()

滚动滚轮。

```python
pyautogui.scroll(500)
```

正数：

向上滚动

负数：

向下滚动

---

# 8. 键盘控制

PyAutoGUI 可以模拟键盘输入。

---

## write()

自动输入字符串。

```python
pyautogui.write(
    'Hello'
)
```

---

### 设置输入间隔

```python
pyautogui.write(
    'Hello',

    interval=0.1
)
```

作用：

模拟真实输入。

---

## press()

按下指定按键。

```python
pyautogui.press('enter')
```

---

### 连续按键

```python
pyautogui.press(
    'tab',

    presses=3
)
```

---

## keyDown()

按下按键但不松开。

```python
pyautogui.keyDown('shift')
```

---

## keyUp()

释放按键。

```python
pyautogui.keyUp('shift')
```

---

## hotkey()

执行组合快捷键。

```python
pyautogui.hotkey(
    'ctrl',
    's'
)
```

执行逻辑：

```text
按下 ctrl
↓
按下 s
↓
释放 s
↓
释放 ctrl
```

---

# 9. 常见按键名称

```python
'enter'
'tab'
'shift'
'ctrl'
'alt'
'esc'
'space'
'up'
'down'
'left'
'right'
'backspace'
'delete'
'f1'
'f2'
'f3'
```

完整列表：

```python
print(pyautogui.KEYBOARD_KEYS)
```

---

# 10. 截图功能

PyAutoGUI 支持屏幕截图。

---

## screenshot()

全屏截图。

```python
image = pyautogui.screenshot()
```

---

## 保存截图

```python
image.save('screen.png')
```

---

## 区域截图

```python
image = pyautogui.screenshot(

    region=(0,0,500,500)
)
```

参数：

```text
(x,y,width,height)
```

---

# 11. 图像识别

PyAutoGUI 可以查找屏幕中的图片。

这是 GUI 自动化的重要功能。

---

## locateOnScreen()

查找图片。

```python
button = pyautogui.locateOnScreen(
    'button.png'
)
```

返回：

```python
Box(left, top, width, height)
```

---

## center()

获取图片中心坐标。

```python
center = pyautogui.center(button)
```

---

## 自动点击图片

```python
button = pyautogui.locateOnScreen(
    'button.png'
)

center = pyautogui.center(button)

pyautogui.click(center)
```

---

# 12. 像素颜色检测

## pixel()

获取指定位置像素颜色。

```python
color = pyautogui.pixel(
    500,
    300
)
```

返回：

```python
RGB(red=255, green=255, blue=255)
```

---

## pixelMatchesColor()

检测颜色是否匹配。

```python
pyautogui.pixelMatchesColor(
    500,
    300,

    (255,255,255)
)
```

用途：

* 游戏脚本
* 状态检测
* 自动点击判断

---

# 13. 消息框

PyAutoGUI 提供简单 GUI 对话框。

---

## alert()

提示框。

```python
pyautogui.alert(
    'Hello'
)
```

---

## confirm()

确认框。

```python
result = pyautogui.confirm(
    'Continue?'
)
```

---

## prompt()

输入框。

```python
text = pyautogui.prompt(
    'Input text'
)
```

---

## password()

密码输入框。

```python
pwd = pyautogui.password(
    'Password'
)
```

---

# 14. FailSafe 安全机制

PyAutoGUI 默认启用安全保护。

---

## 原理

当鼠标移动到：

```text
左上角 (0,0)
```

时：

程序立即停止。

防止：

* 无限循环
* 鼠标失控

---

## 异常

```python
pyautogui.FailSafeException
```

---

## 关闭 FailSafe

```python
pyautogui.FAILSAFE = False
```

不建议关闭。

---

# 15. 自动化常见结构

PyAutoGUI 自动化通常：

```text
获取坐标
↓
移动鼠标
↓
点击
↓
输入文本
↓
等待
↓
继续流程
```

---

# 16. time.sleep()

自动化中经常使用：

```python
time.sleep()
```

作用：

暂停程序。

因为：

GUI 需要响应时间。

例如：

```python
import time

time.sleep(1)
```

---

# 17. 常见问题

## 1. 坐标错误

原因：

* 分辨率变化
* 窗口位置变化

---

## 2. DPI 缩放问题

Windows 缩放可能导致：

```text
坐标不一致
```

建议：

```text
使用 100% 缩放
```

---

## 3. 多显示器问题

多显示器：

可能存在：

```text
负坐标
```

---

## 4. 程序运行过快

GUI 来不及响应。

解决：

```python
time.sleep()
```

---

# 18. 常见自动化案例

## 自动办公

* 自动填表
* 自动复制粘贴
* 自动 Excel 操作

---

## GUI 测试

* 自动点击按钮
* 自动测试界面

---

## 游戏脚本

* 自动点击
* 自动挂机

---

## 数据录入

* 自动输入
* 自动提交

---

# 19. PyAutoGUI 的局限性

PyAutoGUI 本质：

```text
屏幕自动化
```

因此：

* 不读取软件内部数据
* 不是真正 API 控制

所以容易受到：

* 分辨率
* 窗口变化
* 屏幕遮挡

影响。

---

# 20. 推荐学习路线

建议顺序：

```text
坐标系统
↓
鼠标控制
↓
键盘控制
↓
截图
↓
图像识别
↓
自动化流程
↓
综合项目
```

---

# 21. 推荐练习项目

## 初级

* 自动点击器
* 自动输入脚本

---

## 中级

* 自动打开软件
* 自动签到
* 自动填表

---

## 高级

* GUI 自动测试
* 游戏自动化
* 图像识别自动化
* 自动办公系统
