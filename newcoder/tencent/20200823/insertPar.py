s = input()
lens = len(s)

dp = [[0 for i in range(lens)] for j in range(lens)]
for i in range(lens):dp[i][i]=1
for l in range(2, lens+1):
    for i in range(lens - l + 1):
        j = i + l - 1;
        dp[i][j] = float('inf')
        if ((s[i] == '[' and s[j] == ']') or (s[i] == '(' and s[j] == ')')):
            dp[i][j] = dp[i+1][j-1];

        for k in range(i,j):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j]);
print(dp[0][lens-1])