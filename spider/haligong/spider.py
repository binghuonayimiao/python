import requests
import re
import time
from PIL import Image, ImageEnhance
from bs4 import BeautifulSoup
from config import username, password
import pytesseract

session = requests.Session()
# 1.伪装浏览器
session.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'

def GetRandCode(path='randcode.jpg'):
    url = r'http://202.118.192.5/Public/ValidateCode.aspx'
    # url = r'http://jwxt.wust.edu.cn/whkjdx/verifycode.servlet'
    # url = r'http://jws.hebiace.edu.cn/CheckCode.aspx'
    ans = session.get(url)
    ans.raise_for_status() # 捕获异常
    with open(path, 'wb+') as file:
        file.write(ans.content)

    image = Image.open('randcode.jpg')
    image.show()
    print('请输入验证码：')
    # 下面四行代码为提取验证码中数字的逻辑
    # image = image.convert('RGB')
    # image.show()
    # code = pytesseract.image_to_string(image, lang='eng')
    # print(code)

def Login(username, password, randcode):
    # exit_url = 'http://202.118.192.5/UserLogin.aspx?exit=1'
    # session.post(exit_url)
    login_url = r'http://202.118.192.5/'
    information = {
                    'ScriptManager1':'UpdatePanel2|btLogin',
                    '__EVENTTARGET':'btLogin',
                    '__EVENTARGUMENT':'',
                    '__LASTFOCUS':'',
                    '__VIEWSTATE':'/wEPDwULLTE3MzIzNjYwNjMPZBYCAgMPZBYGAg0PZBYCZg9kFgICAQ8PFgIeCEltYWdlVXJsBSp+L1B1YmxpYy9WYWxpZGF0ZUNvZGUuYXNweD9pbWFnZT0yOTA3OTIyMzdkZAIRD2QWAmYPZBYCAgEPEGRkFgFmZAIVD2QWAmYPZBYCAgEPDxYCHgtOYXZpZ2F0ZVVybAUtfi9QdWJsaWMvRW1haWxHZXRQYXNzd2QuYXNweD9FSUQ9TjI5WURScmE0dUk9ZGQYAQUeX19Db250cm9sc1JlcXVpcmVQb3N0QmFja0tleV9fFgEFDVZhbGlkYXRlSW1hZ2WmiIGjvzd5iHMXi7DKBZRuINFwnQ==',
                    '__EVENTVALIDATION':'/wEdAAqyUmRJDCkiku2JFRaDozB6R1LBKX1P1xh290RQyTesRQa+ROBMEf7egV772v+RsRJUvPovksJgUuQnp+WD/+4LQKymBEaZgVw9rfDiAaM1opWKhJheoUmouOqQCzlwTSNWlQTw3DcvmMLY3PAqFoA+uFSTy5ozCEG4XBxL/Ykep0cgC/Irwlr9d8VObb8MnYO0GRqRfbdgDIW2dtIsr6rbyu4yvatwZnC7FEXYnsGzI6xfON0=',
                    'UserName': username, 
                    'PassWord': password, 
                    'ValidateCode': randcode,
                    'drpLoginType':'1',
                    '__ASYNCPOST':'true'
                    }
    login_response = session.post(login_url, data=information)
    print(login_response.text)
    student_url = 'http://202.118.192.5/Gstudent/Course/StudentScoreQuery.aspx?EID=VuYUA7YP5gRRL6Z-IeJgBXS10bXlTWXy-qmX4GxB8li4o6gB-9Zv6w==&UID=' + username
    student_response = session.post(student_url)
    soup = BeautifulSoup(student_response.text, features='lxml')
    print(soup)
    exit_url = 'http://202.118.192.5/UserLogin.aspx?exit=1'
    session.post(exit_url)
    # print(student_response.text)
GetRandCode()
randcode = input()
Login(username, password, randcode)
a = 1