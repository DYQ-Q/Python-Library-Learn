# pySerial 学习笔记

---

# 1. pySerial 简介

pySerial 是 Python 中最常用的串口通信库。

主要用于：

* 单片机通信
* Arduino 通信
* STM32 通信
* ESP32 通信
* 上位机开发
* 串口调试
* 数据采集

本质上：

pySerial 用于：

```text id="oz0imk"
Python 与串口设备之间的数据通信
```

---

# 2. 串口通信基础

在学习 pySerial 前，需要先理解串口通信。

---

# 3. 什么是串口

串口（Serial Port）：

是一种：

```text id="jjdrtc"
按位顺序传输数据
```

的通信方式。

数据传输形式：

```text id="lf6mlh"
1 bit
↓
1 bit
↓
1 bit
```

因此叫：

```text id="m5mkhw"
串行通信
```

---

# 4. 常见串口设备

常见串口设备：

* Arduino
* STM32
* ESP32
* USB转TTL
* GPS模块
* 蓝牙模块
* 激光雷达
* 工业设备

---

# 5. 串口通信参数

串口通信双方必须：

```text id="u9j2rk"
参数一致
```

否则无法正常通信。

---

## 波特率 baudrate

表示：

```text id="p7x50y"
每秒传输多少 bit
```

常见值：

```python id="4jbrut"
9600
115200
256000
921600
```

波特率越高：

速度越快。

但：

稳定性可能下降。

---

## 数据位 bytesize

表示：

```text id="85v8n3"
一个数据包含多少 bit
```

通常：

```python id="3e7uvl"
8 bit
```

最常见。

---

## 停止位 stopbits

表示：

```text id="b5w97w"
一个数据结束标志
```

常见值：

```python id="24g5v6"
1
1.5
2
```

---

## 校验位 parity

用于：

```text id="g5v0a0"
数据校验
```

常见值：

| 值 | 含义  |
| - | --- |
| N | 无校验 |
| E | 偶校验 |
| O | 奇校验 |

通常：

```text id="mfnto2"
N
```

最常见。

---

# 6. 安装 pySerial

## 安装

```bash id="m0e8ka"
pip install pyserial
```

---

## 测试安装

```python id="jlwmqm"
import serial

print(serial.__version__)
```

---

# 7. 串口号

不同系统：

串口名称不同。

---

## Windows

```text id="h8hf14"
COM1
COM2
COM3
```

---

## Linux

```text id="j4p8jw"
/dev/ttyUSB0
/dev/ttyACM0
```

---

## macOS

```text id="wygg3v"
/dev/cu.usbserial
```

---

# 8. 查看串口

## 获取所有串口

```python id="tl8gnb"
import serial.tools.list_ports

ports = serial.tools.list_ports.comports()

for port in ports:

    print(port)
```

用途：

* 查找设备
* 自动识别串口
* 上位机开发

---

# 9. 创建串口对象

## Serial()

pySerial 的核心类。

```python id="tz9blw"
import serial

ser = serial.Serial(
    port='COM3',
    baudrate=115200
)
```

---

## 常见参数

| 参数       | 作用   |
| -------- | ---- |
| port     | 串口号  |
| baudrate | 波特率  |
| bytesize | 数据位  |
| parity   | 校验位  |
| stopbits | 停止位  |
| timeout  | 超时时间 |

---

# 10. 打开串口

创建对象时：

默认会自动打开。

也可以：

```python id="wwfqpn"
ser.open()
```

---

# 11. 关闭串口

```python id="muqycc"
ser.close()
```

关闭串口非常重要。

否则：

串口可能被占用。

---

# 12. 判断串口状态

## is_open

```python id="f3j2vj"
print(ser.is_open)
```

返回：

```python id="l6o58o"
True
False
```

---

# 13. 发送数据

---

## write()

发送字节数据。

```python id="jlwm0i"
ser.write(b'Hello')
```

注意：

pySerial 发送的是：

```text id="1qazp0"
bytes
```

而不是：

```text id="zowjlwm"
str
```

---

## 字符串转 bytes

```python id="3tggu8"
data = 'Hello'.encode()

ser.write(data)
```

---

## 发送整数

```python id="ncyrrr"
ser.write(bytes([1,2,3,4]))
```

---

# 14. 接收数据

---

## read()

读取指定字节数。

```python id="r7j98u"
data = ser.read(5)

print(data)
```

---

## readline()

读取一行数据。

通常用于：

```text id="9m0z0r"
以换行符结尾的数据
```

```python id="a9z8yk"
data = ser.readline()

print(data)
```

---

## read_all()

读取全部缓存数据。

```python id="8qte5p"
data = ser.read_all()
```

---

# 15. bytes 与 str

串口本质上传输的是：

```text id="ji7f3n"
二进制数据
```

因此：

pySerial 大部分操作都围绕：

```text id="gq0mtv"
bytes
```

进行。

---

## bytes 转字符串

```python id="9cn3fy"
data = b'Hello'

text = data.decode()

print(text)
```

---

## 字符串转 bytes

```python id="1lzy2u"
text = 'Hello'

data = text.encode()
```

---

# 16. timeout 超时

## timeout

表示：

```text id="7jv85n"
等待数据的时间
```

例如：

```python id="w0mt73"
ser = serial.Serial(

    'COM3',

    115200,

    timeout=1
)
```

含义：

```text id="kcjlwm"
最多等待1秒
```

---

# 17. in_waiting

获取接收缓存区数据长度。

```python id="cxg7ya"
print(ser.in_waiting)
```

用途：

判断：

```text id="7t2qzi"
是否收到数据
```

---

# 18. 持续读取串口

串口程序通常：

```text id="z7whii"
循环读取
```

例如：

```python id="i13t0u"
while True:

    if ser.in_waiting:

        data = ser.readline()

        print(data)
```

---

# 19. flush()

## flush()

立即发送缓存数据。

```python id="t6ns2d"
ser.flush()
```

通常：

串口会自动发送。

但某些情况下：

需要手动刷新。

---

# 20. reset_input_buffer()

清空接收缓存区。

```python id="lkjlwm"
ser.reset_input_buffer()
```

---

# 21. reset_output_buffer()

清空发送缓存区。

```python id="89vmmi"
ser.reset_output_buffer()
```

---

# 22. 常见通信流程

典型串口流程：

```text id="nl5z5y"
打开串口
↓
发送数据
↓
接收数据
↓
解析数据
↓
关闭串口
```

---

# 23. Arduino 通信示例

Arduino：

```cpp id="lqqkl2"
void setup() {

    Serial.begin(115200);
}

void loop() {

    Serial.println("Hello");

    delay(1000);
}
```

Python：

```python id="7d6o92"
import serial

ser = serial.Serial(
    'COM3',
    115200
)

while True:

    data = ser.readline()

    print(data)
```

---

# 24. 常见编码格式

---

## UTF-8

最常见。

```python id="1hq8yz"
data.decode('utf-8')
```

---

## GBK

Windows 中文常见。

```python id="n3h4hs"
data.decode('gbk')
```

---

# 25. 二进制数据通信

串口不仅能传文本。

还能传：

* 传感器数据
* 图像数据
* 浮点数
* 协议数据

例如：

```python id="9mjlwm"
ser.write(bytes([0xAA,0x55]))
```

---

# 26. struct 模块

处理二进制协议时：

通常配合：

```python id="a2zt8r"
import struct
```

例如：

---

## 打包数据

```python id="lgd2pn"
data = struct.pack(
    'f',
    3.14
)
```

---

## 解包数据

```python id="eahjlwm"
value = struct.unpack(
    'f',
    data
)
```

---

# 27. 上位机开发

pySerial 常用于：

```text id="53eyv9"
Python 上位机
```

通常配合：

* Tkinter
* PyQt
* matplotlib

实现：

* 数据显示
* 波形绘制
* 实时监控

---

# 28. matplotlib 实时波形

常见结构：

```text id="jlwmmb"
串口读取
↓
解析数据
↓
matplotlib绘图
```

用于：

* 示波器
* 传感器监控
* 实时曲线

---

# 29. 多线程串口

GUI 程序中：

不能阻塞主线程。

因此通常：

```text id="xjlwm9"
子线程读取串口
```

例如：

* threading
* queue

---

# 30. 常见问题

---

## 1. 串口被占用

错误：

```text id="49jlwm"
PermissionError
```

原因：

* 串口监视器未关闭
* 其他程序占用

---

## 2. 波特率不一致

现象：

```text id="jlwm4x"
乱码
```

---

## 3. timeout 设置错误

timeout 太大：

程序卡顿。

timeout 太小：

可能读不到完整数据。

---

## 4. bytes 与 str 混淆

错误：

```text id="jlwmg1"
TypeError
```

本质：

```text id="8jlwmc"
bytes ≠ str
```

---

# 31. pySerial 的局限性

pySerial 本质：

```text id="jlwmxr"
串口通信库
```

因此：

* 不负责协议解析
* 不负责界面
* 不负责绘图

通常需要结合：

* struct
* threading
* tkinter
* matplotlib

使用。

---

# 32. 推荐学习路线

建议顺序：

```text id="jlwm89"
串口基础
↓
打开串口
↓
发送数据
↓
接收数据
↓
bytes处理
↓
实时读取
↓
协议解析
↓
GUI上位机
```

---

# 33. 推荐练习项目

---

## 初级项目

### 1. 串口助手

功能：

* 打开串口
* 发送文本
* 接收数据

适合：

* 熟悉 pySerial 基础 API
* 理解串口通信流程

```python
import serial
import time

# 打开串口
ser = serial.Serial(
    port='COM3',
    baudrate=115200,
    timeout=1
)

print("串口已打开")

while True:

    # 输入发送内容
    text = input("发送内容：")

    # 退出程序
    if text == 'exit':
        break

    # 字符串转 bytes
    ser.write(text.encode())

    # 等待设备返回
    time.sleep(0.1)

    # 读取返回数据
    if ser.in_waiting:

        data = ser.read_all()

        print("收到：", data.decode(errors='ignore'))

# 关闭串口
ser.close()

print("串口已关闭")
```

---

### 2. Arduino 通信

Arduino：

```cpp
void setup() {

    Serial.begin(115200);
}

void loop() {

    Serial.println("Hello From Arduino");

    delay(1000);
}
```

Python：

```python
import serial

# 打开串口
ser = serial.Serial(
    'COM3',
    115200,
    timeout=1
)

while True:

    # 读取一行
    data = ser.readline()

    # bytes 转字符串
    text = data.decode(
        'utf-8',
        errors='ignore'
    )

    print(text)
```

---

# 中级项目

---

## 1. 实时数据显示

功能：

* 持续读取串口
* 实时显示传感器数据

适合：

* STM32
* ESP32
* Arduino

发送实时数据。

```python
import serial

ser = serial.Serial(
    'COM3',
    115200,
    timeout=1
)

while True:

    # 判断是否收到数据
    if ser.in_waiting:

        data = ser.readline()

        try:

            # 解码
            text = data.decode().strip()

            # 转 float
            value = float(text)

            print("传感器数据：", value)

        except:

            print("数据解析失败")
```

---

## 2. 串口聊天工具

功能：

* 一边发送
* 一边接收

需要：

```text
两个串口设备
或
虚拟串口
```

```python
import serial
import threading

ser = serial.Serial(
    'COM3',
    115200,
    timeout=1
)

# 接收线程
def receive_thread():

    while True:

        if ser.in_waiting:

            data = ser.readline()

            print(
                "\n收到：",
                data.decode(errors='ignore')
            )

# 启动线程
threading.Thread(
    target=receive_thread,
    daemon=True
).start()

# 主线程发送
while True:

    text = input("发送：")

    ser.write(text.encode())
```

---

# 高级项目

---

## 1. Python 上位机

功能：

* GUI 界面
* 串口通信
* 数据显示

这里使用：

```text
Tkinter + pySerial
```

```python
import tkinter as tk
import serial

# 打开串口
ser = serial.Serial(
    'COM3',
    115200,
    timeout=1
)

# 创建窗口
root = tk.Tk()

root.title("串口上位机")

# 文本框
text_box = tk.Text(root)

text_box.pack()

# 发送函数
def send_data():

    data = entry.get()

    ser.write(data.encode())

# 输入框
entry = tk.Entry(root)

entry.pack()

# 发送按钮
button = tk.Button(
    root,
    text="发送",
    command=send_data
)

button.pack()

root.mainloop()
```

---

## 2. 实时波形显示

功能：

* 串口接收数据
* matplotlib 实时绘图

适用于：

* 传感器波形
* PID 曲线
* 电机数据监控

```python
import serial
import matplotlib.pyplot as plt

ser = serial.Serial(
    'COM3',
    115200,
    timeout=1
)

plt.ion()

data_list = []

while True:

    if ser.in_waiting:

        try:

            # 接收数据
            data = ser.readline()

            value = float(
                data.decode().strip()
            )

            # 保存数据
            data_list.append(value)

            # 只保留100个点
            data_list = data_list[-100:]

            # 清空画布
            plt.clf()

            # 绘图
            plt.plot(data_list)

            plt.title("Real-time Data")

            plt.pause(0.01)

        except:

            pass
```

---

## 3. 二进制协议通信

功能：

* 发送二进制数据
* 解析协议数据

适用于：

* STM32
* 工业通信
* 机器人通信

```python
import serial
import struct

ser = serial.Serial(
    'COM3',
    115200
)

# 打包 float 数据
data = struct.pack(
    'f',
    3.14
)

# 发送数据
ser.write(data)

# 接收4字节 float
recv = ser.read(4)

# 解包
value = struct.unpack(
    'f',
    recv
)

print(value)
```

