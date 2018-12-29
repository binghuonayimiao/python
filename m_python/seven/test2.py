from PIL import Image, ImageEnhance
import pytesseract
image = Image.open('randcode.png')
#转换图片的模式
image = image.convert('YCbCr')
# image.show()
text = pytesseract.image_to_string(image, lang='eng')
print(text)