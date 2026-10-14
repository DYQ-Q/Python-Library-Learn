# 1. OpenCV 简介

OpenCV 是 Python 中最常用的：

```text
计算机视觉库
```

全称：**Open** **S**ource **C**omputer **V**ision Library，由 Intel 于 1999 年发起，经 20 余年发展，已成为全球最流行的跨平台视觉处理工具。

主要用于：

* 图像处理（滤波、边缘检测、几何变换）
* 视频分析（运动检测、目标跟踪）
* 特征检测与匹配（SIFT、ORB）
* 目标检测（人脸检测、物体识别）
* 相机标定与 3D 重建
* 深度学习模型部署

与 Pillow 不同：

```text
Pillow：轻量级图像处理库，侧重图像格式转换和基础操作
OpenCV：重量级计算机视觉库，包含 2500+ 算法，支持实时视觉任务
```

例如：

Pillow：

```python
from PIL import Image
img = Image.open('photo.jpg')
img.show()
```

OpenCV：

```python
import cv2
img = cv2.imread('photo.jpg')
cv2.imshow('Image', img)
cv2.waitKey(0)
```

---

# 2. 安装

## 2.1 安装 OpenCV

OpenCV 提供多个 PyPI 包，根据需求选择：

| 包名 | 说明 |
| ---- | ---- |
| `opencv-python` | **主包**，包含核心功能（推荐大多数用户） |
| `opencv-contrib-python` | 主包 + 扩展模块（含 SIFT 等专利算法） |
| `opencv-python-headless` | 无 GUI 依赖（适合服务器/CI 环境） |
| `opencv-contrib-python-headless` | 扩展版 + 无 GUI（服务器端完整功能） |

安装命令：

```bash
# 基础安装（推荐）
pip install opencv-python

# 需要 SIFT 等额外功能
pip install opencv-contrib-python

# 服务器环境（无 GUI）
pip install opencv-python-headless
```

---

## 2.2 验证安装

```python
import cv2

print(cv2.__version__)   # 输出如 "4.9.0"
```

---

## 2.3 虚拟环境（推荐）

```bash
# 创建虚拟环境
python -m venv .venv

# 激活（Windows）
.venv\Scripts\activate

# 激活（Linux/macOS）
source .venv/bin/activate

# 在虚拟环境中安装
pip install opencv-python
```



---

# 3. OpenCV 的核心思想

OpenCV 的核心设计：

```text
图像 = NumPy 数组 + 算法函数
```

三大核心：

```text
1. 图像即数组：OpenCV 读取的图像就是 NumPy 多维数组
2. 函数式 API：所有操作通过函数调用完成（如 cv2.resize()）
3. BGR 色彩空间：与常规 RGB 不同，OpenCV 默认使用 BGR 顺序
```

与 NumPy 的紧密关系：

```text
OpenCV 的图像本质是 NumPy ndarray
可以直接使用 NumPy 操作像素
```

---

# 4. 核心模块架构

OpenCV 采用模块化设计，主要包含：

| 模块 | 功能 |
| ---- | ---- |
| **Core** | 基础数据结构（Mat、Point、Rect 等） |
| **Imgproc** | 图像处理核心算法（滤波、边缘检测、几何变换） |
| **Features2d** | 特征检测与匹配（SIFT、ORB） |
| **Calib3d** | 相机标定与 3D 重建 |
| **Video** | 视频分析与运动检测 |
| **DNN** | 深度学习模型部署 |
| **ML** | 机器学习算法 |
| **Objdetect** | 目标检测（Haar 级联分类器） |

---

# 5. 图像基础操作

## 5.1 读取图像

```python
import cv2

# 彩色模式（默认）
img = cv2.imread('photo.jpg', cv2.IMREAD_COLOR)

# 灰度模式
gray = cv2.imread('photo.jpg', cv2.IMREAD_GRAYSCALE)

# 保留 Alpha 通道（PNG 透明背景）
img_alpha = cv2.imread('photo.png', cv2.IMREAD_UNCHANGED)

# 检查是否加载成功
if img is None:
    raise FileNotFoundError("图像加载失败，请检查路径")
```

读取模式说明：

```text
cv2.IMREAD_COLOR      ：3通道BGR彩色图（默认）
cv2.IMREAD_GRAYSCALE  ：单通道灰度图
cv2.IMREAD_UNCHANGED  ：包含Alpha通道
```

---

## 5.2 显示图像

```python
# 创建窗口
cv2.namedWindow('Image Viewer', cv2.WINDOW_NORMAL)  # 可调整大小

# 显示图像
cv2.imshow('Image Viewer', img)

# 等待按键（0 表示无限等待）
cv2.waitKey(0)

# 关闭所有窗口
cv2.destroyAllWindows()
```



---

## 5.3 保存图像

```python
cv2.imwrite('output.jpg', img)      # 保存为 JPG
cv2.imwrite('output.png', img)      # 保存为 PNG（支持透明）
```

---

## 5.4 图像属性

```python
# 获取图像尺寸
height, width = img.shape[:2]       # 灰度图
height, width, channels = img.shape # 彩色图

print(f"尺寸：{width}x{height}，通道数：{channels}")
```



---

# 6. 像素级操作

## 6.1 访问与修改像素

```python
# 获取 (y, x) 位置的像素（BGR 顺序）
pixel = img[100, 50]                # 返回 [B, G, R]
b, g, r = img[100, 50]              # 分别获取

# 修改像素值
img[100, 50] = [255, 0, 0]          # 改为蓝色
```



> **注意**：OpenCV 使用 `(行, 列)` 即 `(y, x)` 顺序访问像素。

---

## 6.2 ROI（感兴趣区域）

```python
# 提取 ROI（y1:y2, x1:x2）
roi = img[50:150, 100:200]

# 在 ROI 上绘制矩形
cv2.rectangle(roi, (10, 10), (90, 90), (0, 255, 0), 2)
```



---

## 6.3 通道分离与合并

```python
# 分离 BGR 通道
b, g, r = cv2.split(img)

# 合并通道
img_merged = cv2.merge([b, g, r])

# 更高效的方式（避免 split 性能开销）
b = img[:, :, 0]
g = img[:, :, 1]
r = img[:, :, 2]
```

---

# 7. 颜色空间转换

## 7.1 BGR ↔ 灰度

```python
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
```



---

## 7.2 BGR ↔ HSV

HSV 更适合基于颜色的分割：

```python
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
```

---

## 7.3 BGR ↔ RGB

OpenCV 使用 BGR，Matplotlib 使用 RGB：

```python
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
```

---

## 7.4 二值化

```python
# 简单阈值
_, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# 自适应阈值（适合光照不均）
binary = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                cv2.THRESH_BINARY, 11, 2)
```



---

# 8. 几何变换

## 8.1 缩放

```python
# 指定尺寸
resized = cv2.resize(img, (300, 200))

# 按比例缩放
scale = 0.5
resized = cv2.resize(img, None, fx=scale, fy=scale)

# 插值方法
resized = cv2.resize(img, (300, 200), interpolation=cv2.INTER_LINEAR)
```

插值方法选择：

```text
cv2.INTER_NEAREST  ：最近邻（速度快，可能锯齿）
cv2.INTER_LINEAR   ：双线性（默认，效果平衡）
cv2.INTER_CUBIC    ：双三次（质量高，速度慢）
cv2.INTER_AREA     ：区域插值（缩小图像时效果更好）
```



---

## 8.2 旋转

```python
(h, w) = img.shape[:2]
center = (w // 2, h // 2)

# 获取旋转矩阵（中心点，角度，缩放）
M = cv2.getRotationMatrix2D(center, 45, 1.0)   # 顺时针 45 度

# 应用仿射变换
rotated = cv2.warpAffine(img, M, (w, h))
```



---

## 8.3 平移

```python
# 平移矩阵：[[1, 0, tx], [0, 1, ty]]
M = np.float32([[1, 0, 100], [0, 1, 50]])
shifted = cv2.warpAffine(img, M, (w, h))
```



---

## 8.4 翻转

```python
flip_h = cv2.flip(img, 1)   # 水平翻转
flip_v = cv2.flip(img, 0)   # 垂直翻转
flip_both = cv2.flip(img, -1) # 两个方向
```

---

# 9. 图像滤波

## 9.1 均值滤波（模糊）

```python
blur = cv2.blur(img, (5, 5))   # 5x5 内核
```

---

## 9.2 高斯滤波

```python
gaussian = cv2.GaussianBlur(img, (5, 5), 0)
```

---

## 9.3 中值滤波（去椒盐噪声）

```python
median = cv2.medianBlur(img, 5)
```

---

## 9.4 双边滤波（保边去噪）

```python
bilateral = cv2.bilateralFilter(img, 9, 75, 75)
```

---

# 10. 边缘检测

## 10.1 Canny 边缘检测

```python
edges = cv2.Canny(img, 100, 200)   # 低阈值，高阈值
```



---

## 10.2 Sobel 算子

```python
# X 方向梯度
sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)

# Y 方向梯度
sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

# 梯度幅值
magnitude = np.sqrt(sobelx**2 + sobely**2)
```

---

## 10.3 Laplacian

```python
laplacian = cv2.Laplacian(gray, cv2.CV_64F)
```

---

# 11. 形态学操作

## 11.1 腐蚀与膨胀

```python
kernel = np.ones((5, 5), np.uint8)

erosion = cv2.erode(img, kernel, iterations=1)
dilation = cv2.dilate(img, kernel, iterations=1)
```

---

## 11.2 开运算与闭运算

```python
# 开运算：先腐蚀后膨胀（去除小噪点）
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

# 闭运算：先膨胀后腐蚀（填充小孔）
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
```

---

# 12. 轮廓检测

## 12.1 查找轮廓

```python
# 二值图（Canny 或阈值处理）
edges = cv2.Canny(gray, 50, 150)

# 查找轮廓
contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
```

---

## 12.2 绘制轮廓

```python
cv2.drawContours(img, contours, -1, (0, 255, 0), 2)   # -1 表示绘制所有轮廓
```

---

## 12.3 轮廓特征

```python
for cnt in contours:
    area = cv2.contourArea(cnt)                        # 面积
    perimeter = cv2.arcLength(cnt, True)               # 周长
    x, y, w, h = cv2.boundingRect(cnt)                 # 外接矩形
    (cx, cy), radius = cv2.minEnclosingCircle(cnt)     # 最小外接圆
```

---

# 13. 视频处理

## 13.1 读取视频文件或摄像头

```python
# 从摄像头读取（0 为默认摄像头）
cap = cv2.VideoCapture(0)

# 从视频文件读取
cap = cv2.VideoCapture('video.mp4')

# 检查是否打开
if not cap.isOpened():
    print("无法打开摄像头/视频")
    exit()
```



---

## 13.2 逐帧读取与显示

```python
while True:
    ret, frame = cap.read()      # ret 为 True 表示读取成功

    if not ret:
        break

    # 处理每一帧（如转为灰度）
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 显示
    cv2.imshow('Frame', gray)

    # 按 'q' 退出
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
```



> **注意**：`cv2.waitKey()` 的参数控制播放速度：
> - 值太小 → 视频播放过快
> - 值太大 → 视频播放过慢（慢动作）

---

## 13.3 保存视频

```python
# 定义编码器和 VideoWriter
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

while True:
    ret, frame = cap.read()
    if not ret:
        break
    out.write(frame)             # 写入帧

out.release()
```

---

# 14. 特征检测与匹配

## 14.1 SIFT（尺度不变特征变换）

```python
# 需要 opencv-contrib-python
sift = cv2.SIFT_create()

# 检测关键点和描述符
keypoints, descriptors = sift.detectAndCompute(gray, None)

# 绘制关键点
img_with_kp = cv2.drawKeypoints(img, keypoints, None)
```



---

## 14.2 ORB（快速特征检测）

```python
orb = cv2.ORB_create()

keypoints, descriptors = orb.detectAndCompute(gray, None)
```

---

## 14.3 特征匹配（BFMatcher）

```python
# 创建 BFMatcher
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

# 匹配
matches = bf.match(des1, des2)

# 排序并绘制前 N 个匹配
matches = sorted(matches, key=lambda x: x.distance)
img_matches = cv2.drawMatches(img1, kp1, img2, kp2, matches[:10], None)
```

---

# 15. 人脸检测（Haar 级联）

## 15.1 加载预训练模型

OpenCV 提供预训练的 Haar 级联分类器：

```python
# 加载人脸检测器
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

# 加载眼睛检测器
eye_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_eye.xml'
)
```

---

## 15.2 检测人脸

```python
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30)
)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
```



---

# 16. 绘制图形与文本

## 16.1 绘制基本图形

```python
# 矩形
cv2.rectangle(img, (50, 50), (200, 150), (0, 255, 0), 2)

# 圆形
cv2.circle(img, (100, 100), 50, (0, 0, 255), -1)   # -1 填充

# 线段
cv2.line(img, (0, 0), (200, 200), (255, 0, 0), 3)

# 椭圆
cv2.ellipse(img, (200, 200), (100, 50), 0, 0, 180, (255, 0, 0), 2)

# 多边形
pts = np.array([[10,5], [20,30], [70,20], [50,10]], np.int32)
cv2.polylines(img, [pts], True, (0, 255, 255), 2)
```

---

## 16.2 绘制文本

```python
cv2.putText(img, 'Hello OpenCV', (50, 50),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
```



---

# 17. 深度学习（DNN 模块）

OpenCV 的 DNN 模块支持加载和运行预训练深度学习模型：

```python
# 加载模型
net = cv2.dnn.readNet('model.pb', 'model.pbtxt')

# 准备输入
blob = cv2.dnn.blobFromImage(img, 1.0, (224, 224), (104, 117, 123))
net.setInput(blob)

# 推理
output = net.forward()
```

支持的框架：

```text
• TensorFlow（.pb）
• Caffe（.caffemodel）
• ONNX（.onnx）
• PyTorch（通过 ONNX）
• Darknet（YOLO）
```

---

# 18. 常见应用场景

| 领域 | 应用 | 技术 |
| ---- | ---- | ---- |
| 安防监控 | 人脸检测、运动检测 | Haar 级联、背景减除 |
| 自动驾驶 | 车道线检测、障碍物识别 | Canny、Hough 变换 |
| 医疗影像 | 病灶检测、图像分割 | 阈值处理、轮廓检测 |
| 工业质检 | 缺陷检测、尺寸测量 | 边缘检测、模板匹配 |
| AR/VR | 标记追踪、姿态估计 | 特征匹配、相机标定 |
| 图像编辑 | 滤镜、美颜 | 滤波、颜色空间转换 |

---

# 19. 常见问题

## 1. 图像显示为奇怪的颜色

```text
原因：OpenCV 使用 BGR，Matplotlib 使用 RGB
解决：使用 cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 转换
```



---

## 2. cv2.imread() 返回 None

```text
可能原因：
- 文件路径错误（使用绝对路径或检查相对路径）
- 文件名包含中文或特殊字符
- 图片格式不受支持
- OpenCV 编译时未包含相应解码器
```

---

## 3. 摄像头无法打开

```text
检查：
- 摄像头是否被其他程序占用
- 索引是否正确（0, 1, 2...）
- 权限问题（Linux 需要 /dev/video* 权限）
```

---

## 4. 视频播放速度异常

```text
cv2.waitKey() 的参数控制播放速度
值越小播放越快，值越大播放越慢
正常速度：cv2.waitKey(25)（约 40 FPS）
```



---

## 5. 性能问题（实时处理慢）

```text
优化方法：
- 降低图像分辨率
- 使用灰度图而非彩色图
- 使用 ROI 减少处理区域
- 使用 OpenCV 的 UMat（GPU 加速）
- 考虑使用 opencv-python-headless（减少开销）
```

---

# 20. OpenCV 与其他库的对比

| 功能 | OpenCV | Pillow | scikit-image | NumPy |
| ---- | ------ | ------ | ------------ | ----- |
| 主要用途 | 计算机视觉 | 图像基础操作 | 图像处理算法 | 数值计算 |
| 实时视频 | ✅ | ❌ | ❌ | ❌ |
| 特征检测 | ✅ | ❌ | ✅（有限） | ❌ |
| 目标检测 | ✅ | ❌ | ❌ | ❌ |
| 深度学习部署 | ✅ | ❌ | ❌ | ❌ |
| 相机标定 | ✅ | ❌ | ❌ | ❌ |
| 速度 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ | - |

---

# 21. 推荐学习路线

```text
安装与环境配置
↓
图像读写与显示（imread, imshow, imwrite）
↓
像素级操作与 ROI
↓
颜色空间转换（BGR、灰度、HSV）
↓
几何变换（缩放、旋转、平移）
↓
图像滤波（模糊、高斯、中值）
↓
边缘检测（Canny、Sobel）
↓
形态学操作（腐蚀、膨胀、开闭运算）
↓
轮廓检测与绘制
↓
视频处理（读取、显示、保存）
↓
特征检测（SIFT、ORB）
↓
人脸检测（Haar 级联）
↓
深度学习部署（DNN 模块）
↓
综合实战项目
```

---

# 22. 推荐练习项目

## 初级

* 图像滤镜（灰度、二值化、边缘检测）
* 视频中实时边缘检测

---

## 中级

* 人脸检测与绘制框
* 运动检测（帧差法）
* 图像拼接（特征匹配）

---

## 高级

* 实时人脸识别（结合深度学习）
* 车道线检测（Hough 变换）
* 目标追踪（KCF、CSRT）
* 车牌检测与识别

---

# 23. 总结与速查

## 常用导入与函数

```python
import cv2
import numpy as np

# 读写
cv2.imread(path, flags)
cv2.imshow(winname, mat)
cv2.imwrite(filename, img)

# 颜色空间
cv2.cvtColor(src, code)

# 几何变换
cv2.resize(src, dsize, fx, fy, interpolation)
cv2.warpAffine(src, M, dsize)
cv2.getRotationMatrix2D(center, angle, scale)

# 滤波
cv2.blur(src, ksize)
cv2.GaussianBlur(src, ksize, sigmaX)
cv2.medianBlur(src, ksize)

# 边缘检测
cv2.Canny(image, threshold1, threshold2)

# 形态学
cv2.erode(src, kernel, iterations)
cv2.dilate(src, kernel, iterations)
cv2.morphologyEx(src, op, kernel)

# 轮廓
cv2.findContours(image, mode, method)
cv2.drawContours(image, contours, contourIdx, color, thickness)

# 视频
cv2.VideoCapture(source)
cv2.VideoWriter(filename, fourcc, fps, frameSize)

# 特征
cv2.SIFT_create()
cv2.ORB_create()

# 人脸检测
cv2.CascadeClassifier(filename)
```

## 核心思想

```text
图像 = NumPy 数组
处理 = 函数调用
视觉 = 算法组合
```