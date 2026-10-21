# watchdog 学习笔记

> 目录：[1. 简介](#1-watchdog-简介) | [2. 安装](#2-安装) | [3. 核心概念](#3-核心概念) | [4. 第一个监控程序](#4-第一个监控程序) | [5. 事件详解](#5-事件处理详解) | [6. 模式匹配](#6-模式匹配只监控指定文件) | [7. 多目录监控](#7-多目录与递归监控) | [8. 常见坑](#8-常见坑与解决) | [9. 防抖](#9-事件防抖) | [10. 实战案例](#10-实战案例) | [11. FAQ](#11-常见问题-faq) | [12. 速查表](#12-速查表)

---

# 1. watchdog 简介

watchdog 是 Python 中最常用的：

```text
文件系统监控库（File System Watcher）
```

主要用于：

* 监控文件 / 文件夹的新建、修改、删除、重命名
* 实时响应文件变化（文件一到就处理，无需轮询）
* 自动整理下载文件夹、监控日志、热加载配置文件
* 监控上传目录自动处理新文件

与"轮询"方案对比：

```text
轮询 os.listdir : 简单，但费 CPU、响应慢、容易漏事件
watchdog        : 事件驱动，由操作系统通知，实时且高效
```

工作原理（watchdog 自动选择各平台的原生 API）：

```text
Windows : ReadDirectoryChangesW
Linux   : inotify
macOS   : FSEvents / kqueue
```

> 💡 所以 watchdog 性能很好，但不同平台的行为细节略有差异（见第 11 节）。

---

# 2. 安装

## 安装 watchdog

```bash
pip install watchdog
```

## 测试安装

```python
import watchdog
print(watchdog.__version__)   # 例如 4.0.1
```

---

# 3. 核心概念

watchdog 的对象结构（理解后 everything 就通了）：

```text
Observer（观察者 = 监控引擎，后台线程）
 ├── Schedule（监控计划 = "监控哪个路径，事件发给谁"）
 └── FileSystemEventHandler（事件处理器 = 收到事件后做什么）
```

三个核心角色：

| 角色 | 类 | 说明 |
|------|----|------|
| 观察者 | `Observer` | 后台线程，负责接收系统级文件事件并分发 |
| 事件处理器 | `FileSystemEventHandler`（或其子类） | 重写 `on_xxx` 方法，定义收到事件后的行为 |
| 监控计划 | `observer.schedule(handler, path, recursive)` | 把"处理器"和"监控路径"绑定起来 |

四种事件回调方法（都是可选重写）：

| 方法 | 触发时机 |
|------|----------|
| `on_created` | 文件 / 文件夹被创建 |
| `on_modified` | 文件 / 文件夹被修改 |
| `on_deleted` | 文件 / 文件夹被删除 |
| `on_moved` | 文件 / 文件夹被移动或重命名 |

事件对象 `event` 的两个常用属性：

```text
event.is_directory : 是否是文件夹（bool）
event.src_path     : 事件源的完整路径（str）
event.dest_path    : 移动/重命名的目标路径（仅 on_moved 有）
```

---

# 4. 第一个监控程序

监控当前目录，打印所有文件变化：

```python
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class Handler(FileSystemEventHandler):
    """自定义事件处理器：重写关心的 on_xxx 方法"""

    def on_created(self, event):
        print(f"[新建] {event.src_path}")

    def on_modified(self, event):
        print(f"[修改] {event.src_path}")

    def on_deleted(self, event):
        print(f"[删除] {event.src_path}")

    def on_moved(self, event):
        print(f"[移动] {event.src_path} -> {event.dest_path}")


if __name__ == "__main__":
    observer = Observer()
    # recursive=True 表示同时监控所有子文件夹
    observer.schedule(Handler(), path=".", recursive=True)
    observer.start()          # 启动后台监控线程（非阻塞）
    print("监控已启动，Ctrl+C 退出...")

    try:
        while True:           # 主线程保持运行
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()       # 停止监控
    observer.join()           # 等待线程结束
```

运行后手动在目录里新建 / 修改 / 删除文件，就能看到输出。

固定结构口诀：

```text
① 写 Handler（重写 on_xxx）
② 创建 Observer
③ schedule 绑定（handler + path）
④ observer.start() 启动
⑤ while True 保持主线程
⑥ finally 里 stop() + join()
```

---

# 5. 事件处理详解

## 5.1 只重写需要的事件

`FileSystemEventHandler` 的四个方法都有默认空实现，**只重写关心的即可**：

```python
from watchdog.events import FileSystemEventHandler


class Handler(FileSystemEventHandler):
    def on_created(self, event):     # 只关心"新建"事件
        print(f"新文件: {event.src_path}")
```

## 5.2 过滤文件夹事件

绝大多数场景只关心文件，先过滤目录：

```python
def on_created(self, event):
    if event.is_directory:           # 是文件夹就忽略
        return
    print(f"新文件: {event.src_path}")
```

## 5.3 提取文件名和扩展名

```python
import os
from pathlib import Path

def on_created(self, event):
    filename = os.path.basename(event.src_path)        # 方式一
    filename = Path(event.src_path).name               # 方式二（推荐）
    suffix = Path(event.src_path).suffix               # 扩展名，如 ".csv"
    print(f"文件名: {filename}, 类型: {suffix}")
```

## 5.4 四种事件完整示例

```python
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from pathlib import Path


class Handler(FileSystemEventHandler):
    def on_created(self, event):
        kind = "文件夹" if event.is_directory else "文件"
        print(f"[创建] {kind}: {event.src_path}")

    def on_modified(self, event):
        if event.is_directory:
            return
        print(f"[修改] 文件: {event.src_path}")

    def on_deleted(self, event):
        kind = "文件夹" if event.is_directory else "文件"
        print(f"[删除] {kind}: {event.src_path}")

    def on_moved(self, event):
        # 移动和重命名都会触发 on_moved
        print(f"[移动] {event.src_path} -> {event.dest_path}")


observer = Observer()
observer.schedule(Handler(), path=".", recursive=False)
observer.start()
time.sleep(30)        # 监控 30 秒
observer.stop()
observer.join()
```

## 5.5 on_any_event：统一入口

不想分方法处理时，可以只重写通用回调（此时四个 on_xxx 不用写）：

```python
from watchdog.events import FileSystemEventHandler


class Handler(FileSystemEventHandler):
    def on_any_event(self, event):
        # 所有事件都会进这里，用 event.event_type 区分类型
        # event.event_type: 'created' / 'modified' / 'deleted' / 'moved'
        if event.is_directory:
            return
        print(f"[{event.event_type}] {event.src_path}")
```

> 💡 选择建议：事件类型少用 `on_any_event` 统一分发；逻辑复杂时分开重写 `on_xxx` 更清晰。

---

# 6. 模式匹配（只监控指定文件）

`PatternMatchingEventHandler` 可以按扩展名 / 通配符过滤，不用手写判断：

```python
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler


class CsvHandler(PatternMatchingEventHandler):
    def __init__(self):
        # patterns      : 只处理匹配的（支持 * 通配符）
        # ignore_patterns: 忽略匹配的（如临时文件）
        # ignore_directories: 忽略所有文件夹事件
        # case_sensitive: 大小写敏感（Windows 文件名常不区分，设 False）
        super().__init__(
            patterns=["*.csv", "*.xlsx"],
            ignore_patterns=["*.tmp", "~$*", ".~*"],   # 忽略 Excel 临时文件
            ignore_directories=True,
            case_sensitive=False,
        )

    def on_created(self, event):
        print(f"新的表格文件: {event.src_path}")

    def on_modified(self, event):
        print(f"表格被修改: {event.src_path}")


observer = Observer()
observer.schedule(CsvHandler(), path="./data", recursive=True)
observer.start()
```

常用通配符：

```text
*.csv        所有 csv 文件
*.log        所有日志文件
report*.*    report 开头的文件
*            所有文件（默认）
```

---

# 7. 多目录与递归监控

## 7.1 recursive：是否递归子文件夹

```python
observer.schedule(handler, path="./data", recursive=True)   # 含所有子文件夹
observer.schedule(handler, path="./data", recursive=False)  # 只监控该层
```

## 7.2 一个 Observer 监控多个目录

`schedule()` 可以调用多次，每个目录可以配不同的处理器：

```python
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class Handler(FileSystemEventHandler):
    def on_created(self, event):
        print(f"[新建] {event.src_path}")


class LogHandler(FileSystemEventHandler):
    def on_modified(self, event):
        print(f"[日志更新] {event.src_path}")


observer = Observer()
observer.schedule(Handler(), path="./downloads", recursive=True)   # 目录 1
observer.schedule(LogHandler(), path="./logs", recursive=False)    # 目录 2
observer.start()
```

## 7.3 目录树监控示意图

```text
./downloads          ← path 指定
 ├── a.csv           ✅ recursive=True/False 都监控
 └── sub/            ← 子文件夹
      └── b.csv      ✅ True 才监控 | ❌ False 不管
```

---

# 8. 常见坑与解决

## 坑 1：on_modified 触发多次

一次保存操作，回调可能被触发 2~3 次（不同软件行为不同）：

```text
现象: 保存一次文件 → on_modified 打印了 2 次
原因: 编辑器先写临时文件再替换、或多次刷新元数据
     （记事本/VS Code/Excel 都有此现象，属于正常系统行为）
解决: 事件防抖（见第 9 节）
```

## 坑 2：收到编辑器 / 系统的临时文件事件

```text
VS Code  : 保存时会产生临时文件再替换
Excel    : 打开文件时生成 ~$xxx.xlsx 锁文件
解决方案 : PatternMatchingEventHandler 的 ignore_patterns（见第 6 节）
```

```python
super().__init__(
    patterns=["*.csv"],
    ignore_patterns=["*.tmp", "~$*", ".~*", "*.swp", "*~"],  # 过滤临时文件
    ignore_directories=True,
)
```

## 坑 3：文件刚创建就被处理，但内容还没写完

典型场景：程序正在复制一个 500MB 的大文件到监控目录，
`on_created` 立刻触发，此时文件**不完整**，直接读取会出错：

```python
# 错误做法
def on_created(self, event):
    with open(event.src_path) as f:     # ❌ 文件可能还没复制完
        data = f.read()

# 正确做法：等待文件"稳定"（大小不再变化）再处理
import time


def wait_until_stable(path, interval=0.5, timeout=30):
    """等待文件大小在 interval 秒内不再变化"""
    last_size = -1
    start = time.time()
    while time.time() - start < timeout:
        try:
            size = Path(path).stat().st_size
        except FileNotFoundError:
            time.sleep(interval)
            continue
        if size == last_size and size > 0:
            return True                 # 大小稳定，可以处理了
        last_size = size
        time.sleep(interval)
    return False


def on_created(self, event):
    if event.is_directory:
        return
    if wait_until_stable(event.src_path):
        print(f"文件已就绪: {event.src_path}")   # 此时再安全处理
```

## 坑 4：事件处理里抛异常 → 监控静默失效

`Observer` 的后台线程里抛异常可能导致该 watch 停止工作且**不报错**：

```python
# 错误做法：处理逻辑裸奔
def on_created(self, event):
    process(event.src_path)            # ❌ 一旦抛异常，后续事件可能收不到

# 正确做法：所有事件处理都套 try/except
import traceback


def on_created(self, event):
    try:
        process(event.src_path)
    except Exception:
        traceback.print_exc()          # 至少把错误打出来，方便排查
```

---

# 9. 事件防抖

## 9.1 防抖思想

```text
问题 : 一次保存 → on_modified 触发多次
思路 : 事件到达后不立即处理，等一小段时间；
      若期间又有新事件（同一文件），就重置计时器。
      只有"安静"超过 N 秒才真正处理一次。
```

```text
事件流:  [修改][修改][修改] ...... (2秒安静) ...... 处理 ✅
                ↑ 每次重置计时器        ↑ 只处理这一次
```

## 9.2 实现方案一：时间窗口去重（简单）

记录每个文件上次处理时间，间隔太短的事件直接丢弃：

```python
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

DEBOUNCE_SECONDS = 1.0     # 1 秒内重复事件忽略


class DebounceHandler(FileSystemEventHandler):
    def __init__(self):
        self._last_processed = {}    # {路径: 上次处理时间}

    def _should_process(self, path):
        now = time.time()
        last = self._last_processed.get(path, 0)
        if now - last < DEBOUNCE_SECONDS:
            return False             # 间隔太短，丢弃
        self._last_processed[path] = now
        return True

    def on_modified(self, event):
        if event.is_directory:
            return
        if self._should_process(event.src_path):
            print(f"处理: {event.src_path}")    # 真正的处理逻辑
```

> ⚠️ 缺点：字典会一直增长，长期运行要定期清理旧记录。

## 9.3 实现方案二：Timer 延迟处理（推荐）

用线程定时器，"最后一个事件"到达后才处理：

```python
import threading
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

WAIT_SECONDS = 1.0         # 安静 1 秒后才处理


class TimerDebounceHandler(FileSystemEventHandler):
    def __init__(self):
        self._timers = {}            # {路径: Timer 对象}

    def on_modified(self, event):
        if event.is_directory:
            return
        path = event.src_path
        # 取消该文件上一次的定时器
        old = self._timers.pop(path, None)
        if old:
            old.cancel()
        # 重新启动定时器：WAIT_SECONDS 秒后执行处理
        t = threading.Timer(WAIT_SECONDS, self._process, args=(path,))
        self._timers[path] = t
        t.start()

    def _process(self, path):
        self._timers.pop(path, None)
        print(f"处理: {path}")       # 真正的处理逻辑写在这里
```

两种方案对比：

```text
时间窗口去重 : 简单直接，响应快，但可能漏掉"最后那次"修改
Timer 延迟   : 保证处理的是最终状态，延迟 N 秒，更可靠（推荐）
```

---

# 10. 实战案例

## 案例 1：自动整理下载文件夹（新文件按类型归类）

```python
import shutil
import time
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

DOWNLOAD_DIR = Path(r"C:\Users\你\Downloads")     # 改成自己的下载目录
RULES = {
    "图片": [".jpg", ".png", ".gif", ".webp"],
    "文档": [".pdf", ".docx", ".xlsx", ".pptx", ".txt"],
    "安装包": [".exe", ".msi", ".zip", ".rar", ".7z"],
    "视频": [".mp4", ".mkv", ".avi"],
}


class OrganizerHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return

        src = Path(event.src_path)

        # 按扩展名找目标文件夹
        target_dir = None
        for folder, exts in RULES.items():
            if src.suffix.lower() in exts:
                target_dir = DOWNLOAD_DIR / folder
                break
        if target_dir is None:          # 不在规则里的类型不处理
            return

        target_dir.mkdir(exist_ok=True)

        # 避免把已归类文件再次移动
        if target_dir in src.parents:
            return

        try:
            shutil.move(str(src), target_dir / src.name)
            print(f"已归类: {src.name} -> {folder}/")
        except Exception as e:
            print(f"移动失败: {e}")


if __name__ == "__main__":
    observer = Observer()
    observer.schedule(OrganizerHandler(), str(DOWNLOAD_DIR), recursive=False)
    observer.start()
    print("下载文件夹自动整理运行中... Ctrl+C 退出")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
```

## 案例 2：监控数据目录，新 CSV 到达后自动处理

综合运用：模式匹配 + 等待文件稳定 + 异常保护：

```python
import time
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler


def wait_until_stable(path, interval=0.5, timeout=30):
    last_size, start = -1, time.time()
    while time.time() - start < timeout:
        try:
            size = Path(path).stat().st_size
        except FileNotFoundError:
            time.sleep(interval)
            continue
        if size == last_size and size > 0:
            return True
        last_size = size
        time.sleep(interval)
    return False


class DataHandler(PatternMatchingEventHandler):
    def __init__(self):
        super().__init__(
            patterns=["*.csv"],
            ignore_patterns=["*.tmp", "~$*"],
            ignore_directories=True,
            case_sensitive=False,
        )

    def on_created(self, event):
        try:
            print("发现新数据文件，等待写入完成...")
            if wait_until_stable(event.src_path):
                self.import_csv(event.src_path)
        except Exception:
            import traceback
            traceback.print_exc()

    def import_csv(self, path):
        """业务逻辑：解析 CSV 并入库/统计"""
        import csv
        with open(path, newline="", encoding="utf-8-sig") as f:
            rows = list(csv.reader(f))
        print(f"导入完成: {len(rows)} 行")


observer = Observer()
observer.schedule(DataHandler(), path="./data", recursive=True)
observer.start()
while True:
    time.sleep(1)
```

## 案例 3：配置文件热加载（修改配置立即生效）

```python
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import json
from pathlib import Path


class ConfigReloader(FileSystemEventHandler):
    def __init__(self, config_path):
        self.config_path = config_path
        self.config = self.load()

    def load(self):
        with open(self.config_path, encoding="utf-8") as f:
            return json.load(f)

    def on_modified(self, event):
        if Path(event.src_path).name == Path(self.config_path).name:
            self.config = self.load()
            print(f"配置已热加载: {self.config}")


reloader = ConfigReloader("config.json")

observer = Observer()
observer.schedule(reloader, path=".", recursive=False)
observer.start()

# 其他代码随时用 reloader.config 读最新配置
```

---

# 11. 常见问题 FAQ

**Q1：程序启动后没有任何事件触发？**

```text
检查清单:
① 是否调用了 observer.start()
② 主线程是否保持运行（while True + sleep）
③ path 路径是否写对（建议用绝对路径）
④ 是否被 PatternMatchingEventHandler 的 patterns 过滤掉了
```

**Q2：能监控网络驱动器 / U 盘 / NAS 吗？**

```text
系统 API 对网络路径支持不稳定，可能收不到事件。
解决: 用 PollingObserver（轮询式观察者，不依赖系统 API）

from watchdog.observers.polling import PollingObserver

observer = PollingObserver(timeout=5)   # 每 5 秒扫描一次
# 其余用法与 Observer 完全相同
```

**Q3：监控子文件夹里新建的文件夹，需要重新 schedule 吗？**

```text
不需要。recursive=True 时，watchdog 会自动监控后新建的子目录。
```

**Q4：事件回调在哪个线程执行？阻塞主线程吗？**

```text
事件回调在 Observer 的后台线程执行，不阻塞主线程。
但注意: 事件是逐个分发的，如果某个回调处理很慢（如 sleep(10)），
会阻塞后续事件的处理 → 耗时任务建议丢给新线程/队列处理。
```

**Q5：如何在收到事件时退出监控 / 结束程序？**

```python
observer.stop()      # 在回调里直接调用即可（线程安全）
```

---

# 12. 速查表

## 核心 API

| 代码 | 作用 |
|------|------|
| `Observer()` | 创建观察者 |
| `observer.schedule(handler, path, recursive=True)` | 绑定监控 |
| `observer.start()` / `stop()` / `join()` | 启动 / 停止 / 等待 |
| `FileSystemEventHandler` | 基础事件处理器（重写 on_xxx） |
| `PatternMatchingEventHandler(...)` | 带通配符过滤的处理器 |
| `PollingObserver(timeout=5)` | 轮询式观察者（网络路径用） |

## 事件回调

| 方法 | 事件 |
|------|------|
| `on_created(event)` | 创建 |
| `on_modified(event)` | 修改 |
| `on_deleted(event)` | 删除 |
| `on_moved(event)` | 移动 / 重命名 |
| `on_any_event(event)` | 所有事件（统一入口） |

## 事件对象属性

| 属性 | 说明 |
|------|------|
| `event.src_path` | 源路径 |
| `event.dest_path` | 目标路径（仅 moved） |
| `event.is_directory` | 是否文件夹 |
| `event.event_type` | 事件类型字符串 |

## 标准模板（背下来直接用）

```python
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class Handler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        try:
            print(f"处理: {event.src_path}")
        except Exception:
            import traceback
            traceback.print_exc()


observer = Observer()
observer.schedule(Handler(), path=".", recursive=True)
observer.start()
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()
```

---