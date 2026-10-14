# PyTorch 学习笔记

---

# 1. PyTorch 简介

PyTorch 是目前最主流的深度学习框架之一。

主要用于：

* 深度学习
* 神经网络
* 计算机视觉
* 自然语言处理
* 强化学习
* 科学计算
* 大模型训练

最初由：

[Meta AI](https://ai.meta.com/?utm_source=chatgpt.com)

开发。

---

PyTorch 的核心特点：

* 动态计算图
* Python 风格
* 自动求导
* GPU 加速
* 与 NumPy 风格接近

本质上：

```text
Tensor + 自动求导 + 神经网络 + GPU
```

---

# 2. 安装

建议先查看官方安装命令：

[PyTorch 官方安装页](https://pytorch.org/get-started/locally/?utm_source=chatgpt.com)

常见安装：

```bash
pip install torch torchvision torchaudio
```

测试：

```python
import torch

print(torch.__version__)
```

---

# 3. PyTorch 的整体结构

学习 PyTorch 时建议先理解结构。

```text
Tensor
↓
自动求导
↓
神经网络
↓
数据集
↓
训练循环
↓
模型保存
↓
部署
```

---

# 4. Tensor（张量）

Tensor 是 PyTorch 最核心的数据结构。

可以理解成：

```text
强化版 ndarray
```

支持：

* GPU
* 自动求导
* 深度学习运算

---

## 创建 Tensor

```python
import torch

a = torch.tensor([1,2,3])

print(a)
```

输出：

```text
tensor([1,2,3])
```

---

## 查看类型

```python
print(a.dtype)
```

---

## 查看形状

```python
print(a.shape)
```

---

## 指定数据类型

```python
a = torch.tensor(
    [1,2,3],

    dtype=torch.float32
)
```

---

# 5. Tensor 创建方法

---

## zeros()

全零。

```python
torch.zeros(3,4)
```

---

## ones()

全一。

```python
torch.ones(3,4)
```

---

## rand()

随机。

```python
torch.rand(3,4)
```

范围：

```text
0~1
```

---

## randint()

随机整数。

```python
torch.randint(
    0,
    10,

    (3,4)
)
```

---

## arange()

等差数列。

```python
torch.arange(10)
```

---

## linspace()

连续采样。

```python
torch.linspace(
    0,
    1,

    100
)
```

---

# 6. Tensor 操作

---

## reshape()

改变形状。

```python
x.reshape(
    2,
    3
)
```

---

## view()

改变视图。

```python
x.view(
    2,
    3
)
```

---

## transpose()

转置。

```python
x.T
```

---

## squeeze()

删除维度。

```python
x.squeeze()
```

---

## unsqueeze()

增加维度。

```python
x.unsqueeze(0)
```

---

# 7. Tensor 运算

---

## 加减乘除

```python
a+b

a-b

a*b

a/b
```

---

## 矩阵乘法

```python
a @ b
```

或：

```python
torch.matmul(a,b)
```

---

## 求和

```python
x.sum()
```

---

## 求平均

```python
x.mean()
```

---

## 最大值

```python
x.max()
```

---

## 最小值

```python
x.min()
```

---

# 8. GPU 运算

PyTorch 最大优势之一。

---

查看 GPU：

```python
torch.cuda.is_available()
```

---

移动到 GPU：

```python
device='cuda'

x=x.to(device)
```

返回 CPU：

```python
x.cpu()
```

---

查看 GPU：

```python
torch.cuda.get_device_name()
```

---

# 9. NumPy 与 Tensor 转换

---

NumPy → Tensor

```python
import numpy as np

a=np.array([1,2])

t=torch.from_numpy(a)
```

---

Tensor → NumPy

```python
t.numpy()
```

---

# 10. 自动求导

PyTorch 核心能力。

---

## requires_grad

开启梯度。

```python
x=torch.tensor(

    2.0,

    requires_grad=True
)
```

---

## backward()

反向传播。

```python
y=x**2

y.backward()
```

---

获取梯度：

```python
print(x.grad)
```

结果：

```text
4
```

---

# 11. 神经网络模块

PyTorch 提供：

```python
torch.nn
```

用于搭建网络。

---

常见模块：

---

## Linear

全连接层。

```python
nn.Linear(
    10,
    20
)
```

---

## Conv2d

卷积层。

```python
nn.Conv2d()
```

---

## MaxPool2d

池化。

```python
nn.MaxPool2d()
```

---

## BatchNorm

归一化。

```python
nn.BatchNorm2d()
```

---

## Dropout

防止过拟合。

```python
nn.Dropout()
```

---

# 12. 激活函数

---

## ReLU

```python
nn.ReLU()
```

---

## Sigmoid

```python
nn.Sigmoid()
```

---

## Tanh

```python
nn.Tanh()
```

---

## Softmax

```python
nn.Softmax()
```

---

# 13. 搭建模型

推荐继承：

```python
nn.Module
```

示例：

```python
class Net(nn.Module):

    def __init__(self):

        super().__init__()

        self.fc=nn.Linear(
            10,
            1
        )

    def forward(self,x):

        return self.fc(x)
```

---

# 14. Dataset 与 DataLoader

用于管理数据。

---

## Dataset

定义数据。

---

## DataLoader

负责：

* 批处理
* 打乱
* 加载

示例：

```python
loader=DataLoader(

    dataset,

    batch_size=32,

    shuffle=True
)
```

---

# 15. 损失函数

衡量预测误差。

---

## MSELoss

回归。

```python
nn.MSELoss()
```

---

## CrossEntropyLoss

分类。

```python
nn.CrossEntropyLoss()
```

---

## BCE

二分类。

```python
nn.BCELoss()
```

---

# 16. 优化器

更新参数。

---

## SGD

```python
torch.optim.SGD()
```

---

## Adam

最常用。

```python
torch.optim.Adam()
```

---

## RMSprop

```python
torch.optim.RMSprop()
```

---

# 17. 标准训练流程

深度学习核心。

```text
数据
↓
模型
↓
前向传播
↓
计算损失
↓
反向传播
↓
优化更新
↓
重复
```

典型代码：

```python
for epoch:

    pred=model(x)

    loss()

    backward()

    step()
```

---

# 18. 保存模型

保存参数：

```python
torch.save(

    model.state_dict(),

    'model.pth'
)
```

---

读取：

```python
model.load_state_dict(

    torch.load(

        'model.pth'
    )
)
```

---

# 19. 推理模式

关闭梯度。

```python
with torch.no_grad():

    y=model(x)
```

作用：

* 更快
* 更省显存

---

# 20. 常见模型

---

## MLP

全连接。

---

## CNN

图像。

---

## RNN

序列。

---

## LSTM

时序。

---

## Transformer

现代 AI。

---

# 21. torchvision

用于视觉任务。

安装：

```bash
pip install torchvision
```

常见：

* 数据集
* 图像处理
* 预训练模型

---

## 常见数据集

```python
MNIST

CIFAR10
```

---

## transforms

图像预处理。

```python
transforms.Compose()
```

---

# 22. torch.nn.functional

函数式 API。

常见：

```python
F.relu()

F.softmax()

F.cross_entropy()
```

---

# 23. tensorboard

训练可视化。

安装：

```bash
pip install tensorboard
```

启动：

```bash
tensorboard --logdir=runs
```

---

# 24. 常见问题

---

## Tensor 与 NumPy 混用

错误：

```text
TypeError
```

---

## 忘记 GPU

现象：

训练很慢。

---

## 忘记：

```python
optimizer.zero_grad()
```

导致：

梯度累积。

---

## train eval 模式混乱

训练：

```python
model.train()
```

推理：

```python
model.eval()
```

---

# 25. PyTorch 与 TensorFlow

| 项目   | PyTorch | TensorFlow |
| ---- | ------- | ---------- |
| 学习难度 | 低       | 高          |
| 调试   | 强       | 中          |
| 研究   | 强       | 强          |
| 部署   | 中       | 强          |

---

# 26. 常见应用

---

## AI

* 大语言模型
* 生成模型

---

## 机器人

* 强化学习
* 控制

---

## 图像

* 分类
* 检测

---

## NLP

* 翻译
* 对话

---

# 27. 推荐学习路线

```text
Tensor
↓
自动求导
↓
神经网络
↓
训练流程
↓
CNN
↓
Transformer
↓
项目
```

---

# 28. 推荐练习项目

## 初级

* 手写数字识别
* 线性回归

代码示例（线性回归）：

```python
import torch
import torch.nn as nn

x=torch.rand(100,1)

y=2*x+1

model=nn.Linear(1,1)

loss_fn=nn.MSELoss()

opt=torch.optim.Adam(
    model.parameters()
)

for _ in range(200):

    pred=model(x)

    loss=loss_fn(
        pred,
        y
    )

    opt.zero_grad()

    loss.backward()

    opt.step()

print(model.weight)
```

---

## 中级

* CNN 图像分类
* 猫狗识别

代码示例（CNN）：

```python
import torch.nn as nn

model=nn.Sequential(

    nn.Conv2d(
        1,
        16,
        3
    ),

    nn.ReLU(),

    nn.MaxPool2d(2),

    nn.Flatten(),

    nn.Linear(
        2704,
        10
    )
)

print(model)
```

---

## 高级

* Transformer
* Diffusion
* 强化学习
* 机器人视觉

代码示例（Transformer）：

```python
import torch
import torch.nn as nn

model=nn.Transformer(

    d_model=512,

    nhead=8
)

src=torch.rand(
    10,
    32,
    512
)

tgt=torch.rand(
    20,
    32,
    512
)

out=model(
    src,
    tgt
)

print(out.shape)
```

---

# 29. 下一步推荐

建议继续学习：

* NumPy
* Matplotlib
* OpenCV
* Transformer
* CUDA
* ONNX
* TensorRT
