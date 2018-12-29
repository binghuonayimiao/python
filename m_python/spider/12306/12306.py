import requests
import re
from PIL import Image
import base64
import time
from config import username, password

# 根据图片位置返回坐标点，记得计算时候减去上面边框
def get_point(index):
    map = {
        '1':'36,45',
        '2':'113,45',
        '3':'178,45',
        '4':'255,45',
        '5':'36,116',
        '6':'113,116',
        '7':'178,116',
        '8':'255,116'
    }
    indexs = index.split(',')
    temp = []
    for item in indexs:
        temp.append(map[item])
    return ','.join(temp)

def get_info(url):
    response = session.get(url)
    return response

# cookie处理 request.Session 自动的处理，每次自动带上
session = requests.Session()

# 1.伪装浏览器 将User-Agent添加到headers
session.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'
# print(session.headers)

# 2.登陆获取页面的cookie 获取cookie发现在conf请求后才有的cookie
login_url = 'https://kyfw.12306.cn/passport/web/login'
conf_url = 'https://kyfw.12306.cn/otn/login/conf'
#session.post(login_url)
# print(session.cookies)

# 3.获取验证码
randcode_url = 'https://kyfw.12306.cn/passport/captcha/captcha-image64?login_site=E&module=login&rand=sjrand&1544237758647&callback=jQuery1910022049678042580956_1544237356508&_=1544237356514'
response = session.get(randcode_url)
image_txt = re.findall(r'"image":"(.*?)"', response.text)[0]
image_txt = base64.b64decode(image_txt)
with open('1.jpg', 'wb') as f:
    f.write(image_txt)
image = Image.open('1.jpg')
image.show()
# time.sleep(3)
# print(image_txt)

# 4.校验验证码
# check_url = 'https://kyfw.12306.cn/passport/captcha/captcha-check?callback=jQuery191014937880120235292_1544265281087&answer=124%2C104%2C206%2C113%2C200%2C53&rand=sjrand&login_site=E&_=1544265281089'
# 将answer删除 然后用后面连接新的answer
check_url = 'https://kyfw.12306.cn/passport/captcha/captcha-check?callback=jQuery191014937880120235292_1544265281087&rand=sjrand&login_site=E&_=1544265281089'
print('请输入选中图片位置')
image_index = input()
image_point = get_point(image_index)
check_response = session.get(check_url, params={'answer': image_point})  # 将url中的answer替换后面的内容
result_code = re.findall(r'"result_code":"(\d)"', check_response.text)[0]
print(result_code)
if result_code == '4':
    print('验证码校验成功')
    # 5.校验登陆
    login_url = 'https://kyfw.12306.cn/passport/web/login'
    data = {
        'username': username,
        'password': password,
        'appid': 'otn'
    }
    login_response = session.post(login_url, data=data)
    if login_response.json()['result_code'] == 0:
        print("校验用户名，密码成功")
        # 6.获取token (network对应的uamtk)
        token_url = 'https://kyfw.12306.cn/passport/web/auth/uamtk'
        data = {
            'appid': 'otn'
        }
        token_response = session.post(token_url, data=data)
        if token_response.json()['result_code'] == 0:
            print('获取tk成功')
            tk = token_response.json()['newapptk']
            # 7.验证tk(network中对应的uamauthclient)
            testtk_url = 'https://kyfw.12306.cn/otn/uamauthclient'
            data = {
                'tk': tk
            }
            testtk_response = session.post(testtk_url, data=data)
            if testtk_response.json()['result_code'] == 0:
                username = testtk_response.json()['username']
                print('恭喜' + username + '同学，登陆成功！！！！！')
                url = 'https://kyfw.12306.cn/otn/view/passengers.html'
                response = get_info(url)
                response.encoding = 'utf-8'
                print(response.text)
            else:
                 print('登录失败') 
        else:
            print('获取tk失败')
    else:
        print("校验用户名，密码失败")
else:
    print('验证码校验失败，请再次执行')
