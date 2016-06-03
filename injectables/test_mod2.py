from injectables import injectable


@injectable(modules=['test_mod'])
def ztest(mod_dep):
    return mod_dep

if __name__ == '__main__':
    print(ztest())


