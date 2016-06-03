import inspect
import importlib
import types


def init_state(injectable):

    if not hasattr(injectable, 'registry'):
        injectable.registry = {}

    if not hasattr(injectable.registry, 'mods'):
        injectable.mods = {}

    if not hasattr(injectable, 'calls'):
        injectable.calls = {}


def set_runner():

    def runner(name):
        func = injectable.registry[name]["func"]
        deps = injectable.registry[name]["deps"]
        args = []

        for dep in deps:
            if dep in injectable.calls:
                raise Exception("Circular dependency!")

            injectable.calls[dep] = dep
            args.append(runner(dep))

        return func(*args)

    return runner


def set_resolved_injectable(funcs, run_func):

    def resolved_injectable(override=False, *args, **kwargs):
        if override:
            return funcs(*args, **kwargs)
        resolved = run_func(funcs.__name__)
        injectable.calls = {}
        return resolved

    sig = inspect.signature(funcs)
    injectable.registry[funcs.__name__] = {
        "func": funcs,
        "deps": list(sig.parameters),
    }

    return resolved_injectable


def register_modules(modules):
    for module in modules:
        if module not in injectable.mods:
            injectable.mods[module] = importlib.import_module(module)


def injectable(modules=None):

    def wrapper(funcs):
        run_func = set_runner()
        return set_resolved_injectable(funcs, run_func)

    init_state(injectable)

    if callable(modules):
        f = modules
        return wrapper(f)

    elif isinstance(modules, list):
        register_modules(modules)
        return wrapper

