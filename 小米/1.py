import sys

for line in sys.stdin.readlines():
    if line[0] == '0':
        break
    else:
        line_ = list(map(int, line.split()))
        print(sum(line_[1:]))
