import re
s = 'life is short, i use python'
r = re.findall('life (.*) python', s)
print(r)