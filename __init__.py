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

    def wrapper(override=False, *args, **kwargs):
        if override:
            return func(*args, **kwargs)
        resolved = run_func(func.__name__)
        injectable.calls = {}
        return resolved

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
    def how_are_you():
      return "how_are_you?"


    @injectable
    def im_fine(how_are_you):
      print(how_are_you)
      return 'I am fine'


    @injectable
    def conversation(im_fine):
      print (im_fine)
      print ('good to hear')


    # run function as injectable, which resolves and injects all dependencies first
    conversation()
    # override injection flow and call normally
    conversation(override=True, im_fine="hey!!!!")

