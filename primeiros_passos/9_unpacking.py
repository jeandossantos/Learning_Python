def unpacking_experiment(*args):
    arg1 = args[0]
    arg2 = args[1]
    rest = args[2:]

    print(arg1, arg2, rest)

unpacking_experiment(1, 2, 3, 4, 5)

print("****************************************************************")

def unpacking_experiment(**kwargs):
    print(kwargs)

unpacking_experiment(named="Test", other="Other")