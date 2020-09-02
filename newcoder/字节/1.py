n, l, r = [int(i) for i in input().split(' ')]

l -= 1
MOD = int(1e9 + 7)
dp = [[0 for i in range(3)] for j in range(n + 1)]
dp[0][0] = 1
for i in range(n):
    for j in range(3):
        w = (r - j + 3) // 3 - (l - j + 3) // 3

        for k in range(3):
            dp[i + 1][(k + j) % 3] = (dp[i + 1][(k + j) % 3] + dp[i][j] * w) % MOD


print(dp[n][0])
