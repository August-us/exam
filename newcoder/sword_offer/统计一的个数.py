# -*- coding:utf-8 -*-

'''
给定一个整数 n，计算所有小于等于 n 的非负整数中数字 1 出现的个数。 

 示例: 

输入: 13
输出: 6 
解释: 数字 1 出现在以下数字中: 1, 10, 11, 12, 13 。 
'''''
class Solution:
    def NumberOf1Between1AndN_Solution1(self, n:int):
        if n < 0:return 0
        tmp=n
        base=1
        res=0
        while tmp:
            last=tmp%10
            tmp//=10
            res+=tmp*base
            if last>1:
                res+=base
            elif last==1:
                res+=n%base+1
            base*=10
        return res

    def NumberOf1Between1AndN_Solution(self, n):
        count=0
        for i in [10**i for i in range(len(str(n)))]:
            count+=(n//(i*10))*i+min(max(n%(i*10)-i +1,0),i)
        return count

print(Solution().NumberOf1Between1AndN_Solution(13))
