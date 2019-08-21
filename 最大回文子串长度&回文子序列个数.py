
def NumOfPalindromeSubSequence(str):
    #回文子序列个数
    length = len(str)
    dp = [[0] * (length + 1) for i in range(length + 1)]
    for j in range(length):
        dp[j][j] = 1
        for i in range(j - 1, -1, -1):
            dp[i][j] = dp[i + 1][j] + dp[i][j - 1] - dp[i + 1][j - 1]
            if str[i] == str[j]:
                dp[i][j] += 1 + dp[i + 1][j - 1]

    return dp[0][length - 1]


def longestPalindromeSubSequence(str):
    #最大回文子串长度
    length = len(str)
    dp = [[0] * (length + 1) for i in range(length + 1)]
    for j in range(length):
        dp[j][j] = 1
        for i in range(j - 1, -1, -1):
            dp[i][j] = dp[i + 1][j] + dp[i][j - 1] - dp[i + 1][j - 1]
            if str[i] == str[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:dp[i][j]=max(dp[i+1][j],dp[i][j-1])
    return dp[0][length - 1]
s=input()
print (NumOfPalindromeSubSequence(s))
print (longestPalindromeSubSequence(s))