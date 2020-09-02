'''
有一叠扑克牌，每张牌介于1和10之间

有四种出牌方法：

单出1张
出2张对子
出五张顺子，如12345
出三连对子，如112233
给10个数，表示1-10每种牌有几张，问最少要多少次能出完
'''
class Solution1:
    def leastTimes(self,nums,begin=0):
        res=sum(nums[begin:])
        if not res:return 0
        if nums[begin]>0:
            if begin+2<10 and nums[begin]>1 and nums[begin+1]>1 and nums[begin+2]>1:
                for i in range(begin,begin+3):
                    nums[i]-=2
                res=min(1+self.leastTimes(nums,begin),res)
                for i in range(begin,begin+3):
                    nums[i]+=2

            if begin+4<10 and nums[begin+1] and nums[begin+2] and nums[begin+3] and nums[begin+4]:
                for i in range(begin, begin + 5):
                    nums[i] -= 1
                res=min(1+self.leastTimes(nums,begin),res)
                for i in range(begin, begin + 5):
                    nums[i] += 1
            if nums[begin]>1:
                nums[begin] -= 2
                return min(1+self.leastTimes(nums,begin),res)

            else :
                return min(res,1+self.leastTimes(nums,begin+1))
        else:
            return self.leastTimes(nums,begin+1)



a=[1,2,2,2,2,2,1,1,1,1]
import numpy as np
a=np.random.randint(0,5,10)
print(a)
print(Solution1().leastTimes(a))






