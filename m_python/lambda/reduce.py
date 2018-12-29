# reduce 类似递归 连续计算，连续调用lambda
from functools import reduce
list_x = [1, 2, 3, 4, 5, 6]
r = reduce(lambda x, y: x + y, list_x)
print(r)