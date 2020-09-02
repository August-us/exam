import numpy as np

def combination_list(string,n):
    res=set()
    if not isinstance(string,list):
        string=list(string)
    def dfs(begin,n,pre):
        if len(string)-begin < n:
            return
        if n==0:
            # res.add(''.join(map(str,pre)))
            res.add(tuple(pre.copy()))
            return
        pre.append(string[begin])
        dfs(begin+1,n-1,pre)
        pre.pop()
        dfs(begin+1,n,pre)
    dfs(0,n,[])
    return res
# 输入一个8个数字的数组，判断是否可以把数字甜到正方形顶点上，使得三组相对的面的四个顶点之和全部相等，
def OctDigitPermutation(array):
    if sum(array)&1:
        return False
    half=sum(array)>>1
    count=0
    res=combination_list(array,4)
    for r in res:
        if sum(r)==half:
            print(r)
            count+=1
    return count>5



from typing import List

'''
n       solution(n)  
1       1  
2       0  
3       0  
4       2  
5       10  
6       4  
7       40  
8       92  
9       352  
10      724  
11      2680  
12      14200  
13      73712  
14      365596  
15      2279184  
16      14772512  
17      95815104  
18      666090624  
19      4968057848  
20      39029188884  
21      314666222712  
22      2691008701644  
23      24233937684440  
24      227514171973736  
25      2207893435808352 
'''

class NQueen:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []

        def nQueens(pre=[], last=list(range(n))):
            if not last:
                res.append(pre.copy())
            for idx,i in enumerate(last):
                if pre and not self.couldPlace(i,pre):
                    continue
                pre.append(i)
                last.remove(i)
                nQueens(pre, last)
                pre.remove(i)
                last.insert(idx,i)
        nQueens([],list(range(n)))
        result = []
        for r in res:
            _=[]
            for i in r:
                string='.'*i+'Q'+'.'*(n-i-1)
                _.append(string)
            result.append(_)
        return result

    def couldPlace(self, i, pre):
        for j in range(1,len(pre)+1):
            if abs(i-pre[-j])==j:
                return False
        return True

# 单纯的求数目，使用位运算来加快判断速度。
class Solution:
    def totalNQueens(self, n):
        def backtrack(row=0, hills=0, next_row=0, dales=0, count=0):
            """
            :type row: 当前放置皇后的行号
            :type hills: 主对角线占据情况 [1 = 被占据，0 = 未被占据]
            :type next_row: 下一行被占据的情况 [1 = 被占据，0 = 未被占据]
            :type dales: 次对角线占据情况 [1 = 被占据，0 = 未被占据]
            :rtype: 所有可行解的个数
            """
            if row == n:  # 如果已经放置了 n 个皇后
                count += 1  # 累加可行解
            else:
                # 当前行可用的列
                # ! 表示 0 和 1 的含义对于变量 hills, next_row and dales的含义是相反的
                # [1 = 未被占据，0 = 被占据]
                free_columns = columns & ~(hills | next_row | dales)

                # 找到可以放置下一个皇后的列
                while free_columns:
                    # free_columns 的第一个为 '1' 的位
                    # 在该列我们放置当前皇后
                    curr_column = - free_columns & free_columns

                    # 放置皇后
                    # 并且排除对应的列
                    free_columns ^= curr_column


                    count = backtrack(row + 1,
                                      (hills | curr_column) << 1,
                                      next_row | curr_column,
                                      (dales | curr_column) >> 1,
                                      count)
            return count

        # 棋盘所有的列都可放置，
        # 即，按位表示为 n 个 '1'
        # bin(cols) = 0b1111 (n = 4), bin(cols) = 0b111 (n = 3)
        # [1 = 可放置]
        columns = (1 << n) - 1
        return backtrack()


print(sorted(Solution().totalNQueens(5)))
res=[["Q....","..Q..","....Q",".Q...","...Q."],["Q....","...Q.",".Q...","....Q","..Q.."],[".Q...","...Q.","Q... .","..Q..","....Q"],[".Q...","....Q","..Q..","Q....","...Q."],["..Q..","Q....","...Q.",".Q...","....Q"],["..Q..","....Q",".Q...","...Q.","Q...."],["...Q.","Q....","..Q..","....Q",".Q..."],["...Q.",".Q...","....Q","..Q..","Q...."],["....Q",".Q...","...Q.","Q....","..Q.."],["....Q","..Q..","Q....","...Q.",".Q..."]]
print(sorted(res))
print(res)