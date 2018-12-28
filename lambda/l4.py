# map
list_x = [1, 2, 3, 4, 5, 6]
list_y = [1, 2, 3, 4, 5, 6]
# 如果传入参数列表大小不同的话，执行较少集合的长度
def square(x):
    return x * x
r = map(lambda x, y: x*x+y, list_x, list_y)
print(list(r))