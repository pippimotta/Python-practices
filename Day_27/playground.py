# advanced Python Arguments
# def(*args) --* accepet any number of arguments
# 把傳入的數字放入一個名為args的tuple
def add(*args):
    result = 0
    for n in args:
        result += n
    return result


print(add(3, 4, 5, 6, 8, 9))


# unlimited keyword arguments
# kwargs 是一個dictionary
# def calculate(n, **kwargs):
#     # for key,value in kwargs.items():
#     #     print(key)
#     #     print(value)
#     n += kwargs['add']
#     n *= kwargs['multiply']
#     print(n)
#
#
# calculate(2, add=3, multiply=5)


class Car:

    def __init__(self, **kw):
        # kwargs is all the optional arguments that will be passed in
        # self.make = kw['make']
        self.make = kw.get('make')
        self.model = kw.get('model')
    # 用kw.get()來避免缺失key的error


my_car = Car(make='Nissan')
print(my_car.model)
