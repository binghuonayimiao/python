import re
language = 'cpp|python|cpp|php|cpp'
def convert(value):
    match = value.group()
    return '++' + match + "++"
r = re.sub('cpp', convert, language)
print(r)
# ----------------------------
s = 'a8c3721d86'
def my_replace(value):
    match = value.group()
    if int(match) > 6:
        return '9'
    else:
        return '0'

r = re.sub('\d', my_replace, s)
print(r)