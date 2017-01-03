#!/usr/bin/python3
i = 0
for i in range(ord('a'), ord('z')+1):
    if (not(i == ord('e') or i == ord('q'))):
        print(chr(i), end='')
