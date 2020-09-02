from scipy.special import comb
from typing import List


class Solution62:
    '''
    一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

    机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

    问总共有多少条不同的路径？

    '''
    def uniquePaths(self, m: int, n: int) -> int:
        return self.comb(m+n-2,n-1)

    def factorialArray(self,arr):
        arr = [1] + arr
        tmp = 1
        res = []
        for i in range(1, len(arr)):
            for j in range(arr[i - 1] + 1, arr[i] + 1):
                tmp *= j
            res.append(tmp)
        return res

    def comb(self,n, k):
        if k > n / 2:
            k = n - k
        res = self.factorialArray([k, n - k, n])
        return res[2] // res[1] // res[0]

    def uniquePaths_withdp(self, m: int, n: int) -> int:  # C_{m+n}^m=C_{m+n-1}^m+C_{m+n-1}^{m-1}  对应到矩阵中就是左上和右下
        cur = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                cur[j] += cur[j-1]
        return cur[-1]

    def uniquePaths_opti(self, m: int, n: int) -> int: # dp[i]=sum(dp[k]) k=1...i
        if m == 1:
            return 1
        A = [1] * n

        for i in range(m - 2):
            for j in range(1, n):
                A[j] += A[j - 1]
        return sum(A)



class Solution63:
    '''
    一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
    机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
    现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？

    网格中的障碍物和空位置分别用 1 和 0 来表示。
    说明：m 和 n 的值均不超过 100。
    示例 1:
    输入:
    [
      [0,0,0],
      [0,1,0],
      [0,0,0]
    ]
    输出: 2
    解释:
    3x3 网格的正中间有一个障碍物。
    从左上角到右下角一共有 2 条不同的路径：
    1. 向右 -> 向右 -> 向下 -> 向下
    2. 向下 -> 向下 -> 向右 -> 向右

    '''
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m,n=len(obstacleGrid),len(obstacleGrid[0])
        cur = [0]*n
        cur[0]=1
        for i in range(m):
            cur[0]=min( int(obstacleGrid[i][0]!=1),cur[0])
            for j in range(1, n):
                if obstacleGrid[i][j]==1:
                    cur[j] = 0
                else:
                    cur[j] += cur[j-1]
        return cur[-1]


class Solution64:
    '''
    给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

    说明：每次只能向下或者向右移动一步。

    示例:

    输入:
    [
      [1,3,1],
      [1,5,1],
      [4,2,1]
    ]
    输出: 7
    解释: 因为路径 1→3→1→1→1 的总和最小。

    '''
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        for j in range(1,n):grid[0][j]+=grid[0][j-1]
        for i in range(1, m):
            grid[i][0]+= grid[i-1][0]
            for j in range(1, n):
                grid[i][j] +=min(grid[i-1][j],grid[i][j-1])
        return grid[-1][-1]

# a=[[0,0,0],[0,1,0],[0,0,0]]
a=[[0,1,0,0,0],[1,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
print(Solution63().uniquePathsWithObstacles(a))
print(Solution62().uniquePaths(1,2))