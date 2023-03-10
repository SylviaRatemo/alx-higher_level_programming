#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    count = len(sys.argv) - 1
    if count != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit (1)
    ops = {'+': add, '-': sub, '*': mul, '/': div}

    if sys.argv[2] in ops:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        op = ops[sys.argv[2]]
        ans = op(a, b)
        print("{:d} {:s} {:d} = {:d}".format(a, sys.argv[2], b, ans))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    exit(0)
