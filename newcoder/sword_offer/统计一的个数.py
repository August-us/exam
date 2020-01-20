# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution1(self, n):
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

print(Solution().NumberOf1Between1AndN_Solution(11111))
