from enum import Enum
class VIP(Enum):
    YELLOW = 1
    GREEN = 2
    RED = 3

print(VIP.YELLOW)
print(VIP.YELLOW.value)
for v in VIP.__members__:
    print(v)


# 加入从数据库中读出来一个a,如何给其转换为枚举类型

a = 1
print(VIP(a))