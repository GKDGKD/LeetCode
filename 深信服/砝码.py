def fast_power(base, exponent):
    """
    快速幂运算。
    对于任意正整数 a 和非负整数 n，我们可以将 a^n 表示为：

    如果 n 为偶数，那么 a^n = (a^(n/2))^2。
    如果 n 为奇数，那么 a^n = a * (a^((n-1)/2))^2。
    通过不断地将指数 n 减半并递归计算，可以将幂运算的时间复杂度从线性降低到对数级别。

    @base: 基数，int
    @exponent: 指数，int
    
    """

    if exponent == 0:
        return 1
    if exponent % 2 == 0:
        half_power = fast_power(base, exponent // 2)
        return half_power * half_power
    else:
        half_power = fast_power(base, (exponent - 1) // 2)
        return base * half_power * half_power

def weight(n):

    # fama = [3 ** i for i in range(n)]
    # max_w  = int(sum(fama) % (10**7 + 7))
    res = 0
    for i in range(n):
        res += fast_power(3, i)

    return int(res % (10**7 + 7))

T = int(input())
# sol = Solution()
for _ in range(T):
    n = int(input())
    print(weight(n))


"""
5
1
2
3
137
1000


out:
1
4
13
4619116
2189876

"""