import psutil
import time

while True:
    cpu = psutil.cpu_percent(interval=2) # 2秒内CPU使用率
    mem = psutil.virtual_memory() # 虚拟内存信息
    print(f"CPU: {cpu}% | RAM: {mem.percent}% "
          f"({mem.used / 1024**3:.1f}/{mem.total / 1024**3:.1f} GB)")