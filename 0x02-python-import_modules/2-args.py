#!/src/bin/python3
def no_args(*args):
    while(args):
        print("{}: {}".format((len(args), args)))
        args = args + 1
