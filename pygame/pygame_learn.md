# 1. Pygame 简介

Pygame 是 Python 中最常用的：

```text
游戏开发库
```

基于 SDL 库，主要用于：

* 2D 游戏开发
* 图形绘制
* 音效播放
* 键盘/鼠标事件处理
* 碰撞检测
* 精灵动画
* 游戏循环管理

与 Tkinter 不同：

```text
Tkinter 用于 GUI 应用
Pygame 专为实时游戏设计
```

例如：

```python
import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("My Game")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0,0,0))
    pygame.display.flip()

pygame.quit()
```

结果：

```text
显示一个黑色窗口，点击关闭按钮退出
```

---

# 2. 安装

## 安装 Pygame

```bash
pip install pygame
```

---

## 测试安装

```python
import pygame
print(pygame.version.ver)
```

---

# 3. Pygame 的核心思想

Pygame 的核心：

```text
游戏循环 + 事件驱动 + 表面(Surface)绘制
```

典型游戏循环结构：

```text
初始化
↓
进入主循环：
  - 处理事件
  - 更新游戏状态
  - 绘制画面
  - 控制帧率
↓
退出
```

例如：

```python
clock = pygame.time.Clock()
while running:
    clock.tick(60)  # 限制 60 FPS
    # 事件处理、更新、绘制
```

---

# 4. 初始化与窗口

---

## pygame.init()

初始化所有模块。

```python
import pygame
pygame.init()
```

---

## 设置窗口

```python
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My Game")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)
```

---

## 获取屏幕信息

```python
info = pygame.display.Info()
print(info.current_w, info.current_h)
```

---

# 5. 事件处理

---

## 事件队列

```python
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            print("Space pressed")
    elif event.type == pygame.MOUSEBUTTONDOWN:
        print("Mouse clicked at", event.pos)
```

---

## 常用事件类型

| 事件 | 含义 |
| ---- | ---- |
| QUIT | 关闭窗口 |
| KEYDOWN | 键盘按下 |
| KEYUP | 键盘释放 |
| MOUSEBUTTONDOWN | 鼠标按下 |
| MOUSEBUTTONUP | 鼠标释放 |
| MOUSEMOTION | 鼠标移动 |

---

## 键盘按键常量

```python
pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN
pygame.K_a, pygame.K_b, ..., pygame.K_z
pygame.K_RETURN, pygame.K_ESCAPE, pygame.K_SPACE
```

---

# 6. 图形绘制

Pygame 在 Surface 上绘制图形。

---

## 颜色表示

```python
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
```

---

## 绘制基本形状

```python
# 矩形
pygame.draw.rect(screen, RED, (100, 100, 200, 150))  # (x,y,width,height)
pygame.draw.rect(screen, GREEN, (300, 200, 100, 50), 2)  # 2px 边框

# 圆形
pygame.draw.circle(screen, BLUE, (400, 300), 50)

# 椭圆
pygame.draw.ellipse(screen, WHITE, (500, 200, 80, 120))

# 线条
pygame.draw.line(screen, RED, (0,0), (800,600), 3)

# 多边形
points = [(200,400), (300,450), (250,500)]
pygame.draw.polygon(screen, GREEN, points)
```

---

## 填充背景

```python
screen.fill((0,0,0))  # 黑色背景
```

---

# 7. 图像与精灵

---

## 加载图像

```python
img = pygame.image.load('player.png')
img = pygame.transform.scale(img, (50, 50))  # 缩放
img_rotated = pygame.transform.rotate(img, 45)  # 旋转
```

---

## 绘制图像

```python
screen.blit(img, (100, 200))  # 在 (100,200) 位置绘制
```

---

## 图像透明与颜色键

```python
img.set_colorkey((0,0,0))  # 将黑色视为透明
```

---

## 简单精灵类

```python
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((0,255,0))
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 100

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
```

---

# 8. 精灵组与碰撞检测

---

## 创建精灵组

```python
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
```

---

## 更新与绘制

```python
all_sprites.update()
all_sprites.draw(screen)
```

---

## 碰撞检测

```python
# 矩形碰撞
if player.rect.colliderect(enemy.rect):
    print("Collision!")

# 精灵组碰撞
hits = pygame.sprite.spritecollide(player, enemies, False)
```

---

# 9. 文本显示

---

## 使用系统字体

```python
font = pygame.font.SysFont('Arial', 36)
text_surface = font.render('Hello Pygame', True, WHITE)
screen.blit(text_surface, (50, 50))
```

---

## 使用自定义字体

```python
font = pygame.font.Font('myfont.ttf', 32)
```

---

# 10. 声音播放

---

## 初始化混音器

```python
pygame.mixer.init()
```

---

## 播放音效

```python
sound = pygame.mixer.Sound('laser.wav')
sound.play()
```

---

## 播放背景音乐

```python
pygame.mixer.music.load('bgm.mp3')
pygame.mixer.music.play(-1)  # -1 循环播放
pygame.mixer.music.stop()
```

---

# 11. 控制帧率

```python
clock = pygame.time.Clock()
while running:
    dt = clock.tick(60) / 1000.0  # dt 为秒
    # 使用 dt 实现帧率无关移动
    player.rect.x += 200 * dt
```

---

# 12. 简单游戏循环模板

```python
import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()
running = True

while running:
    # 事件处理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # 更新逻辑
    # ...

    # 绘制
    screen.fill((0,0,0))
    # ... 绘制代码
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
```

---

# 13. 常用模块

| 模块 | 功能 |
| ---- | ---- |
| pygame.display | 窗口管理 |
| pygame.event | 事件处理 |
| pygame.draw | 绘制图形 |
| pygame.image | 图像加载与保存 |
| pygame.transform | 图像缩放、旋转 |
| pygame.font | 文本渲染 |
| pygame.mixer | 音频播放 |
| pygame.sprite | 精灵与碰撞 |
| pygame.time | 计时与帧率 |
| pygame.key | 键盘按键 |
| pygame.mouse | 鼠标状态 |
| pygame.Rect | 矩形区域 |

---

# 14. 矩形 Rect 类

```python
rect = pygame.Rect(x, y, width, height)

# 属性和方法
rect.x, rect.y, rect.width, rect.height
rect.center, rect.topleft, rect.bottomright
rect.move(dx, dy)
rect.move_ip(dx, dy)
rect.inflate(dx, dy)  # 扩大
rect.colliderect(other)  # 碰撞检测
```

---

# 15. 键盘连续检测

```python
keys = pygame.key.get_pressed()
if keys[pygame.K_LEFT]:
    player.rect.x -= 5
if keys[pygame.K_RIGHT]:
    player.rect.x += 5
```

---

# 16. 鼠标获取

```python
pos = pygame.mouse.get_pos()
buttons = pygame.mouse.get_pressed()  # (left, middle, right)
```

---

# 17. 显示 FPS

```python
font = pygame.font.SysFont('Arial', 24)
fps_text = font.render(f"FPS: {int(clock.get_fps())}", True, WHITE)
screen.blit(fps_text, (10,10))
```

---

# 18. 简单动画示例

```python
x = 0
while running:
    x += 5
    if x > 800:
        x = -50
    screen.fill((0,0,0))
    screen.blit(img, (x, 300))
    pygame.display.flip()
    clock.tick(60)
```

---

# 19. 常见应用

---

## 2D 游戏

* 平台跳跃
* 射击游戏
* 益智游戏

---

## 交互仿真

* 物理模拟
* 可视化演示

---

## 图形工具

* 绘图板
* 动画制作

---

# 20. 常见问题

---

## 1. 窗口无响应

原因：没有处理 QUIT 事件。

解决：

```python
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False
```

---

## 2. 图像不显示

原因：忘记 `screen.blit()` 或 `pygame.display.flip()`。

---

## 3. 音效不播放

检查：

```python
pygame.mixer.init()
sound = pygame.mixer.Sound('file.wav')
sound.play()
```

并确保文件存在。

---

## 4. 移动速度过快/过慢

使用帧率独立移动：

```python
dt = clock.tick(60) / 1000.0
velocity = 200  # 像素/秒
player.x += velocity * dt
```

---

# 21. 推荐学习路线

```text
安装与窗口创建
↓
事件处理（关闭、键盘、鼠标）
↓
绘制图形（矩形、圆形、图像）
↓
精灵与精灵组
↓
碰撞检测
↓
文本与字体
↓
声音播放
↓
完整游戏循环
↓
开发一个小游戏（如 Pong、贪吃蛇）
```

---

# 22. 推荐练习项目

## 初级

* 移动的方块
* 鼠标点击画点

---

## 中级

* 贪吃蛇
* 打砖块

---

## 高级

* 平台跳跃游戏
* 射击游戏（飞机大战）
* 粒子效果系统