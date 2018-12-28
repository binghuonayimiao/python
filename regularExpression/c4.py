# 数量词
import re
s = 'python 111java   cpp'
r = re.findall('[a-z]{3,6}', s)
# 贪婪 与 非贪婪
# 贪婪要匹配最大词数  
# 非贪婪匹配最小词数
# 非贪婪加上？号 [a-z]{3,6}？
print(r)