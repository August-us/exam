# -*- coding:utf-8 -*-
# 输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
# 如果需要对一个数的每一位进行操作，使用循环来进行移位操作通常也是一个好办法
# python表示补码需要用 n& 2**base-1
class Solution:
    def NumberOf1(self, n):
        # write code here
        if n<0:
            a=str(bin(n))
            return 33-a[::-1].find('1')-a.count('1')
        return str(bin(n)).count('1')

class Solution1:
    def NumberOf1(self, n):
        # write code here
        # from functools import reduce
        # return(reduce(lambda x,y:x+y,map(lambda x:n>>x&1,range(0,32))))
        return sum([(n>>i & 1) for i in range(0,32)])

class Solution2:
    def NumberOf1(self, n):
        # write code here
        if n<0:
            a=0xffffffff
            return str(bin(n&a)).count('1')
        return str(bin(n)).count('1')

a=Solution2()
from time import time
start=time()
for i in range(-10000,10000,1):
    a.NumberOf1(i)
print(time()-start)
# print(Solution1().NumberOf1(-1))