from injectables import injectable

@injectable
def mod_dep():
    return True

def f():
    return True

if __name__ == '__main__':
    import test_mod
    print (test_mod.f())

