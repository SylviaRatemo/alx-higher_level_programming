#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as mod
    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, mod.add(a, b)))
    print("{} - {} = {}".format(a, b, mod.sub(a, b)))
    print("{} * {} = {}".format(a, b, mod.mul(a, b)))
    print("{} / {} = {}".format(a, b, mod.div(a, b)))
