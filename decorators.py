# def decorator(func):
   
#     def wrapper():
#         print("Before calling the function")
#         func()
#         print("After calling the function")

#     return wrapper 

def outer_decorator(num, val):
 
    number = num
    concate_val = val
    def decorator(func):

        def wrapper():

            for i in range(number):
                print(concate_val)
                func()
                

        return wrapper

    return decorator

num = 3
val = "HEY, HEY, HEY, HEY, HEY"
@outer_decorator(num, val)
def saying_hello():
    print("Hello")

saying_hello()




# class decorator_class:

#     def __init__(self, func):
#         self.func = func

#     def __call__(self):
#         print("Before calling the function")
#         self.func()
#         print("After calling the function")


# @decorator_class
# def saying_bye():
#     print("Bye!")

# saying_bye()
# # saying_bye = decorator_class(saying_bye)