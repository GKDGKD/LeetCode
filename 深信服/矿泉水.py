"""
题目：https://www.nowcoder.com/exam/test/73584754/detail?pid=23358504&examPageSource=Company&testCallback=https%3A%2F%2Fwww.nowcoder.com%2Fexam%2Fcompany%3FcurrentTab%3Drecommand%26jobId%3D100%26keyword%3D%E6%B7%B1%E4%BF%A1%E6%9C%8D%26selectStatus%3D0&testclass=%E8%BD%AF%E4%BB%B6%E5%BC%80%E5%8F%91

小明横穿沙漠，需要携带至少x毫升的水。

有两种规格的矿泉水可供选购：小瓶矿泉水每瓶500ml，价格a元。大瓶矿泉水每瓶1500ml，价格b元。

小明打算买一些矿泉水用于横穿沙漠，为了保证至少买到x毫升的水，小明至少需要花费多少钱？

输入例子：
3
5000 5 10
4999 5 10
5000 5 100
输出例子：
35
35
50

"""

def calculate(x, a, b):
    if x <= 500:
        return a
    elif x <= 1500:
        return b

    total = 0
    num_a, num_b = 0, 0
    while total < x:
        if x - total > 500 and b / 1500 < a / 500:
            num_b += 1
            total += 1500
        else:
            num_a += 1
            total += 500

    res = num_a * a + num_b * b
    return res

t = int(input())

for _ in range(t):
    x, a, b = map(int, input().split())
    print(calculate(x, a, b))