import re
language = 'python cpp php'
# 也可以这么替换
# language.replace('python', 'java')
r = re.sub('python', 'java', language)
print(r)
print(language)
language = re.sub('python', 'java', language)
print(language) 