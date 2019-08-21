import time
import numpy as np


def dpmaze():
    M, N, K = [int(num) for num in input().strip().split()]
    import time
    start = time.time()
    matrix = []
    for i in range(N):
        matrix.append(list(map(int, input().strip().split())))
    maze0 = np.array(matrix)
    maze1 = np.zeros((M, N))
    maze2 = np.zeros((M, N))
    it = 0
    for k in range(K):
        while True:
            for i in range(M):
                for j in range(N):
                    if i - 1 >= 0 and maze0[i - 1, j] > maze0[i, j]:
                        maze1[i, j] = max(maze1[i, j], 1 + maze2[i - 1, j])
                    if i + 1 < N and maze0[i + 1, j] > maze0[i, j]:
                        maze1[i, j] = max(maze1[i, j], 1 + maze2[i + 1, j])

                    if j - 1 > 0 and maze0[i, j - 1] > maze0[i, j]:
                        maze1[i, j] = max(maze1[i, j], 1 + maze2[i, j - 1])

                    if j + 1 < M and maze0[i, j + 1] > maze0[i, j]:
                        maze1[i, j] = max(maze1[i, j], 1 + maze2[i, j + 1])
                    it += 1

            if (maze1 == maze2).all():
                break
            maze2 = maze1.copy()
        for i in range(M):
            for j in range(N):
                if i - 1 >= 0 and maze0[i - 1, j] <= maze0[i, j]:
                    maze1[i, j] = max(maze1[i, j], 1 + maze2[i - 1, j])
                if i + 1 < N and maze0[i + 1, j] <= maze0[i, j]:
                    maze1[i, j] = max(maze1[i, j], 1 + maze2[i + 1, j])

                if j - 1 > 0 and maze0[i, j - 1] <= maze0[i, j]:
                    maze1[i, j] = max(maze1[i, j], 1 + maze2[i, j - 1])

                if j + 1 < M and maze0[i, j + 1] <= maze0[i, j]:
                    maze1[i, j] = max(maze1[i, j], 1 + maze2[i, j + 1])
                it += 1
    while True:
        for i in range(M):
            for j in range(N):
                if i - 1 >= 0 and maze0[i - 1, j] > maze0[i, j]:
                    maze1[i, j] = max(maze1[i, j], 1 + maze2[i - 1, j])
                if i + 1 < N and maze0[i + 1, j] > maze0[i, j]:
                    maze1[i, j] = max(maze1[i, j], 1 + maze2[i + 1, j])

                if j - 1 > 0 and maze0[i, j - 1] > maze0[i, j]:
                    maze1[i, j] = max(maze1[i, j], 1 + maze2[i, j - 1])

                if j + 1 < M and maze0[i, j + 1] > maze0[i, j]:
                    maze1[i, j] = max(maze1[i, j], 1 + maze2[i, j + 1])
                it += 1

        if (maze1 == maze2).all():
            break
        maze2 = maze1.copy()
    print((maze2 + 1))
    print(time.time() - start, it)

def maze():
    M, N, k = [int(num) for num in input().strip().split()]
    start = time.time()
    it=0
    matrix = []
    result=np.zeros((k+1,N,M))
    def dfs(x,y,k):
        global it
        it+=1
        if result[k,x,y]!=0:
            return  result[k,x,y]
        if y>0:
            if matrix[x][y]<matrix[x][y-1]:
                left_res=dfs(x,y-1,k)
            else:
                if k>0:
                    left_res=dfs(x,y-1,k-1)
                else:
                    left_res=0
        else:
            left_res = 0

        if y<M-1:
            if matrix[x][y]<matrix[x][y+1]:
                right_res=dfs(x,y+1,k)
            else:
                if k>0:
                    right_res = dfs( x, y + 1, k - 1)
                else:
                    right_res=0
        else:
            right_res=0

        if x>0:
            if matrix[x][y]<matrix[x-1][y]:
                up_res=dfs(x-1,y,k)
            else:
                if k>0:
                    up_res=dfs(x-1,y,k-1)
                else:
                    up_res=0
        else:
            up_res = 0

        if x<N-1:
            if matrix[x][y]<matrix[x+1][y]:
                down_res=dfs(x+1,y,k)
            else:
                if k>0:
                    down_res = dfs( x+1, y, k - 1)
                else:
                    down_res=0
        else:
            down_res=0
        result[k,x, y]=1 + max(left_res, up_res, right_res, down_res)
        return result[k,x,y]


    for i in range(N):
        matrix.append(list(map(int,input().strip().split())))
    res=0
    for i in range(N):
        for j in range(M):
            a=dfs(i,j,k)
            res=max(res,a)
    print(res)
    print(result)
    print(time.time()-start,it)

if __name__=='__main__':
    maze()
'''
迷宫问题：给定一个矩阵，如果一个数比它上下左右的数小，那么它可以跳到它的上下左右位置，如果周围的数不大于它，这种移动称为强制跳跃，一个m×n的矩阵
在有k次强制跳跃的机会下，最多可以走多远。
3 3 1
1 3 3
2 4 9
0 9 2
'''
'''
12 12 100
1 3 3 1 3 3 1 3 3 1 3 3
2 4 9 0 9 2 2 4 9 0 9 2
1 3 3 1 3 3 2 4 9 0 9 2
2 4 9 0 9 2 2 4 9 0 9 2
2 4 9 0 9 2 1 3 3 1 3 3
2 4 9 0 9 2 2 4 9 0 9 2
1 3 3 1 3 3 1 3 3 1 3 3
2 4 9 0 9 2 2 4 9 0 9 2
1 3 3 1 3 3 2 4 9 0 9 2
2 4 9 0 9 2 2 4 9 0 9 2
2 4 9 0 9 2 1 3 3 1 3 3
2 4 9 0 9 2 2 4 9 0 9 2
'''