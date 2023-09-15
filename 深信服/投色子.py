p_map = {i: 7 - i for i in range(1, 7)}




x = int(input())

if x < 2:
    print(0)
elif x <  7:
    print(1)
else:
    print(x % 6 + 1)


"""
in:
7
149696127901

out:
2
27217477801

"""