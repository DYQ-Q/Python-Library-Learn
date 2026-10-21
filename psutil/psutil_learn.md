# 1. psutil 简介

psutil（process and system utilities）是 Python 中最常用的：

```text
跨平台系统监控与进程管理库
```

主要用于：

* CPU 使用率监控
* 内存与交换分区统计
* 磁盘分区与 I/O 信息
* 网络接口与连接状态
* 进程信息查询与管理
* 传感器与电池状态读取

与 os / subprocess 不同：

```text
os        ：基础系统接口，粒度粗，功能分散
subprocess：执行外部命令，解析开销大
psutil    ：统一 API，跨平台，返回结构化数据
```

例如，获取 CPU 使用率：

```python
import psutil
print(psutil.cpu_percent(interval=1))
```

输出：

```text
12.5
```

而用 `top` 命令需要解析文本输出，跨平台一致性差。

---

# 2. 安装

## 安装 psutil

```bash
pip install psutil
```

升级到最新版：

```bash
pip install psutil --upgrade
```

## 验证安装

```python
import psutil
print(psutil.__version__)
```

## 支持的平台

psutil 目前支持：

```text
Linux、Windows、macOS、FreeBSD、OpenBSD、NetBSD、Sun Solaris、AIX
```

Python 版本要求 **3.6+**（最后支持 Python 2.7 的是 psutil 6.1.1）。

---

# 3. psutil 的核心思想

psutil 的核心设计：

```text
统一 API + 跨平台抽象 + 结构化返回
```

三大特点：

```text
1. 统一接口：同一套函数在 Linux / Windows / macOS 上语义一致
2. 命名元组返回：所有函数返回具名元组，可按属性或索引访问
3. 异常驱动：进程消失、权限不足等情况以明确异常抛出
```

与命令行工具的对标：

```text
psutil 实现了 ps、top、lsof、netstat、ifconfig、df、free、kill、iostat 等工具的功能
```



---

# 4. 系统信息获取

## 4.1 CPU 信息

| 函数 | 说明 |
| ---- | ---- |
| `psutil.cpu_count()` | 逻辑 CPU 数量 |
| `psutil.cpu_count(logical=False)` | 物理核心数 |
| `psutil.cpu_percent(interval=1)` | 总体 CPU 使用率（阻塞采样 1 秒） |
| `psutil.cpu_percent(percpu=True)` | 每个核心的使用率列表 |
| `psutil.cpu_times()` | CPU 时间分布（user、system、idle 等） |
| `psutil.cpu_freq()` | CPU 频率（current、min、max） |
| `psutil.getloadavg()` | 系统负载均值（仅 Unix） |

```python
import psutil

print(psutil.cpu_count())                 # 8
print(psutil.cpu_count(logical=False))    # 4
print(psutil.cpu_percent(interval=1))     # 15.2
print(psutil.cpu_times().user)            # 用户态时间
print(psutil.cpu_freq().current)          # 当前频率 MHz
```

`cpu_times()` 返回的 `user`、`system`、`idle` 分别表示用户态、内核态和空闲时间。

---

## 4.2 内存信息

### 虚拟内存（物理 RAM）

```python
mem = psutil.virtual_memory()

print(mem.total)          # 总物理内存（字节）
print(mem.available)      # 可用内存
print(mem.used)           # 已用内存
print(mem.percent)        # 使用百分比
print(mem.free)           # 完全空闲内存
```

部分属性平台相关：

```text
buffers  ：仅 Linux
cached   ：仅 Linux
shared   ：仅 Linux
active   ：仅 Unix
inactive ：仅 Unix
```



### 交换分区

```python
swap = psutil.swap_memory()

print(swap.total)     # 交换区总量
print(swap.used)      # 已用
print(swap.percent)   # 使用百分比
print(swap.sin)       # 换入字节数（Unix）
print(swap.sout)      # 换出字节数（Unix）
```



---

## 4.3 磁盘信息

### 分区与使用率

```python
# 所有已挂载分区
for part in psutil.disk_partitions():
    print(part.device, part.mountpoint, part.fstype)

# 指定路径的使用率
usage = psutil.disk_usage("/")
print(usage.total)     # 总空间
print(usage.used)      # 已用空间
print(usage.free)      # 可用空间
print(usage.percent)   # 使用百分比
```



### 磁盘 I/O

```python
io = psutil.disk_io_counters()

print(io.read_count)     # 读取次数
print(io.write_count)    # 写入次数
print(io.read_bytes)     # 读取字节数
print(io.write_bytes)    # 写入字节数
print(io.read_time)      # 读取耗时（ms）
print(io.write_time)     # 写入耗时（ms）

# 按磁盘分区统计
per_disk = psutil.disk_io_counters(perdisk=True)
```



---

## 4.4 网络信息

### 全局网络 I/O

```python
net = psutil.net_io_counters()

print(net.bytes_sent)      # 发送字节数
print(net.bytes_recv)      # 接收字节数
print(net.packets_sent)    # 发送包数
print(net.packets_recv)    # 接收包数
print(net.errin)           # 入站错误
print(net.errout)          # 出站错误
print(net.dropin)          # 入站丢包
print(net.dropout)         # 出站丢包
```

按网卡统计：

```python
per_nic = psutil.net_io_counters(pernic=True)
```



### 网络接口地址与状态

```python
# 所有网卡的 IP / MAC
addrs = psutil.net_if_addrs()

# 网卡状态（是否 up、速率、MTU）
stats = psutil.net_if_stats()
eth0 = stats.get("eth0")
if eth0:
    print(eth0.isup, eth0.speed, eth0.mtu)
```



### 网络连接（socket 级）

```python
conns = psutil.net_connections(kind="inet")   # IPv4/IPv6
# kind 可选："tcp"、"udp"、"inet"、"all"

for c in conns:
    print(c.laddr, c.raddr, c.status, c.pid)
```

常配合状态常量过滤监听端口：

```python
for conn in psutil.net_connections(kind="inet"):
    if conn.status == psutil.CONN_LISTEN:
        ...
```



---

# 5. 进程管理

## 5.1 Process 类基础

### 创建 Process 对象

```python
import psutil

# 当前进程
p = psutil.Process()

# 指定 PID
p = psutil.Process(pid=1234)
```



### 常用属性与方法

```python
p.pid                   # 进程 ID
p.ppid()                # 父进程 ID
p.name()                # 进程名
p.exe()                 # 可执行文件路径
p.cwd()                 # 当前工作目录
p.cmdline()             # 命令行列表
p.status()              # 状态（running / sleeping / zombie 等）
p.username()            # 所属用户名
p.create_time()         # 创建时间戳
p.cpu_percent(interval=1)  # CPU 使用率
p.cpu_times()           # CPU 时间（user / system）
p.memory_info()         # 内存信息
p.memory_info().rss     # 常驻内存大小
p.memory_percent()      # 占总内存百分比
p.num_threads()         # 线程数
p.io_counters()         # I/O 计数器
```



`oneshot()` 上下文管理器可以在一次性读取多个属性时显著提速：

```python
p = psutil.Process(pid=1234)
with p.oneshot():
    print(p.name())
    print(p.cpu_times())
    print(p.memory_info())
```



---

## 5.2 遍历所有进程

### 推荐方式：process_iter()

```python
import psutil

for proc in psutil.process_iter(["pid", "name", "username"]):
    print(proc.info)
```

输出：

```text
{'pid': 1, 'name': 'systemd', 'username': 'root'}
{'pid': 2, 'name': 'kthreadd', 'username': 'root'}
...
```

`process_iter()` 是遍历进程的首选方式，相比 `psutil.pids()` 更能规避 PID 复用带来的竞态问题，并且每个 `Process` 实例在内部缓存中只创建一次。

### 过滤示例

```python
# 按名称过滤
for proc in psutil.process_iter(["pid", "name"]):
    if "python" in proc.info["name"].lower():
        print(proc.info)

# 按内存占用过滤（带异常保护）
for proc in psutil.process_iter(["pid", "name", "memory_percent"]):
    try:
        if proc.info["memory_percent"] > 5.0:
            print(f"{proc.info['name']}: {proc.info['memory_percent']:.1f}%")
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        pass
```



### 字典式收集

```python
procs = {p.pid: p.info for p in psutil.process_iter(["name", "username"])}
```



---

## 5.3 进程操作

### 终止与杀死

```python
p = psutil.Process(1234)

p.terminate()   # 优雅终止，Unix 上对应 SIGTERM
p.wait(timeout=3)  # 等待进程退出

p.kill()        # 强制杀死，Unix 上对应 SIGKILL
```

`terminate()` 允许进程清理资源，`kill()` 不可拦截。

### 挂起与恢复

```python
p.suspend()     # 暂停进程（Unix: SIGSTOP）
p.resume()      # 恢复进程（Unix: SIGCONT）
```



### 等待多个进程

```python
procs = [psutil.Process(pid) for pid in [1001, 1002, 1003]]

# 先尝试优雅终止，超时后强制杀死
for p in procs:
    p.terminate()

gone, alive = psutil.wait_procs(procs, timeout=3)
for p in alive:
    p.kill()
```

`wait_procs()` 返回 `(gone, alive)` 二元组，不会因超时抛异常，适合批量管理。

---

# 6. 其他常用功能

## 6.1 传感器与电池（平台相关）

```python
# 温度传感器（Linux）
for name, entries in psutil.sensors_temperatures().items():
    for entry in entries:
        print(entry.label, entry.current, entry.high, entry.critical)

# 风扇转速（Linux）
psutil.sensors_fans()

# 电池（笔记本）
battery = psutil.sensors_battery()
if battery:
    print(battery.percent, battery.secsleft, battery.power_plugged)
```



## 6.2 启动时间与登录用户

```python
import datetime

boot = psutil.boot_time()
print(datetime.datetime.fromtimestamp(boot))

for user in psutil.users():
    print(user.name, user.terminal, user.host, user.started)
```



## 6.3 系统标识常量

```python
psutil.LINUX       # 是否 Linux
psutil.WINDOWS     # 是否 Windows
psutil.MACOS       # 是否 macOS
psutil.BSD         # 是否 BSD
psutil.version_info
```



---

# 7. 常见异常与处理

psutil 的多数函数在特定情况下会抛出异常：

| 异常 | 触发场景 |
| ---- | -------- |
| `psutil.NoSuchProcess` | 进程已不存在（PID 已退出或被复用） |
| `psutil.AccessDenied` | 权限不足，无法读取进程信息 |
| `psutil.ZombieProcess` | 进程处于僵尸状态（Unix） |
| `psutil.TimeoutExpired` | `wait()` / `wait_procs()` 等待超时 |

处理方式：

```python
for proc in psutil.process_iter(["pid", "name"]):
    try:
        print(proc.info["pid"], proc.info["name"])
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        continue
```

对于 `AccessDenied`，也可以在 `process_iter()` 中通过 `attrs` 预取属性，psutil 会自动跳过无权限的进程。

---

# 8. 综合示例

## 实时监控 CPU 与内存

```python
import psutil
import time

while True:
    cpu = psutil.cpu_percent(interval=2)
    mem = psutil.virtual_memory()
    print(f"CPU: {cpu}% | RAM: {mem.percent}% "
          f"({mem.used / 1024**3:.1f}/{mem.total / 1024**3:.1f} GB)")
```



## 找出内存占用最高的 5 个进程

```python
import psutil

procs = []
for p in psutil.process_iter(["pid", "name", "memory_percent"]):
    procs.append(p.info)

top5 = sorted(procs, key=lambda x: x["memory_percent"] or 0, reverse=True)[:5]

for p in top5:
    print(f"PID {p['pid']:>6} | {p['name']:25} | {p['memory_percent']:.1f}%")
```



## 磁盘空间告警

```python
import psutil

for part in psutil.disk_partitions():
    usage = psutil.disk_usage(part.mountpoint)
    if usage.percent > 90:
        print(f"WARNING: {part.mountpoint} 已使用 {usage.percent}%")
```



---

# 9. 常见问题

## 1. AccessDenied 频繁出现

```text
原因：普通用户无法读取系统进程的详细信息
解决：
• 以管理员 / root 运行（不推荐全面提权）
• 在 process_iter 中预取属性，自动跳过无权限进程
• 用 try/except 捕获并忽略
```



## 2. Process 对象操作时报 NoSuchProcess

```text
原因：进程在获取信息和操作之间退出了
解决：始终用 try/except 包裹，或使用 process_iter 遍历
```

## 3. cpu_percent 首次调用返回 0.0

```text
原因：interval 未设置时，首次调用没有参照基准
解决：传入 interval=1 或先调用一次进行“预热”
```

## 4. 部分属性在某些平台为 0 或不可用

```text
psutil 的许多属性是平台相关的（如 Linux 的 buffers/cached、Unix 的 getloadavg）
使用前可先检查平台常量，或使用 getattr 提供默认值
```



---

# 10. 推荐学习路线

```text
安装与版本验证
↓
CPU 信息（cpu_count、cpu_percent、cpu_times）
↓
内存信息（virtual_memory、swap_memory）
↓
磁盘信息（disk_usage、disk_io_counters）
↓
网络信息（net_io_counters、net_connections）
↓
Process 类基础属性
↓
process_iter 遍历与过滤
↓
进程操作（terminate、kill、suspend、resume）
↓
异常处理与平台差异
↓
综合监控脚本
```

---

# 11. 推荐练习项目

## 初级

* 打印系统 CPU、内存、磁盘的基本信息
* 列出当前所有 Python 进程

---

## 中级

* 实时监控脚本（CPU / 内存 / 网络每秒刷新）
* 按内存或 CPU 排序的进程 Top N
* 磁盘使用率超过阈值时发送提醒

---

## 高级

* 进程守护与自动重启（监控目标进程存活状态）
* 跨平台系统信息采集工具
* 结合 `curses` 或 `rich` 构建终端系统监控面板

---

# 12. 核心 API 速查

```python
import psutil

# CPU
psutil.cpu_count(logical=False)
psutil.cpu_percent(interval=1, percpu=True)
psutil.cpu_times()
psutil.cpu_freq()

# 内存
psutil.virtual_memory()
psutil.swap_memory()

# 磁盘
psutil.disk_partitions()
psutil.disk_usage("/")
psutil.disk_io_counters(perdisk=True)

# 网络
psutil.net_io_counters(pernic=True)
psutil.net_if_addrs()
psutil.net_if_stats()
psutil.net_connections(kind="inet")

# 进程
psutil.pids()
psutil.process_iter(["pid", "name", "username"])
psutil.Process(pid)
p.name() / p.cpu_percent() / p.memory_info()
p.terminate() / p.kill() / p.wait()
p.suspend() / p.resume()

# 其他
psutil.boot_time()
psutil.users()
psutil.sensors_battery()
```