
def oneIter():
    n, m, q = [int(i) for i in input().split(' ')]
    A = []
    Q = []
    for i in range(n):
        A.append([int(i) for i in input().split(' ')])
    # for i in range(q):
    #     Q.append([int(i) for i in input().split(' ')])
    row=[0]*n  # 求行的公差
    col=[0]*m  # 求列的公差
    numRow=[-1]*n # 求该行的一个数的索引
    numCol=[-1]*m # 求该列的一个数的索引
    for i in range(n):
        for j in range(m):
            if A[i][j]:
                p=j
                numRow[i]=j
                for j in range(j+1,m):
                    if A[i][j]:
                        row[i]=(A[i][j]-A[i][p])//(j-p)
                        for j in range(m):
                            if not A[i][j]:
                                A[i][j]=A[i][numRow[i]] + ((j - numRow[i]) * row[i])
                        break
                break
    for i in range(m):
        for j in range(n):
            if A[j][i]:
                p = j
                numCol[i]=j
                for j in range(j + 1, n):
                    if A[j][i]:
                        col[i]=(A[j][i]-A[p][i])//(j-p)
                        for j in range(n):
                            if not A[j][i]:
                                A[j][i]=A[numCol[i]][i] + ((j - numCol[i]) * col[i])
                        break
                break

    for a in A:
        print(a)
    for i,j in Q:
        i=i-1
        j=j-1
        if row[i]==-1 and col[j]==-1:
            print('Unknown')
        else:
            print(A[i][j])


n, m, q = [int(i) for i in input().split(' ')]
A = []
Q = []
for i in range(n):
    A.append([int(i) for i in input().split(' ')])
for i in range(q):
    Q.append([int(i) for i in input().split(' ')])
row=[False]*n  # 记录该行是否公差可求
col=[False]*m  # 记录该列是否公差可求
for time in range(2):
    for i in range(n):
        for j in range(m):
            if A[i][j]:
                p = j
                for j in range(j + 1, m):
                    if A[i][j]:
                        d = (A[i][j] - A[i][p]) // (j - p)
                        row[i]=True
                        for j in range(m):
                            if not A[i][j]:
                                A[i][j] = A[i][p] + ((j - p) * d)
                        break
                break
    for i in range(m):
        for j in range(n):
            if A[j][i]:
                p = j
                for j in range(j + 1, n):
                    if A[j][i]:
                        d = (A[j][i] - A[p][i]) // (j - p)
                        col[i]=True
                        for j in range(n):
                            if not A[j][i]:
                                A[j][i] = A[p][i] + ((j - p) * d)
                        break
                break
for a in A:
    print(a)

for i, j in Q:
    if row[i-1] or col[i-1] or  A[i-1][j-1]:
        print(A[i-1][j-1])
    else:
        print('Unknown')


'''

3 3 6
1 0 5
2 0 0
0 0 7
1 1
1 2
1 3
2 1
2 2
2 3


2 3 6
1 0 3
0 0 0
1 1
1 2
1 3
2 1
2 2
2 3


4 4 0
4 5 0 0
9 0 0 0
0 0 24 0
0 0 0 0
'''


