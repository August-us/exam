from collections import defaultdict

n,m,k = [int(i) for i in input().split(' ')]


path = defaultdict(lambda :defaultdict(lambda :0))
for i in range(m):
    x,y,l = [int(i) for i in input().split(' ')]
    path[x][y] = l
    path[y][x] = l


for i in range(k):
    x,y = [int(i) for i in input().split(' ')]
    path[x][y] = 0
    path[y][x] = 0

flag = [False for i in range(n)]
res = float('inf')
def viste(s, distance):
    global res
    if flag[s - 1] or distance>res:
        return
    elif s==n:
        res = min(res, distance)
    else:
        flag[s - 1]=True
        for i in path[s]:
            viste(i, distance+path[s][i])
viste(1, 0)
if res==float('inf'):
    print(-1)
else:
    print(res)
'''
5 3 2
1 2 1
2 3 1
3 4 1
4 5
1 2
'''