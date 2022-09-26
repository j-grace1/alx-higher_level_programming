#!/usr/bin/python3
import sys
argc = len(sys.argv)
if argc > 1:
    print('{} arguments:'.format(argc))
    for i in range(0, argc):
        print('{}: {}'.format(i, sys.argv[i]))
elif argc == 1:
    print('{} argument:'.format(argc))
else:
    print('{} arguments.'.format(argc))
