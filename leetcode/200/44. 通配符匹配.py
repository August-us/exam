
'''
给定一个字符串 (s) 和一个字符模式 (p) ，实现一个支持 '?' 和 '*' 的通配符匹配。
'?' 可以匹配任何单个字符。
'*' 可以匹配任意字符串（包括空字符串）。
两个字符串完全匹配才算匹配成功。

说明:
s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母，以及字符 ? 和 *。

示例 1:
输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。

示例 2:
输入:
s = "aa"
p = "*"
输出: true
解释: '*' 可以匹配任意字符串。

示例 3:
输入:
s = "cb"
p = "?a"
输出: false
解释: '?' 可以匹配 'c', 但第二个 'a' 无法匹配 'b'。

示例 4:
输入:
s = "adceb"
p = "*a*b"
输出: true
解释: 第一个 '*' 可以匹配空字符串, 第二个 '*' 可以匹配字符串 "dce".

示例 5:
输入:
s = "acdcb"
p = "a*c?b"
输入: false
'''
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # 递归法，让每一个*匹配剩下的所有可能
        i=j=0
        lenp,lens=len(p),len(s)
        if p==s or p=='*':return True
        if '*' not in p and lens!=lenp:return False
        while i<lenp:
            if p[i]=='*':
                while i+1<lenp and p[i+1]=='*':
                    i+=1
                for j in range(j,len(s)+1):
                    if self.isMatch(s[j:],p[i+1:]):
                        return True
                if j==lens: return i==lenp-1
                return False
            if j<lens and (p[i]=='?' or p[i]==s[j]):
                i+=1
                j+=1
            else:return False
        return j==lens

    def isMatch2(self, s: str, p: str) -> bool:
        # 递归法，用状态转移来让每一个*匹配剩下的所有可能

        i=j=0
        lenp,lens=len(p),len(s)
        if p==s or p=='*':return True
        if '*' not in p and lens!=lenp:return False
        while i<lenp:
            if p[i]=='*':
                return self.isMatch2(s[j:],p[i+1:]) or self.isMatch2(s[j+1:],p[i+1:]) or self.isMatch2(s[j+1:],p[i:])
            if j<lens and (p[i]=='?' or p[i]==s[j]):
                i+=1
                j+=1
            else:return False
        return j==lens

    def isMatch_backtrack(self, s: str, p: str) -> bool:
        # 回溯法每次最多一回溯一个*，但是如果采用递归的话，就能回溯多个*,这是不必要的
        s_idx=p_idx=0
        lenp,lens=len(p),len(s)
        start_idx=tmp_idx=-1
        while s_idx<lens:
            if  p_idx<lenp  and (p[p_idx]== '?' or p[p_idx]==s[s_idx]):
                s_idx+=1
                p_idx+=1
            elif p_idx<lenp and p[p_idx]== '*':
                while p_idx+1<lenp and p[p_idx + 1]== '*':
                    p_idx+=1

                start_idx=p_idx  # 记录*出现的位置,同时初始化的时候保证*不匹配字符
                tmp_idx=s_idx
                p_idx+=1

            elif start_idx==-1:
                return False
            else:
                # 回溯，让p_idx和s_idx都回溯，并且每次回溯，*多匹配一个字符
                p_idx=start_idx+1
                s_idx=tmp_idx+1
                tmp_idx=s_idx
        return all(x=='*' for x in p[p_idx:])

    def isMatch_dp(self, s: str, p: str) -> bool:
        # 动态规划，空间复杂度可以优化到O(min(S,P))
        lenp,lens=len(p),len(s)
        dp=[[False]*(lens+1) for i in range(lenp+1)]
        dp[0][0]=True
        if p==s or p=='*':return True
        for i in range(1,lenp+1):
            for j in range(lens+1):
                if p[i-1] == '*' and dp[i - 1][j]:
                    dp[i][j:]=[True]*(lens-j+1)
                    break
                if j>0:
                    dp[i][j]=dp[i-1][j-1] and (p[i-1]==s[j-1] or p[i-1]=='?')
        return dp[lenp][lens]


# s="babbbbaabababaabbababaababaabbaabababbaaababbababaaaaaabbabaaaabababbabbababbbaaaababbbabbbbbbbbbbaabbb"
# p="b**bb**a**bba*b**a*bbb**aba***babbb*aa****aabb*bbb***a"
s="a"
p="aa"

print(Solution().isMatch_dp(s,p))