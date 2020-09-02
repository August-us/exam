# -*- coding:utf-8 -*-
from functools import reduce

def LastRemaining_Solution(n, m):
    # write code here
    # 用列表来模拟环，新建列表range(n)，是n个小朋友的编号
    if not n or not m:
        return -1
    lis = list(range(n))
    i = 0
    while len(lis) > 1:
        i = (m - 1 + i) % len(lis)  # 递推公式
        lis.pop(i)
    return lis[0]

def LastRemaining(n, m):# write code here
    if n<1 or m<1:
        return -1
    last=0
    for i in range(2,n+1):
        last=(last+m)%i
    return last
    # return   reduce(lambda x, y: (x + m) % y,range(2,n+1),0)  # 一行解法

print(LastRemaining_Solution(10,3))
