from injectables import injectable

@injectable(modules=['test_mod3'])
def mod_dep(another_mod_dep):
    return another_mod_dep

