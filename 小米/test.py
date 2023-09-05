# import sys

# def convert(base, value):
#     # 编写一个函数来将数字从给定的进制转换为十进制
#     value = int(value, base)
#     return value

# a = []
# b = []

# for line in sys.stdin.readlines():
#     if line.strip() == 'END':
#         break
#     else:
#         n, m = line.strip().split('#')
#         print(f'n:{n}, m:{m}')

#         a.append(m)
#         b.append(convert(int(n), m))


import sys

for line in sys.stdin.readlines():
    if line[0] == '0':
        break
    else:
        line_ = list(map(int, line.split()))
        print(sum(line_[1:]))