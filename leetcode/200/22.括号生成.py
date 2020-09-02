from typing import List
from functools import reduce

'''
给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。
例如，给出 n = 3，生成结果为：
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

'''
class Solution:
    # 动态规划
    def generateParenthesis(self, n: int) -> List[str]:
        dp=[[] for i in range(n+1)]
        dp[0]=['']
        for i in range(1,n+1):
            for j in range(i):
                dp[i].extend(self.compent(dp[j],dp[i-j-1]))
        return dp[i]

    def compent(self, l, r):
        # res=[]
        # for s1 in l:
        #     for s2 in r:
        #         res.append('('+s1+')'+s2 )
        # return res
        return reduce(lambda x,y:x+y,map(lambda x:['('+x+')'+i for i in r],l),[])
class Solution2:
    def generateParenthesis(self,n):
        ans=[]
        self.max=n
        self.backtrack(ans, "", 0, 0)
        return ans
    def backtrack(self, ans, cur, left, right):
        if left==self.max:
            ans.append(cur +')' * (self.max - right))
            return
        if(left<self.max):
            self.backtrack(ans, cur +'(', left + 1, right)
        if right<left:
            self.backtrack(ans, cur +')', left, right + 1)

class Solution1:
    def generateParenthesis(self,n):
        ans=[]
        left=right=0
        cur=[]
        while left<n:
            cur.append('(')
            left+=1
            if left==n:
                ans.append(''.join(cur)+')'*(n-right))
        return ans



dp=Solution2().generateParenthesis(3)
print(dp)

