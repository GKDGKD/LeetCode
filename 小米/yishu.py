"""
2019年小米秋招——软件开发笔试题
网址：https://www.acmcoder.com/#/practice/company

寻找异数
定义:数值序列中包含2~16进制整数，如果序列中有一个数，与序列中其他任何一个数大小都不相等，则这个数叫做“异数”。请找出给定数值序列中所有的“异数”。

输入数值序列行(0<i，每一行分别是进制和数值，以“#”分割。如: n#m,n是整数，代表n进制(1n<17),m是n进制下的数值.
输入序列以结束符”END”结束。

输出j行(0<js=i,每 行都是输入序列的“异数”。要求
1.按照输入序列的原序输出:
2.如果没有”异数”,输出字符串”None"
3.结束符“END”不用输出

input:
10#15
4#32
4#33
8#17
END

out:
4#32

"""

import sys
def convert(n, m):
    if int(n) == 10:
        return int(m)
    else:
        res = 0
        for i in range(len(m)):
            res += int(n)**i*int(m[-(i+1)])

        return res

a = []
b = []

# while True:
#     line = input()
#     print(line)
#     if line == 'END':
#         break
#     else:
#         n, m = line.split('#')
#         a.append(line)
#         b.append(convert(n, m))
#         print(f'n:{n}, m:{m}')
#         print(f'a: {a}, b: {b}')


for line0 in sys.stdin:
    line = line0.strip()
    print(line)  # 移除行尾的换行符
    if line == 'END':
        break
    else:
        n, m = line.split('#')
        print(f'n:{n}, m:{m}')

        a.append(line)
        b.append(convert(int(n), m))


if len(set(b)) == 1:
    print('None')
else:
    count = {i: 0 for i in b}
    for i in b:
        count[i] += 1
    yishu = max(count.items(), key=lambda x:x[1]==1)[0]

yishu_index = b.index(yishu)
# breakpoint()
print(a[yishu_index])
