import numpy as np

def score(A):
    print(A)
    return np.abs(np.diff(np.array([0]+A))).sum()

def dp(A):
    res=[[0 for i in range(len(A))] for j in range(len(A))]
    sel=[[0 for i in range(len(A))] for j in range(len(A))]
    for i in range(len(A)):
        res[i][i]=A[i]
        sel[i][i]=A[i]
    return res
print(dp([1,2,3,4]))

'''
#  马贼分金

如果先手拿走ai，那么先手可以得到的最大的价值是：
a(i) + sum(i + 1, j) - f(i + 1, j) => sum(i, j) - f(i + 1, j)
因为先手拿走a(i)后，后手就会在i + 1, j中取元素，因此双方都要按照最佳的策略取，因此后手也会在ai+1, ... aj的序列上取得最大值，这个时候我们可以把在ai, ai+1, ... aj上的后手看做在i + 1, ...j上的先手能取得最大的价值。

同理，如果先手拿走aj，那么先手可以得到的最大的价值是：
a(j) + sum(i, j - 1) - f(i, j - 1) => sum(i, j) - f(i, j - 1)

由此我们推出状态转移方程：
f(i, j) = max{sum(i, j) - f(i + 1, j), sum(i, j) - f(i, j - 1)}
=>
f(i, j) = sum(i, j) - min{f(i + 1, j), f(i, j - 1)}
0 <= i <= j <= L
其中L表示序列的总长度
f(i, j) = sum(i, j) 当 i == j时

最后，关于sum(i, j)的计算其实不需要使用二维数组来存储，因此这样非常浪费存储空间，类似的存储通常会采用下列的方式：
sum'(k)表示从数列开始(通常建议从1开始)到k位置的所有的元素的和
sum'(k) = sum'(k - 1) + a[k] (k >= 1, sum'[0] = 0_
那么sum(i, j) = sum'(j) - sum'(i - 1) (i >= 1)

通常，动态规划的代码都比较简短，其关键是分析问题，抽象模型，划分阶段，设计状态和决策。
'''
import sys

def main():
    case = map(int, sys.stdin.readline().strip().split())[0]
    for c in range(case):
        n = map(int, sys.stdin.readline().strip().split())[0]
        au = map(int, sys.stdin.readline().strip().split())

        f = [[0 for i in range(n + 1)] for j in range(n + 1)]
        sum = [0 for i in range(n + 1)]

        for i in range(1, n + 1):
            sum[i] = sum[i - 1] + au[i - 1]
            f[i][i] = au[i - 1]  # 注意状态的初始化

        for j in range(n):
            for i in range(1, n):
                if i + j <= n:
                    f[i][i + j] = sum[i + j] - sum[i - 1] - min(f[i + 1][i + j], f[i][i + j - 1])

        print ('Case #%d: %d %d'%(c + 1, f[1][n], sum[n] - f[1][n]))


if __name__ == '__main__':
    main()

