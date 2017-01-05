#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    argv = sys.argv
    operator = ['+', '-', '*', '/']
    if len(argv) != 4:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)
    elif argv[2] not in operator:
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)
    else:
        a = int(argv[1])
        b = int(argv[3])
        if argv[2] == '+':
            total = a + b
        elif argv[2] == '-':
            total = a - b
        elif argv[2] == '*':
            total = a * b
        else:
            total = a / b
        print('{:d} {:s} {:d} = {:d}'.format(a, argv[2], b, total))
