# -*- coding:utf-8 -*-

import urllib.request, re, sys, os

# 文件保存路径 F:\imageFromWeb
imagePath = 'F:\\imageFromWeb'

# 检测文件路径
if not os.path.exists(imagePath):
    os.mkdir(imagePath)

# 定义爬取网站
my_url = 'http://www.45uuuu.com/p04/list_42.html'


# 封装爬取方法
def get_one_page(url):
    # 封装请求
    req = urllib.request.Request(url)

    # 进行爬取
    resp = urllib.request.urlopen(req)

    # 输出网页,设置编码
    html = resp.read().decode('utf-8')

    # 输出检测
    return html

# 定义正则匹配
def get_data(html):
    # 正则匹配
    return re.findall(r'<a href="(.*?)".*?>(.*?)</a>', html, re.S)

# 定义正则获取图片
def get_img(html):
    # 正则匹配
    return re.findall(r'<img src="(.*?\.jpg)" border="0"><br>', html, re.S)

new_path = r'http://www.45uuuu.com'+get_data(get_one_page(my_url))[-27][0]

for i in get_img(get_one_page(new_path)):
    print(i)