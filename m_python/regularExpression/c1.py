import re
str = 'C6C++7PHP8Python9Java'

result = re.findall('\d', str)
print(result)