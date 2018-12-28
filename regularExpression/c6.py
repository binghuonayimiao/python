# 边界匹配 ^从字符串开头匹配 &匹配到结尾
# 加入qq4-9位合法
import re
aa = '10000000001'
r = re.findall('^\d{4,9}$', aa)
print(r)