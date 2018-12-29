class Human():
    sum = 0
    age = 18
    name = 'zgs'
    def __init__(self, name, age):
        self.age = age
        self.name = name
    def my_print(self):
        print(self.name)