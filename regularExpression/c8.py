# 匹配模式参数,第三个参数可以选择多个模式用|并列
import re
language = 'PythonpythonC++Java'
r = re.findall('c\+\+', language, re.I)
print(r)