# 组
import re
a = 'pythonpythonpythonpythonpythonpythonpythonpython'
r = re.findall('(python){5}', a)
print(r)