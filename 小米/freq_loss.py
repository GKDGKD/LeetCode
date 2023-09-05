n = int(input())
losses = input().split(',')

f, l = [], []
for i in losses:
    freq, loss = list(map(int, i.split(':')))
    f.append(freq)
    l.append(loss)

distance = [abs(n - i) for i in f]
min_dis  = min(distance)
nums     = [i == min_dis for i in distance]
len_     = len(distance)
if sum(nums) > 1:
    res = []
    for i in range(len_):
        if distance[i] == min_dis:
            res.append(l[i])
    print('%.1f' %(sum(res) / len(res)))
else:
    for i in range(len_):
        if distance[i] == min_dis:
            breakpoint()
            print('%.1f'%(l[i]))


# breakpoint()
# 2800
# 1950:10,2000:15,3000:9
# 9.0