# map
list_x = [1, 2, 3, 4, 5, 6]
def square(x):
    return x * x
""" list_y = map(square, list_x)
print(list(list_y)) """
list_y = map(lambda x: x*x, list_x)
print(list(list_y))