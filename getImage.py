# -*- coding:utf8 -*-

import urllib.request, socket, re, sys, os

print(sys.getdefaultencoding())

# 定义文件保存路径
targetPath = "C:\\Users\\Student\\Desktop\\python"


# 检测路径有效
def saveFile(path, imgPath):
    # 检测路径有效性
    if not os.path.isdir(path):
        print("十分抱歉，路径不存在，已执行创建>>>")
        os.mkdir(path)
    else:
        print("路径存在,继续执行操作>>>")
    # 设置每个图片的路径
    fullPath = os.path.join(targetPath, imgPath)
    return fullPath


# 使用if __name__ == '__name__'来判断此文件是被引用还是直接调用
# if __name__ == "__main__":

# 获取关键字
kw = input('>>>请输入关键字\n')

# 设置网址
url = r'http://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=detail&fr=&sf=1&fmq=1447473655189_R&pv=&ic=0&nc=1&z=&se=&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word='+urllib.request.quote(kw)

# 伪装网络头部信息
# headers = {
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
# }

# 封装请求
req = urllib.request.Request(url)

# 发送请求，获取响应
resp = urllib.request.urlopen(req)

# 读取网页
html = resp.read()

# 设置编码格式
html = html.decode('utf-8')

# 输出检测
# print(html)

# 数据获取
imgs = re.findall(r'"objURL":"(.*?(jpg|png|gif|jpeg))"', html, re.S)

# 遍历检查
imgNum = len(imgs)

# 遍历输出
# for pic in imgs:
#     print(pic)

i = 1
# 储存图片
for pic in imgs:
    try:
        print('>>>正在下载第', i, '/', imgNum, '张图片:', pic)
        u = urllib.request.urlopen(pic[0],timeout=3)
        data = u.read()
        f = open('image//' + str(i) + '.' + pic[1], 'wb')
        f.write(data)
        f.close()
    except Exception as e:
        print('>>>图片下载失败！！！')
        i += 1
        continue
    i += 1
