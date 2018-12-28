# 数量词
# *匹配前面这个字符0次或者无限多次
# +一次或者无限多次
# ？匹配0次或者一次
import re
str = 'pytho0pythonn1python'

result = re.findall('python*', str)
print(result)
result1 = re.findall('python?', str)
print(result1)