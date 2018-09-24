import inspect
def reflect(obj):
    print(type(obj))
    for x in inspect.getmembers(obj):
        print(x[0])
        print()

reflect(1)
reflect(["1","2"])
