'''
给定一个字符串 S 和一个字符串 T，计算在 S 的子序列中 T 出现的个数。

一个字符串的一个子序列是指，通过删除一些（也可以不删除）字符且不干扰剩余字符相对位置所组成的新字符串。（例如，"ACE" 是 "ABCDE" 的一个子序列，而 "AEC" 不是）

题目数据保证答案符合 32 位带符号整数范围。

 

示例 1：

输入：S = "rabbbit", T = "rabbit"
输出：3
解释：

如下图所示, 有 3 种可以从 S 中得到 "rabbit" 的方案。
(上箭头符号 ^ 表示选取的字母)

rabbbit
^^^^ ^^
rabbbit
^^ ^^^^
rabbbit
^^^ ^^^
示例 2：

输入：S = "babgbag", T = "bag"
输出：5
解释：

如下图所示, 有 5 种可以从 S 中得到 "bag" 的方案。 
(上箭头符号 ^ 表示选取的字母)

babgbag
^^ ^
babgbag
^^    ^
babgbag
^    ^^
babgbag
  ^  ^^
babgbag
    ^^^

'''''

class Solution:
    def numDistinct_dpnm(self, s: str, t: str) -> int:
        if not s or not t:return 0
        res=[[0]*len(s) for i in range(len(t)+1)]
        res[-1] = [1]*len(s)


        for i in range(len(t)):
            res[i][i] = res[i-1][i-1] * int(s[i] == t[i])
            for j in range(i+1,len(s)):
                res[i][j] = int(s[j]==t[i]) * res[i - 1][j - 1]+res[i][j-1]
        return res[-2][-1]

    def numDistinct_copy(self, s: str, t: str) -> int:
        if not s or not t:return 0
        pre=[1]*len(s)
        for i in range(len(t)):
            res = [0] * len(s)
            for j in range(i,len(s)):
                res[j] = int(s[j]==t[i])*pre[j - 1]+res[j-1]
            pre=res.copy()
        return res[-1]

    def numDistinct(self, s: str, t: str) -> int:
        if not s or len(s)<len(t):return 0
        res=[[1]*len(s),[0]*len(s)]
        flag=1
        for i in range(len(t)):
            res[flag][i] = int(s[i] == t[i]) * res[1 - flag][i - 1]
            for j in range(i+1,len(s)):
                res[flag][j] = int(s[j]==t[i])*res[1-flag][j - 1]+res[flag][j-1]
            flag=1-flag
        return res[1-flag][-1]

s = "babgbag"
t = "bag"
print( Solution().numDistinct_copy("fff",
"ffff"))

