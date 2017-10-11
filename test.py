import urllib.request,re

# 定义爬取网址
url = 'http://www.baidu.com'
# 定义请求
req = urllib.request.Request('http://www.baidu.com')
# 发送请求获取响应
resp = urllib.request.urlopen(req)
# 读取响应内容
html = resp.read()
# 设置网页编码格式
html = html.decode('utf-8')

# print(html)
# 通过正则表达式解析网页
links = re.findall('href="(http://.*?)"',html,re.S)

print(len(links))

for a in links:
    print(a)
