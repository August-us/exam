from collections import defaultdict

n,k = [int(i) for i in input().split(' ')]
keys= defaultdict(lambda:0)
b = [0] * (k-1)
res =0
for i in range(n):
    a = [int(i) for i in input().split(' ')]
    for i in range(1,k):
        a[i] -= a[0]
        b[i-1] = -a[i]
    if tuple(b) in keys:
        res += keys[tuple(b)]
    t = tuple(a[1:])
    keys[t] +=1

print(res)


'''
5 3
2 11 21
19 10 1
20 11 1
6 15 24
18 27 36
'''