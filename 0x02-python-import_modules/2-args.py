#!/usr/bin/python3
str = str(input(''))
split_str = str.split(' ')
argv = []
for i in split_str:
    argv.append(i)
argc = len(argv)
if argc > 0:
    print('{} arguments:'.format(argc))
    for i in range(0, argc):
        print('{}: {}'.format(i, argv[i]))
elif argc == 0:
    print('{} argument:'.format(argc))
else:
    print('{} arguments.'.format(argc))