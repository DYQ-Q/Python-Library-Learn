import requests

response = requests.get('https://api.github.com')
print(response.status_code)      # 200
print(response.text)             # 响应内容（字符串）