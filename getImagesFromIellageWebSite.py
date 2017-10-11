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
    return re.findall('<img src="(.*?)".*?>', html, re.S)[2:]



# 定义下载方法
def download_img(images):
    i = 1
    for img in images:
        try:
            print("正在下载第",i,"/",len(images),"张图片")
            img = urllib.request.urlopen(img)
            f= open(imagePath+"\\"+i+".jpg","wb")
            f.write(img)
            f.close()
            i+=1
        except Exception as e:
            print(e)
            print("图片资源无法获取")
            i+=1
            continue
new_path = 'http://www.45uuuu.com'+get_data(get_one_page(my_url))[-26][0]


aaaa = get_img(get_one_page(new_path))
req = urllib.request.Request("http://0spyr.8iwvsl.com/11091C/p04/%E5%8F%88%E6%98%AF%E9%9B%99%E7%9C%89%E7%9B%AE%E8%AE%93%E4%BA%BA%E6%B7%B1%E9%82%83%20[14P]/01.jpg")
resp = urllib.request.urlopen(req)
f= open(imagePath+"\\1"+".jpg","wb")
f.write(resp.read())
f.close()