from functools import reduce


'''
从左上角开始往下走，如果一个格子的行号和列号的数每个数位上的数之和大于k，则可以进入，输入行号和列号，以及阈值k，判断最多可以到达多少个格子
'''

t = int(input())


for i in range(t):
    h, w, k = [int(i) for i in input().split(' ')]

    visited = [[False for i in range(w)] for j in range(h)]
    res = 0


    def couldArrive(s):
        return reduce(lambda x,y:x+int(y), s, 0) > k
    def dfs(i, j):
        global res
        if 0>i or i>=h or j<0 or j>= w or visited[i][j] or couldArrive(str(i)+str(j)):
            return

        else:
            visited[i][j] = True
            res += 1
            dfs(i-1, j)
            dfs(i+1, j)
            dfs(i, j+1)
            dfs(i, j-1)
    dfs(0,0)
    print(res)


'''
3
1 1 0
2 3 1
2 3 2

'''


