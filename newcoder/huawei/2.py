m,n = [int(i) for i in input().split(' ')]

area = [[int(i) for i in input().split(' ')] for j in range(m)]



visited = [[0 for i in range(n)] for j in range(m)]
res = 0


def dfs(i, j, pre=None):
    if 0>i or i>=m or j<0 or j>= n or (pre is not None and pre >= area[i][j]):
        return 0
    if visited[i][j]:
        return visited[i][j]
    else:
        r = dfs(i-1, j, area[i][j])
        r = max(dfs(i+1, j, area[i][j]), r)
        r = max(dfs(i, j-1, area[i][j]), r)
        r = max(dfs(i, j+1, area[i][j]), r)
        visited[i][j] = r+1
        return r+1


for i in range(m):
    for j in range(n):
        res = max(dfs(i,j), res)

print(res)





'''
2 3
8 4 1
6 5 2

'''

# m,n = 1000,1000
# area = [[i+j*1000 for i in range(1000)] for j in range(1000)]