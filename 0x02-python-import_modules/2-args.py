#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    arg_num = len(argv)
    if arg_num == 1:
        print('{:d} argument.'.format(0))
    elif arg_num == 2:
        print('{:d} argument:'.format(arg_num - 1))
        print('{:d}: {:s}'.format(1, argv[1]))
    else:
        print('{:d} arguments:'.format(arg_num - 1))
        for i in range(arg_num):
            if i > 0:
                print('{:d}: {:s}'.format(i, argv[i]))
