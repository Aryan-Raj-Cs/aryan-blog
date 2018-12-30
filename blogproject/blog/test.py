def decorator(arg1, arg2):

    def real_decorator(function):

        def wrapper(args):
            print("Congratulations.  You decorated a function that does something with ",args)
            function(args)
        return wrapper

    return real_decorator

@decorator("her0","kk")
def print_args(a):
    print(a)
print_args("aaa")

print("=====================================")
class my_decorator(object):

    def __init__(self,f):
        print("inside my_decorator.__init__()")
        #f() # Prove that function definition has completed
        self.f=f
    def __call__(self,h,j):
        print("inside my_decorator.__call__()",j,h)
        self.f(h,j)



@my_decorator
def aFunction(a,b):
    print("inside aFunction()")

print("Finished decorating aFunction()")

aFunction("f","h")

print("finshing................................")
class ClassBasedDecorator(object):

    def __init__(self, func_to_decorate):
        print ("INIT ClassBasedDecorator")
        self.func_to_decorate = func_to_decorate

    def __call__(self, *args, **kwargs):
        print("CALL ClassBasedDecorator")
        return self.func_to_decorate(*args, **kwargs)


@ClassBasedDecorator
def print_moar_args(*args):
    for arg in args:
        print("arg")


print_moar_args(1, 2, 3)

print("class based with arguments....................................")
class ClassBasedDecoratorWithParams(object):

    def __init__(self, arg1, arg2):
        print ("INIT ClassBasedDecoratorWithParams")
        print( arg1)
        print (arg2)

    def __call__(self, fn):
        print ("CALL ClassBasedDecoratorWithParams")

        def new_func(*args, **kwargs):
            print ("Function has been decorated.  Congratulations.")
            return fn(*args, **kwargs)
        return new_func


@ClassBasedDecoratorWithParams("arg1", "arg2")
def print_args_again(*args):
    for arg in args:
        print (arg)


print_args_again(1, 2, 3)
print_args_again(1, 2, 3)