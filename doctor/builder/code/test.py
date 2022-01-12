import inspect

def foo(arg1, arg2):
    #do something with args
    a = arg1 + arg2
    return a


if __name__ == "__main__":
    source_foo = inspect.getsource(foo)  # foo is normal function
    print(source_foo)