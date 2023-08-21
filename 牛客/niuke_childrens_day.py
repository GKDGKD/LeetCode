"""
每年六一儿童节，牛客都会准备一些小礼物和小游戏去看望孤儿院的孩子们。
其中，有个游戏是这样的：首先，让 n 个小朋友们围成一个大圈，小朋友们的编号是0~n-1。然后，随机指定一个数 m ，让编号为0的小朋友开始报数。
每次喊到 m-1 的那个小朋友要出列唱首歌，然后可以在礼品箱中任意的挑选礼物，并且不再回到圈中，
从他的下一个小朋友开始，继续0... m-1报数....这样下去....直到剩下最后一个小朋友，可以不用表演，并且拿到牛客礼品，请你试着想下，哪个小朋友会得到这份礼品呢？

Solution:
这个问题可以使用数学归纳的方法来解决。我们将编号为0到n-1的小朋友依次编号为0, 1, 2, ..., n-1。设f(n, m)表示当有n个小朋友围成一圈时，每次报数为m时，最后获得礼物的小朋友的编号。

首先，我们可以知道当只有一个小朋友时，编号必然为0，即f(1, m) = 0。

接下来，我们考虑n个小朋友的情况。当有n个小朋友时，每次报数为m时，第一个出列的小朋友的编号是(m-1) % n。
假设这个小朋友的编号为x，则剩下的n-1个小朋友的编号为x+1, x+2, ..., n-1, 0, 1, ..., x-2。
我们可以将这个问题转化为有n-1个小朋友时的情况，即f(n-1, m)。但这个编号不是从0开始的，而是从x+1开始的，所以我们需要将它转换为从0开始编号的小朋友。
可以通过模运算来实现，即f(n, m) = (f(n-1, m) + m) % n。

最终的解就是当n个小朋友围成一圈时，每次报数为m时，最后获得礼物的小朋友的编号，即f(n, m)。

"""


def last_gift_holder(n, m):
    if n <= 0 or m <= 0:
        return -1  # 无效输入，返回-1表示错误
    last_holder = 0
    for i in range(2, n+1):
        last_holder = (last_holder + m) % i
        print(f'i: {i}, last_holder: {last_holder}')
    return last_holder

# 示例输入
n = 5
m = 3
result = last_gift_holder(n, m)
print(result)  # 输出：3
