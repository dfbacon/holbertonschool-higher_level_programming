#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    arg_num = len(argv)
    total = 0
    for i in range(arg_num):
        if i > 0:
            total += int(argv[i])
    print('{:d}'.format(total))
