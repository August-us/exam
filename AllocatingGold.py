au = [int(i) for i in input().split(' ')]
n=len(au)

f = [[0 for i in range(n + 1)] for j in range(n + 1)]
sum = [0 for i in range(n + 1)]

for i in range(1, n + 1):
    sum[i] = sum[i - 1] + au[i - 1]
    f[i][i] = au[i - 1]

for j in range(n):
    for i in range(1, n):
        if i + j <= n:
            f[i][i + j] = sum[i + j] - sum[i - 1] - min(f[i + 1][i + j], f[i][i + j - 1])

print(f[1][n],sum[n] - f[1][n])

