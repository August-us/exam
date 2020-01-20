from functools import reduce
from itertools import permutations

class Solution:
    prim = [2, 3, 5, 7, 11]
    def primeFactorization(self, tsum):
        for i in range(self.prim[-1]+1,int(tsum**0.5)):
            flag=True
            for j in self.prim:
                if i%j==0:
                    flag=False
                    break
            if flag:
                self.prim.append(i)
        i=0
        fac=[]
        while i<len(self.prim):
            if tsum%self.prim[i]:
                i+=1
                continue
            fac.append(self.prim[i])
            tsum/=self.prim[i]
        return fac

    def FindContinuousSequence(self, tsum):
        fac=self.primeFactorization(tsum)
        odd=[i for i in fac if i%2]
        fact=set()
        res=[]
        mul=lambda x,y:x*y
        for i in range(len(odd)):
            l=permutations(odd,i+1)
            for j in l:
                a=reduce(mul,j)
                fact.add(a)
                fact.add((tsum<<1)//a)
        fact=sorted(list(fact))
        for i in fact:
            j=tsum*2//i
            if i<j+1:
                continue
            res.append(list(range((i-j+1)>>1,(i+j+1)>>1)))
        return res
class Solution1:
    def FindContinuousSequence(self, tsum):
        if tsum < 3:
            return []
        small = 1
        big = 2
        middle = (tsum + 1)>>1
        curSum = small + big
        output = []
        while small < middle:
            if curSum == tsum:
                output.append(range(small, big+1))
                big += 1
                curSum += big
            elif curSum > tsum:
                curSum -= small
                small += 1
            else:
                big += 1
                curSum += big
        return output

class Solution2:
    def FindContinuousSequence(self, tsum):
        # write code here
        res=[]
        for i in range(1,tsum//2+1):
            for j in range(i,tsum//2+2):
                tmp=(j+i)*(j-i+1)/2
                if tmp>tsum:
                    break
                elif tmp==tsum:
                    res.append(range(i,j+1))
        return res
import random
from time import time

# a=random.randint(1,2**32-10)
a=random.sample(range(1,2**32-1),1)
start=time()
for i in a:
    Solution().FindContinuousSequence(i)
print(time()-start)

start=time()
for i in a:
    Solution2().FindContinuousSequence(i)
print(time()-start)
