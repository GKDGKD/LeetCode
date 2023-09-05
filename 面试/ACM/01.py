import sys

for line in sys.stdin:
    line  = line.split()
    print(type(line[0]))
    if line[0] == '0':
        break
    else:
        print(line[0] + line[1])
