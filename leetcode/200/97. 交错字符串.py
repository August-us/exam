'''
给定三个字符串 s1, s2, s3, 验证 s3 是否是由 s1 和 s2 交错组成的。

示例 1:

输入: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
输出: true
示例 2:

输入: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
输出: false

这个问题应当采用动态规划的形式，但是感觉动态规划需要计算的量过于多
'''

class Solution:
    def isInterleave_recurse(self, s1: str, s2: str, s3: str) -> bool:
        l1=len(s1)-1
        l2=len(s2)-1
        k=len(s3)-1
        while l1>=0 and 0<=l2:
           if s3[k]==s1[l1]:
               if s3[k] == s2[l2]:
                   return self.isInterleave(s1[:l1],s2[:l2+1],s3[:k]) or self.isInterleave(s1[:l1+1],s2[:l2],s3[:k])
               else:
                    l1-=1
           elif s3[k]==s2[l2]:
               l2-=1
           else:
               return False
           k-=1
        if l1>=0:return s3[:k+1]==s1[:l1+1]
        else: return s3[:k+1]==s2[:l2+1]

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        self.s1=s1
        self.s2=s2
        self.s3=s3
        self.dp={}
        return self.interLeave(len(s1)-1,len(s2)-1)  if len(s1)+len(s2)==len(s3) else False

    def interLeave(self, end1, end2):
        if (end1, end2) in self.dp: return self.dp[(end1, end2)]
        k = end1 + end2 + 1
        while end1 >= 0 and 0 <= end2:
            if self.s3[k] == self.s1[end1]:
                if self.s3[k] == self.s2[end2]:
                    self.dp[(end1, end2)]=self.interLeave(end1-1,end2) or self.interLeave(end1,end2-1)
                    return self.dp[(end1, end2)]
                else:
                    end1 -= 1
            elif self.s3[k] == self.s2[end2]:
                end2 -= 1
            else:
                self.dp[(end1, end2)]=False
                return False
            k -= 1
        if end1 >= 0:
            self.dp[(end1, end2)]=self.s3[:k + 1] == self.s1[:end1 + 1]
        else:
            self.dp[(end1, end2)]= self.s3[:k + 1] == self.s2[:end2 + 1]
        return self.dp[(end1, end2)]





print(Solution().isInterleave(
'a'*10,
'a'*10,
'a'*20,
))