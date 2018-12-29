# 旅行者旅行问题
# 方法一
a = 0
def length(x):
    global a
    y = a + x
    a = y
    return y
print(length(2))
print(length(3))
print(length(6))

# 方法二
def real_length():
    a = 0
    def length(x):
        nonlocal a # 不加这个定义时候根据a = len，系统会判断其为一个局部变量，因此len = a + x就会报错，它不会向上查找a，认为a没有被定义
        len = a + x
        a = len
        return len
    return length

f = real_length()
print(f(2))
print(f(3))
print(f(6))


