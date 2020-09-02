from typing import List
'''
给定一个正整数 n，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。

示例:

输入: 3
输出:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]

'''

class Solution:
    # matrix类型为二维列表，需要返回列表
    def generateMatrix(self, n: int) -> List[List[int]]:
        # write code here
        matrix=[[0]*n for i in range(n)]
        start=1
        for o in range((n+1)>>1):
            matrix[o][o:n - o]=range(start,start+n-2*o)
            start+=n-2*o
            for j in range(o + 1, n - o - 1):
                matrix[j][n - 1 - o]=start
                start+=1
            if start>= n*n:
                return matrix
            matrix[n-o-1][o:n - o]=range(start,start+n-2*o)[::-1]
            start+=n-2*o
            for j in range(n - o - 2,o,-1):
                matrix[j][o] = start
                start+=1
        return matrix

class Solution1:
    def generateMatrix(self, n: int) -> [[int]]:
        # 事实上很多在矩阵中转向的问题，可以直接设置边界参数量，然后判断参数量的移动来做出改变。
        # 该方法是要比上述方法更快的
        l, r, t, b = 0, n - 1, 0, n - 1
        mat = [[0 for _ in range(n)] for _ in range(n)]
        num, tar = 1, n * n
        while num <= tar:
            for i in range(l, r + 1): # left to right
                mat[t][i] = num
                num += 1
            t += 1
            for i in range(t, b + 1): # top to bottom
                mat[i][r] = num
                num += 1
            r -= 1
            for i in range(r, l - 1, -1): # right to left
                mat[b][i] = num
                num += 1
            b -= 1
            for i in range(b, t - 1, -1): # bottom to top
                mat[i][l] = num
                num += 1
            l += 1
        return mat

for i in Solution().generateMatrix(5):
    print(i)


