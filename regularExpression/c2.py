import re
s = 'abc, aac, afc, adc, acc'
r1 = re.findall('a[cf]c', s)
r2 = re.findall('a[^cf]c', s)
r3 = re.findall('a[c-f]c', s)
print(r1)
print(r2)
print(r3)