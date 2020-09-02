from typing import List

'''这道题如果需要优化O(1)的空间复杂度，则可以考虑使用位来标记死活'''
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:return board
        if len(board)==1 or len(board[0])==1:
            for i in range(len(board)):
                for j in range(len(board[0])):
                    board[i][j] = 0
            return board
        res = [i.copy() for i in board]
        def count(i,j):
            if 0<=i<len(res) and 0<=j< len(res[0]):
                return res[i][j]
            return 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                cur = 0
                for k in [-1, 1]:
                    for h in range(-1, 2):
                        cur += count(i+k,j+h)
                cur += count(i ,j-1) + count(i, j+1)
                if cur < 2:
                    board[i][j] = 0
                elif cur >3:
                    board[i][j] =0
                elif board[i][j] ==0 and cur==3:
                    board[i][j] =1
print(Solution().gameOfLife([[0,1,0],[0,0,1],[1,1,1],[0,0,0]]))