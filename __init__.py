import inspect


def injectable(func):

    def run_func(name):
        func = injectable.registry[name]["func"]
        deps = injectable.registry[name]["deps"]
        args = []

        if not hasattr(injectable, 'calls'):
            injectable.calls = {}

        for dep in deps:
            if dep in injectable.calls:
                raise Exception("Circular dependency!")

            injectable.calls[dep] = dep
            args.append(run_func(dep))

        return func(*args)

    def wrapper():
        return run_func(func.__name__)

    if not hasattr(injectable, 'registry'):
        injectable.registry = {}

    sig = inspect.signature(func)
    injectable.registry[func.__name__] = {
        "func": func,
        "deps": list(sig.parameters),
    }

    return wrapper


'''
Example usage
'''
if __name__ == '__main__':

    @injectable
    def a():
        return "hey!"


    @injectable
    def b(a):
        return a


    @injectable
    def c(b):
        print (b)


    c()



