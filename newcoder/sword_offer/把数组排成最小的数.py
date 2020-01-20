'''
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。例如输入数组
{3，32，321}，则打印出这三个数字能排成的最小数字为321323。
'''
import functools
class Solution:
    def PrintMinNumber(self, numbers):
        if not numbers:
            return ''
        sL=[str(i) for i in numbers]
        l=len(max(sL,key=len))
        sL=sorted(sL,key=lambda x:x*(l//len(x))+x[:l-l//len(x)*len(x)])
        return ''.join(sL)
class Solution1:
    def PrintMinNumber(self, numbers):
        # write code here
        if not numbers:
            return ""
        lmb = lambda n1, n2:int(str(n1)+str(n2))-int(str(n2)+str(n1))
        array = sorted(numbers, key=functools.cmp_to_key(lmb))
        return ''.join([str(i) for i in array])

from time import time
from random import sample
a=sample(range(1,100000),50000)
start=time()
print(Solution().PrintMinNumber(a))
print(time()-start)
start=time()
print(Solution1().PrintMinNumber(a))
print(time()-start)