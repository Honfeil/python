# -*- coding:utf-8 -*-

# 这个破网站超级麻烦
# 定义获取json的方法
import urllib.request, json, re, os

path = 'D:\imageFromWeb'

if not os.path.exists(path):
    os.mkdir(path)


def get_resource(url, type='json'):
    req = urllib.request.Request(url)
    resp = urllib.request.urlopen(req)
    if type == 'json':
        return json.load(resp)
    else:
        return resp.read().decode('utf-8')


# 将json有用的信息转为list
def trans_data(json):
    list = []
    for data in json['data']['items']:
        list.append({'name': data['collect']['nickname'], 'url': 'http://www.yiyibox.com/photo' + data['shorturl'][1:]})
    return list


# 从页面中解析出img地址
def get_img_url(html):
    return re.findall(r'<img src="(.*?)" width="658">', html, re.S)

# 根据图片地址下载图片
def download_img(img_path,images):
    i=1
    for img in images:
        print('>>>正在下载第%d/%d张' % (i,len(images)))
        try:
            req = urllib.request.Request('http:'+img)
            resp = urllib.request.urlopen(req).read()
            f = open(img_path+'\\'+str(i)+'.jpg','wb')
            f.write(resp)
            f.close()
        except Exception as e:
            print(e)
            print(">>>图片下载失败")
        i+=1


# 根据图片地址进行下载
def download_data(data):
    for msg in data:
        print('正在下载%s的图片' % msg['name'])
        img_path = path + '\\' + msg['name']
        if not os.path.exists(img_path):
            os.mkdir(img_path)
        html = get_resource(msg['url'], 'web')
        images = get_img_url(html)
        print(images)
        download_img(img_path,images)



aaaa = get_resource('http://www.yiyibox.com/api/v1.1/?page=1')

data = trans_data(aaaa)
download_data(data)


