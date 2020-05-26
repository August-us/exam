'''
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
 条件 |示例 1|示例 2
 -|-|-|
输入| "babad"|"cbbd"
输出| "bab"|"bb"
注意| "aba" 也是一个有效答案。
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxLength=''
        for center in range(len(s)):
            radius=0
            while radius<min(center+1, len(s)-center-1) and s[center-radius]==s[center+radius+1]:
                radius+=1
            if 2 * radius + 1 > len(maxLength):
                maxLength = s[center - radius + 1:center + radius + 1]
            radius=0
            while radius<min(center, len(s)-center-1) and s[center-radius-1]==s[center+radius+1]:
                    radius+=1
            if 2 * radius + 1 > len(maxLength):
                maxLength = s[center - radius:center + radius + 1]
        return maxLength

def longestPalindromeSubSequence(s):
    # 最大回文子串长度
    s = "abcda"
    maxLength = s[0]
    length = len(s)
    dp = [[False] * (length + 1) for i in range(length + 1)]
    for j in range(length - 1, -1, -1):
        dp[j][j] = True
        dp[j - 1][j] = (s[j - 1] == s[j])
        for i in range(j - 1, -1, -1):
            if s[i] == s[j]:
                if dp[i + 1][j - 1]:
                    dp[i][j] = True
                    if j - i + 1 > len(maxLength):
                        maxLength = s[i:j + 1]
    return dp[0][length - 1], maxLength


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

def longestPalindromeSubSequence_lcs(s):
    lena = len(s)
    b=s[::-1]
    Maxstr=''
    c = [[0 for i in range(lena + 1)] for j in range(lena + 1)]
    for i in range(lena):
        for j in range(lena):
            if s[i] == b[j] :
                c[i + 1][j + 1] = c[i][j] + 1
                cur=c[i+1][j+1]
                if cur>len(Maxstr) and i+j-cur==lena-2:
                    Maxstr=s[i-cur+1:i+1]
            else:
                c[i + 1][j + 1] = 0
    return Maxstr

s="bcbbc"
s = 'aab'
print (NumOfPalindromeSubSequence(s))
print (longestPalindromeSubSequence(s))
print(Solution().longestPalindrome(s))
