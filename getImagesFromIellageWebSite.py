# -*- coding:utf-8 -*-
import json
import urllib.request, re, sys, os

# 文件保存路径 F:\imageFromWeb
imagePath = 'D:\\imageFromWeb'

# 检测文件路径
if not os.path.exists(imagePath):
    os.mkdir(imagePath)

# 定义爬取网站
# my_url = 'http://www.45uuuu.com/p04/list_42.html'
my_url = 'http://www.yiyibox.com'

headers = {"User-Agent": "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)", "Referer": "http://www.zhihu.com/articles"}


# 封装爬取方法
def get_one_page(url):
    # 封装请求
    req = urllib.request.Request(url, None, headers)

    # 进行爬取
    resp = urllib.request.urlopen(req)

    # 输出网页,设置编码
    html = resp.read().decode('utf-8')

    # 输出检测
    return html


# 定义正则匹配
def get_data(html):
    # 正则匹配
    return re.findall(r'<a href="(.*?)".*?>.*?</a>', html, re.S)


# 定义正则获取图片
def get_img(html):
    return re.findall('<img src="(.*?)".*?>', html, re.S)[2:]


# 定义下载方法
def download_img(images):
    i = 1
    for img in images:
        try:
            print("正在下载第", i, "/", len(images), "张图片")
            req = urllib.request.Request(img)
            img = urllib.request.urlopen(req)
            f = open(imagePath + "\\" + i + ".jpg", "wb")
            f.write(img)
            f.close()
        except Exception as e:
            print(e)
            print("图片资源无法获取")
        i += 1


# req = urllib.request.Request('http://www.yiyibox.com/api/v1.1/?page=1',None,headers)
# resp = urllib.request.urlopen(req)
# print(resp)
# print(resp.read().decode('utf-8'))


req = urllib.request.Request('http://www.yiyibox.com/api/v1.1/?page=1')
img = urllib.request.urlopen(req)
data = json.load(img)
# print(data['data']['items'][0]['shorturl'][1:])
print(len(data['data']['items']))