import sys

tasks = input().split(',')
MAX_T = 4800
# consume, t_min = [], []

n = len(tasks)
tt = {i: {'consume':0, 'min':0} for i in range(n)} 
for ind, i in enumerate(tasks):
    c, m = map(int, i.split(':'))
    tt[ind]['consume'] = c
    tt[ind]['min'] = m
    if m > MAX_T:
        print(-1)
        sys.exit(1)

max_consume_ind = max(tt)
res = tt[max_consume_ind]['min']
for i in range(n - 1):
    if i == max_consume_ind:
        pass
    else:
        res += tt[i]['consume']

max_min_t_ind = max(tt.items(), key=lambda x:x[1]['min'])
if res < max_min_t_ind[1]['min']:
    res = max_min_t_ind[1]['min']

print(res)

breakpoint()


# 1:10,2:12,3:10
# 13