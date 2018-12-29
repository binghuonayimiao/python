import re
s = 'sahdfk&$54dad'
# \d 数字 \D非数字
# \w 数字和字母  \w相反
r = re.findall('\w', s)
r1 = re.findall('A-Za-z0-9', s)
# r和r1结果等价
print(r)