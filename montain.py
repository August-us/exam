N,M=[int(i) for i in input().strip().split(' ')]
graph=[[0 for i in range(N)]for i in range(N)]
for i in range(M):
    s, e = [int(i) for i in input().strip().split(' ')]
    graph[s-1][e-1]=graph[e-1][s-1]=1
vis=[False for i in range(N)]

def dfs(i):
    for j in range(i+1,N):
        if graph[i][j]!=0 and not vis[j]:
            vis[j]=True
            dfs(j)
            return
    for j in range(i+1,N):
        if graph[i][j]!=0:
            dfs(j)
time=0
for i in range(N):
    if vis[i]:
        continue
    else:
        vis[i]=True
        time+=1
        dfs(i)
print(time)




'''
5 4
1 3
2 3
3 4
3 5

4 0
'''