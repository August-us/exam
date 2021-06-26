n = int(input())

pan = []
visited = [[0 for i in range(n)] for j in range(n)]
res = float('inf')
for i in range(n):
    pan.append([int(i) for i in input().split(' ')])

def dfs(i,j, cur, pre):
    if i>=n or i<0 or j>=n or 0>j or visited[i][j]:
        return
    else:
        cur += abs(pre-pan[i][j])
        global res
        if cur > res:
            return
        if i==n-1 and j==n-1:
            res = min(cur, res)
            visited[i][j] = 0
            return
        visited[i][j] = 1

        dfs(i-1,j, cur, pan[i][j])
        dfs(i+1,j, cur, pan[i][j])
        dfs(i,j-1, cur, pan[i][j])
        dfs(i,j+1, cur, pan[i][j])
        visited[i][j] = 0

dfs(0,0,0,pan[0][0])
print(res)

#     for j in range(n):
#         res[i][j] = min(res[i-1][j]+abs(pan[i][j] - pan[i-1][j]), res[i][j-1]+abs(pan[i][j] - pan[i][j-1]))
#
# print(res[-1][-1])



'''
3
1 2 4
1 3 1
1 2 1
'''