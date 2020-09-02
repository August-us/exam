from collections import defaultdict

n = int(input())
res = []

send = defaultdict(list)
for i in range(n):
    a, b = [int(i) for i in input().split(' ')]
    res.append(a)
    b -= 2
    send[b].append(i)
me = {}
def getMaxValue(k):
    if k in me:
        return me[k]
    r = res[k]
    if k in send:
        for i in send[k]:
            r += max(getMaxValue(i), 0)
    me[k] =  r % 1000000003
    return me[k]

a = 0
for i in range(n):
    a = max(getMaxValue(i), a)
print(a)





'''
5
-2 0
-1 2
-1 2
5 3
-10 3

'''