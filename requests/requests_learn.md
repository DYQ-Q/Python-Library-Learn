# 1. Requests 库简介

Requests 是 Python 中最常用的：

```text
HTTP 请求库
```

基于 urllib3，提供了更简洁、人性化的 API，被称为 "HTTP for Humans"。

主要用于：

* 发送 GET / POST / PUT / DELETE 等 HTTP 请求
* 处理请求参数、请求头、Cookie
* 处理响应数据（JSON、文本、二进制）
* 文件上传与下载
* 会话管理（Session）
* 处理代理、SSL 验证、超时

与 urllib 对比：

```text
urllib：Python 内置，但 API 繁琐
Requests：第三方库，API 简洁直观
```

例如：

urllib：

```python
import urllib.request
import urllib.parse

data = urllib.parse.urlencode({'key': 'value'}).encode()
req = urllib.request.Request('http://httpbin.org/post', data=data)
with urllib.request.urlopen(req) as response:
    print(response.read().decode())
```

Requests：

```python
import requests

response = requests.post('http://httpbin.org/post', data={'key': 'value'})
print(response.text)
```

---

# 2. 安装

## 安装 Requests

```bash
pip install requests
```

---

## 测试安装

```python
import requests

print(requests.__version__)
```

---

# 3. 核心概念

Requests 的核心思想：

```text
封装 HTTP 请求的所有细节
提供统一的、面向对象的 API
```

请求流程：

```text
构造请求 → 发送请求 → 接收响应 → 处理响应
```

---

# 4. 发送 GET 请求

## 4.1 基础 GET

```python
import requests

response = requests.get('https://api.github.com')
print(response.status_code)      # 200
print(response.text)             # 响应内容（字符串）
```

---

## 4.2 带参数的 GET（查询字符串）

```python
params = {'q': 'python', 'page': 1}
response = requests.get('https://api.github.com/search/repositories', params=params)

print(response.url)  # 自动编码为 https://api.github.com/search/repositories?q=python&page=1
print(response.json())  # 解析为 JSON
```

---

## 4.3 获取响应内容

| 属性/方法 | 说明 |
| --------- | ---- |
| `response.text` | 响应内容（字符串，自动解码） |
| `response.content` | 响应内容（字节） |
| `response.json()` | 解析为 JSON（dict/list） |
| `response.raw` | 原始 socket 流（需设置 stream=True） |

---

## 4.4 响应状态码

```python
print(response.status_code)          # 200
print(response.reason)               # 'OK'
response.raise_for_status()          # 状态码非 2xx 时抛出异常
```

---

## 4.5 响应头

```python
print(response.headers)              # 所有头（不区分大小写）
print(response.headers['Content-Type'])
print(response.headers.get('content-type'))
```

---

# 5. 发送 POST 请求

## 5.1 表单数据（application/x-www-form-urlencoded）

```python
data = {'username': 'admin', 'password': '123456'}
response = requests.post('https://httpbin.org/post', data=data)
print(response.json())
```

---

## 5.2 JSON 数据（application/json）

```python
import json

payload = {'key1': 'value1', 'key2': 'value2'}
response = requests.post('https://httpbin.org/post', json=payload)
# 或
response = requests.post('https://httpbin.org/post', data=json.dumps(payload), headers={'Content-Type': 'application/json'})
print(response.json())
```

---

## 5.3 文件上传

```python
files = {'file': open('report.txt', 'rb')}
response = requests.post('https://httpbin.org/post', files=files)

# 指定文件名和 MIME 类型
files = {'file': ('report.pdf', open('report.pdf', 'rb'), 'application/pdf')}
response = requests.post('https://httpbin.org/post', files=files)
```

---

# 6. 请求头与自定义 Headers

```python
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'Authorization': 'Bearer your_token',
    'Accept': 'application/json'
}
response = requests.get('https://api.github.com/user', headers=headers)
```

---

# 7. Cookie 处理

## 7.1 手动设置 Cookie

```python
cookies = {'sessionid': 'abcdef123456'}
response = requests.get('https://example.com', cookies=cookies)
```

---

## 7.2 从响应中获取 Cookie

```python
response = requests.get('https://httpbin.org/cookies/set?name=value')
print(response.cookies)            # <RequestsCookieJar>
print(response.cookies['name'])    # 'value'
```

---

## 7.3 跨请求保持 Cookie（Session）

使用 `Session` 对象会自动管理 Cookie（见第 10 节）。

---

# 8. 超时设置

```python
# 连接超时和读取超时（秒）
response = requests.get('https://api.github.com', timeout=5)

# 分别指定连接超时和读取超时
response = requests.get('https://api.github.com', timeout=(3.05, 10))
```

超时异常：

```python
import requests
from requests.exceptions import Timeout

try:
    response = requests.get('https://httpbin.org/delay/3', timeout=1)
except Timeout:
    print("请求超时")
```

---

# 9. 代理设置

## 9.1 HTTP/HTTPS 代理

```python
proxies = {
    'http': 'http://127.0.0.1:8080',
    'https': 'http://127.0.0.1:8080',
}
response = requests.get('https://api.github.com', proxies=proxies)
```

---

## 9.2 带认证的代理

```python
proxies = {
    'http': 'http://user:pass@127.0.0.1:8080',
    'https': 'https://user:pass@127.0.0.1:8080',
}
```

---

# 10. Session 会话对象

## 10.1 保持 Cookie 和持久连接

```python
session = requests.Session()
session.get('https://httpbin.org/cookies/set?session=abc')
response = session.get('https://httpbin.org/cookies')
print(response.json())   # {'cookies': {'session': 'abc'}}
```

---

## 10.2 设置默认 Headers

```python
session = requests.Session()
session.headers.update({'User-Agent': 'MyApp/1.0'})
session.get('https://httpbin.org/headers')  # 自动携带该 User-Agent
```

---

## 10.3 设置默认参数

```python
session = requests.Session()
session.params = {'token': '123456'}
session.get('https://httpbin.org/get')   # 自动添加 ?token=123456
```

---

# 11. SSL 证书验证

## 11.1 默认验证（推荐）

```python
response = requests.get('https://api.github.com')   # 自动验证证书
```

---

## 11.2 忽略 SSL 验证（不推荐）

```python
response = requests.get('https://self-signed.badssl.com', verify=False)
```

---

## 11.3 使用自定义证书

```python
response = requests.get('https://example.com', verify='/path/to/cert.pem')
```

---

# 12. 文件下载（流式）

```python
url = 'https://www.python.org/static/img/python-logo.png'
response = requests.get(url, stream=True)

with open('logo.png', 'wb') as f:
    for chunk in response.iter_content(chunk_size=8192):
        f.write(chunk)
```

---

# 13. 重定向处理

默认自动跟随重定向（状态码 301/302）：

```python
response = requests.get('http://github.com')
print(response.url)                 # 最终重定向后的 URL
print(response.history)             # 重定向历史列表
```

禁止自动重定向：

```python
response = requests.get('http://github.com', allow_redirects=False)
print(response.status_code)         # 301
```

---

# 14. 事件钩子（Hook）

```python
def print_url(response, *args, **kwargs):
    print("请求URL:", response.url)

response = requests.get('https://api.github.com', hooks={'response': print_url})
```

---

# 15. 异常处理

常见异常：

| 异常 | 说明 |
| ---- | ---- |
| `requests.exceptions.Timeout` | 超时 |
| `requests.exceptions.ConnectionError` | 网络连接错误 |
| `requests.exceptions.HTTPError` | HTTP 错误状态码（需配合 `raise_for_status()`） |
| `requests.exceptions.ProxyError` | 代理错误 |
| `requests.exceptions.SSLError` | SSL 证书错误 |

完整示例：

```python
import requests
from requests.exceptions import Timeout, ConnectionError, HTTPError

try:
    response = requests.get('https://api.github.com', timeout=5)
    response.raise_for_status()
except Timeout:
    print("请求超时")
except ConnectionError:
    print("网络连接错误")
except HTTPError as e:
    print(f"HTTP 错误: {e}")
except Exception as e:
    print(f"其他错误: {e}")
else:
    print(response.json())
```

---

# 16. 认证

## 16.1 基本认证（Basic Auth）

```python
from requests.auth import HTTPBasicAuth

response = requests.get('https://httpbin.org/basic-auth/user/pass', auth=HTTPBasicAuth('user', 'pass'))
# 或简写
response = requests.get('https://httpbin.org/basic-auth/user/pass', auth=('user', 'pass'))
```

---

## 16.2 Bearer Token（JWT）

```python
headers = {'Authorization': 'Bearer your_token_here'}
response = requests.get('https://api.example.com', headers=headers)
```

---

## 16.3 Digest 认证

```python
from requests.auth import HTTPDigestAuth

response = requests.get('https://httpbin.org/digest-auth/auth/user/pass', auth=HTTPDigestAuth('user', 'pass'))
```

---

# 17. 性能与最佳实践

## 17.1 复用 Session

```python
session = requests.Session()
for i in range(100):
    session.get('https://api.example.com/item/' + str(i))
# Session 会自动复用 TCP 连接（Keep-Alive）
```

---

## 17.2 限制重试次数（使用 urllib3）

```python
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

session = requests.Session()
retry = Retry(total=3, backoff_factor=1, status_forcelist=[500, 502, 503, 504])
adapter = HTTPAdapter(max_retries=retry)
session.mount('http://', adapter)
session.mount('https://', adapter)
```

---

## 17.3 关闭连接

```python
response = requests.get('https://api.github.com')
response.close()       # 手动关闭
```

或使用上下文管理器：

```python
with requests.get('https://api.github.com') as response:
    print(response.text)
```

---

# 18. 常见应用场景

| 场景 | 方法 |
| ---- | ---- |
| REST API 调用 | GET/POST/PUT/DELETE + JSON |
| 网页爬虫 | GET + 自定义 Headers + 代理 |
| 文件下载 | stream + iter_content |
| 表单提交 | POST + data |
| 文件上传 | POST + files |
| 登录保持 | Session 维持 Cookie |
| 接口测试 | 配合 assert 检查状态码和响应 |

---

# 19. 常见问题

## 1. 出现 SSL 错误

```text
SSLError: [SSL: CERTIFICATE_VERIFY_FAILED]
```

解决方案：

```python
# 临时忽略（不推荐生产环境）
response = requests.get(url, verify=False)
# 或更新证书
pip install --upgrade certifi
```

---

## 2. 中文乱码

```python
response = requests.get('http://example.com')
response.encoding = 'utf-8'          # 或 'gbk'
print(response.text)
```

或自动检测：

```python
response.encoding = response.apparent_encoding
```

---

## 3. 请求超时

```python
# 设置总超时
response = requests.get(url, timeout=10)
# 设置连接超时和读取超时分开
response = requests.get(url, timeout=(3, 7))
```

---

## 4. 重定向循环

```python
# 限制最大重定向次数
response = requests.get(url, max_redirects=5)
```

---

## 5. 代理环境变量冲突

```python
# 忽略系统代理
response = requests.get(url, proxies={})
```

---

# 20. 推荐学习路线

```text
安装与导入
↓
GET 请求（基础、带参数）
↓
响应处理（status_code, text, json, headers）
↓
POST 请求（data, json, files）
↓
自定义 Headers 和 Cookies
↓
Session 管理
↓
超时、代理、SSL
↓
异常处理
↓
流式下载与上传
↓
最佳实践（复用 Session、重试）
```

---

# 21. 推荐练习项目

## 初级

* 爬取一个公开 API（如 GitHub API）的数据
* 实现一个简单的天气查询程序

---

## 中级

* 实现带登录功能的爬虫（Session + 表单提交）
* 批量下载图片或文件

---

## 高级

* 封装一个 REST API 客户端类
* 实现自动重试和指数退避
* 结合 asyncio + aiohttp 做并发请求

---

# 22. 总结与速查

## 常用方法

```python
requests.get(url, params=None, headers=None, cookies=None, auth=None, timeout=None, proxies=None, verify=True, stream=False)
requests.post(url, data=None, json=None, files=None, ...)
requests.put(url, data=None, ...)
requests.delete(url, ...)
requests.Session()    # 会话对象
```

## 常用属性

```python
response.status_code      # 状态码
response.text             # 文本内容
response.content          # 字节内容
response.json()           # JSON 解析
response.headers          # 响应头
response.cookies          # Cookie
response.url              # 最终 URL
response.history          # 重定向历史
response.encoding         # 编码
```

## 异常捕获

```python
from requests.exceptions import Timeout, ConnectionError, HTTPError
```