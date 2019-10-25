def getMaximumGold_(grid):
    # error version, I only considered the bottom and right without considering the left and upper.
    n=len(grid)
    m=len(grid[0])
    res=0

    for i in range(n-2,-1,-1):
        if grid[i][-1]!=0:
            grid[i][-1]+=grid[i+1][-1]
            res=max(grid[i][-1],res)
    for i in range(m-2,-1,-1):
        if grid[-1][i]!=0:
            grid[-1][i]+=grid[-1][i+1]
            res = max(grid[i][-1], res)
    for i in range(n-2,-1,-1):
        for j in range(m - 2, -1, -1):
            if grid[i][j]!=0:
                grid[i][j]+=max(grid[i+1][j],grid[i][j+1])
                res=max(res,grid[i][j])
    print(res)

def getMaximumGold(grid):
    n = len(grid)
    m = len(grid[0])
    res=0
    visited = [[False for i in range(m)] for j in range(n)]

    def dfs(i,j):
        tri=0
        visited[i][j]=True
        if i>0 and grid[i-1][j] and not visited[i-1][j]:
            tri=max(tri,dfs(i-1,j))
        if i<n-1 and grid[i+1][j] and not visited[i+1][j]:
            tri=max(tri,dfs(i+1,j))
        if j>0 and grid[i][j-1] and not visited[i][j-1]:
            tri=max(tri,dfs(i,j-1))
        if j<m-1 and grid[i][j+1] and not visited[i][j+1]:
            tri=max(tri,dfs(i,j+1))
        visited[i][j] = False
        return grid[i][j]+tri
    for i in range(n):
        for j in range(m):
            if grid[i][j]:
                res=max(res,dfs(i,j))
    return res


class Solution:
    def search4(self, i, j, val, grid, loc):
        va = [val]
        loc[i][j] = 1
        if i > 0 and grid[i - 1][j] and not loc[i - 1][j]:
            va.append(self.search4(i - 1, j, val + grid[i - 1][j], grid, loc))
        if i < len(grid) - 1 and grid[i + 1][j] and not loc[i + 1][j]:
            va.append(self.search4(i + 1, j, val + grid[i + 1][j], grid, loc))
        if j > 0 and grid[i][j - 1] and not loc[i][j - 1]:
            va.append(self.search4(i, j - 1, val + grid[i][j - 1], grid, loc))
        if j < len(grid[0]) - 1 and grid[i][j + 1] and not loc[i][j + 1]:
            va.append(self.search4(i, j + 1, val + grid[i][j + 1], grid, loc))
        loc[i][j] = 0
        return max(va)

    def getMaximumGold(self, grid):
        ret = 0
        for m in range(len(grid)):
            for n in range(len(grid[0])):
                loc = [[0 for ii in range(len(grid[0]))] for jj in range(len(grid))]
                tmp = grid[m][n]
                if not tmp:
                    continue
                tmp = self.search4(m, n, tmp, grid, loc)
                ret = max(tmp, ret)
        return ret

if __name__ == '__main__':
    mat=[[0,0,0,2,22,26,0],[0,0,2,5,0,0,14],[15,17,0,25,0,26,0],[0,23,0,0,0,0,14],[0,4,0,4,0,1,0],[29,0,28,0,0,0,28]]
    mat1=[[0,6,0],[5,8,7],[0,9,0]]
    print(getMaximumGold(mat))
    # print(Solution().getMaximumGold(mat))
    input()
