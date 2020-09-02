from collections import defaultdict
from typing import List

class Solution5:
    '''
    给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
     条件 |示例 1|示例 2
     -|-|-|
    输入| "babad"|"cbbd"
    输出| "bab"|"bb"
    注意| "aba" 也是一个有效答案。
    '''''
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

    def longestPalindromeSubSequence(self,s):
        # 最大回文子串长度,通过dp_{ij}判断s[i:j+1]是否是回文串
        maxLength = s[0]
        length = len(s)
        dp = [[False] * (length) for i in range(length)]
        for i in range(length): dp[i][i] = True
        for j in range(1, length): dp[j - 1][j] = (s[j - 1] == s[j])
        for gap in range(2, length):
            for i in range(0, length - gap):
                j = i + gap
                if s[i] == s[j]:
                    if dp[i + 1][j - 1]:
                        dp[i][j] = True
                        if j - i + 1 > len(maxLength):
                            maxLength = s[i:j + 1]
        return dp[0][length - 1], maxLength

    def longestPalindromeSubSequence_lcs(self,s):
        lena = len(s)
        b = s[::-1]
        Maxstr = ''
        c = [[0 for i in range(lena + 1)] for j in range(lena + 1)]
        for i in range(lena):
            for j in range(lena):
                if s[i] == b[j]:
                    c[i + 1][j + 1] = c[i][j] + 1
                    cur = c[i + 1][j + 1]
                    if cur > len(Maxstr) and i + j - cur == lena - 2:
                        Maxstr = s[i - cur + 1:i + 1]
                else:
                    c[i + 1][j + 1] = 0
        return Maxstr

class Solution131:
    '''
    给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。
    
    返回 s 所有可能的分割方案。
    
    示例:
    
    输入: "aab"
    输出:
    [
      ["aa","b"],
      ["a","a","b"]
    ]
    '''''
    def partition(self, s: str) -> List[List[str]]:
        keys = set()  # 保存回文串的起始和终止元组
        for gap in range(1,len(s)):
            for beg in range(len(s)-gap):
                end = beg + gap
                i = 0
                while beg + i < end - i:
                    if s[beg + i] == s[end - i]:
                        i += 1
                    else:
                        break
                else:
                    keys.add((beg, end))
        res = [[[]]]
        print(s[0:4],s[3:0:-1])
        keys = sorted(keys,key=lambda x:x[1]) +[(0,len(s))]
        k = 0
        for i in range(1,len(s) + 1):
            res.append([pre+ list(s[i-1]) for pre in res[i-1]])
            while keys[k][1] == i-1:
                # print(list(s[keys[k][0]:i]))
                res[i].extend([pre + [s[keys[k][0]:i]] for pre in res[keys[k][0]]])
                k +=1
        return res[-1]

    # 同样的思路，同样的动态规划，别人的思路就是写的简单
    def partition_forward(self, s: str) -> List[List[str]]:
        dp = [[] for _ in range(len(s) + 1)]
        dp[-1] = [[]]
        for end in range(1,len(s)+1):
            for start in range(end):
                if s[start:end] == s[start:end][::-1]:
                    for each in dp[start-1]:
                        dp[end-1].append(each+[s[start:end]])
        return dp[len(s)-1]
    # 从前往后计算下标需要平移,比较麻烦,可以考虑从后往前计算


    def partition_dfsWithDp(self, s: str) -> List[List[str]]:
            n = len(s)
            dp = [[False] * n for _ in range(n)]

            for i in range(n):
                for j in range(i + 1):
                    if (s[i] == s[j]) and (i - j <= 2 or dp[j + 1][i - 1]):
                        dp[j][i] = True
            # print(dp)
            res = []
            def helper(i, tmp):
                if i == n:
                    res.append(tmp)
                for j in range(i, n):
                    if dp[i][j]:
                        helper(j + 1, tmp + [s[i: j + 1]])
            helper(0, [])
            return res

    def partition_dfs(self, s: str) -> List[List[str]]:
        res = []

        def dfs(start, tmp):
            if start == len(s):
                res.append(tmp)
            for i in range(start+1, len(s) + 1):
                if s[start:i] == s[start:i][::-1]:  # 如果start 到 i 是回文串，则进行深度遍历
                    dfs(i, tmp + [s[start:i]])
        dfs(0, [])
        return res


class Solution132:
    def minCut_usesort(self, s: str) -> int:
        # 先找出所有的回文串，使用回文串可以减少分割次数，需要对回文串按照结束的位置排序
        length = len(s)
        keys = {(0,0)}
        for j in range(1,length):
            keys.add((j,j))
            if s[j]==s[j-1]:keys.add((j-1,j))

        for gap in range(2, length):
            for i in range(0, length - gap):
                j = i + gap
                if s[i] == s[j] and (i+1,j-1) in keys:keys.add((i,j))

        dp = list(range(-1,len(s)))

        for k in sorted(keys,key=lambda x:x[1]):
            dp[k[1]+1] = min(dp[k[0]]+1,dp[k[1]+1])
        return dp[-1]

    def minCut(self, s: str) -> int:
        # 直接求以第j个字符结尾的字符串，并计算dp
        length = len(s)
        dp = list(range(-1,len(s)))
        pre = [True] + [False]*(length-1)
        for end in range(1,length):
            keys = [False if i!=end else True for i in range(length) ]
            dp[end+1] = dp[end] +1
            for beg in range(end):
                if s[beg] == s[end] and  (pre[beg+1] or beg+1==end):
                    dp[end+1] = min(dp[beg]+1,dp[end+1])
                    keys[beg] = True
            pre = keys

        return dp[-1]


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



s="bcbbc"
s ="abbab"
# print (NumOfPalindromeSubSequence(s))
# print (longestPalindromeSubSequence(s))
# print(Solution().longestPalindrome(s))

print(Solution131().partition("aab"))
# print(Solution132().minCut(s))