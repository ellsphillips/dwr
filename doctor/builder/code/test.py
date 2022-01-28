import inspect


def foo(a: int, b: int) -> int:
    # do something with args
    return a + b


if __name__ == "__main__":
    source_foo = inspect.getsource(foo)  # foo is normal function
    print(source_foo)
