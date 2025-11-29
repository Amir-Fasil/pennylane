def decorator(num, func):
    num_repet = num
    def wrapper():
        print("Before calling the function")
        for i in range(num_repet):
            func()
        print("After calling the function")

    return wrapper 

num = 3
@decorator(num)
def saying_hello():
    print("Hello")


saying_hello()

num = 3
decorated_function = decorator(saying_hello, num)
decorated_function()


class decorator_class:
    def __init__(self, func):
        self.func = func

    def __call__(self):
        print("Before calling the function")
        self.func()
        print("After calling the function")


def saying_bye():
    print("Bye!")

decoration_class = decorator_class(saying_bye)
decoration_class()