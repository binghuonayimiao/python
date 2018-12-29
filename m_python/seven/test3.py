import requests
import re
import time
from PIL import Image, ImageEnhance
import pytesseract

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36",
}
foo = requests.session()

def GetRandCode(path='randcodeYES.jpg'):
    code = ''
    i = 1
    while code == '':
        url = r'http://202.118.192.5/Public/ValidateCode.aspx'
        #url = r'http://jwxt.wust.edu.cn/whkjdx/verifycode.servlet'
        # url = r'http://jws.hebiace.edu.cn/CheckCode.aspx'
        ans = foo.get(url)
        ans.raise_for_status()
        with open(path, 'wb+') as file:
            file.write(ans.content)

        image = Image.open('randcodeYES.jpg')
        image.show()
        image_gray = image.convert('L')
        image_gray.show()
        img_two = image_gray.point(lambda x:255 if x>200 else 0)
        img_two.show()
        code = pytesseract.image_to_string(img_two, lang='eng')
        print(code)
        print(i)
        #break
    

GetRandCode()