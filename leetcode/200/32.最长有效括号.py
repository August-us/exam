'''
给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。

示例 1:
输入: "(()"
输出: 2
解释: 最长有效括号子串为 "()"

示例 2:
输入: ")()())"
输出: 4
解释: 最长有效括号子串为 "()()"
'''


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        maxLength=0
        stack=[-1]
        for i,c in enumerate(s):
            if c=='(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    maxLength=max(maxLength,i-stack[-1])
        return maxLength

    def longestValidParentheses_dp(self, s: str) -> int:
        if not s:return 0
        dp=[0]*len(s)
        maxLength=0
        for i in range(2,len(s)):
            if s[i] == ')':
                if s[i-1]=='(':
                    dp[i]=dp[i-2]+2 if i>1 else 2
                elif i-dp[i-1]>0 and s[i-dp[i-1]-1]=='(':
                    dp[i]=dp[i-1]+2
                    if i-dp[i-1]-1>0:
                        dp[i]+=dp[i-dp[i-1]-2]
                maxLength=max(maxLength,dp[i])
        return max(dp)

    def longestValidParentheses_twoscan(self, s: str) -> int:
        left=right=maxLength=0
        for c in s:
            if c=='(':
                left+=1
            else:
                right+=1
            if left==right:
                maxLength=max(right<<1,maxLength)
            elif right>left:
                left=right=0
        left = right = 0
        for c in s[::-1]:
            if c=='(':
                left+=1
            else:
                right+=1
            if left==right:
                maxLength=max(right<<1,maxLength)
            elif right<left:
                left=right=0
        return maxLength




s="(()"
print(Solution().longestValidParentheses_twoscan(s))