import requests
import re
from PIL import Image, ImageEnhance

# 百度下载单个图片
# url = "http://img3.imgtn.bdimg.com/it/u=3963046268,2775601997&fm=26&gp=0.jpg"
# header ={
#         "Referer": "http://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gb18030&word=%CD%BC%C6%AC&fr=ala&ala=1&alatpl=others&pos=0"
# }
# response = requests.get(url, headers = header)
# with open('test.jpg', 'wb') as f:
#     f.write(response.content)
# image = Image.open('test.jpg')
# image.show()

# 批量下载图片，首先找到请求所有图片url的url
page_url = 'http://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gb18030&word=%CD%BC%C6%AC&fr=ala&ala=1&alatpl=others&pos=0'
header ={
        "Referer": "http://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gb18030&word=%CD%BC%C6%AC&fr=ala&ala=1&alatpl=others&pos=0"
}
response = requests.get(page_url, headers = header)
response.encoding = 'utf-8' # 防止页面乱码，可以通过‘charset’,查看页面编码格式
html = response.text
pattern = r'"thumbURL":"(.*?)"'
urls = re.findall(pattern, html)
print(urls)
for index, url in enumerate(urls):
    response = requests.get(url, headers = header)
    with open('%s.%s' %(index, url.split('.')[-1]), 'wb') as f:
        f.write(response.content)
#print(response.text)  # 文本文件用.text，图片用.content