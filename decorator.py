from pprint import pprint
def print_args(func):

    def inner(*args,**kwargs):
            for item in args:
                print(item)
            pprint(kwargs)
            
            print("I got decorated")
            func(*args, **kwargs)
            print("after func")
    return inner
@print_args
def simp(*args,rabbit, name):
    print("simple")
    print(args)
    print(rabbit)



simp("dog","wooo",rabbit=None, name="boo")


# def arg_func()
