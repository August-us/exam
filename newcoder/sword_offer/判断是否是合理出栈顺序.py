# -*- coding:utf-8 -*-
# 这道题目可以从入栈序列入手，也可以从出栈序列入手，显然出栈顺序可以加速，但是不能降低复杂度
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        stack=[]
        last=0
        for i in range(len(popV)):
            tmp=popV[i]
            if stack and stack[-1]==tmp:
                stack.pop()
            else:
                try:
                    k=pushV.index(tmp,last)
                except ValueError:
                    return False
                stack.extend(pushV[last:k])
            last=k+1
        if not stack:
            return True


class Solution1:
    def IsPopOrder(self, pushV, popV):
        # write code here
        if not pushV or len(pushV) != len(popV):
            return False
        stack = []
        for i in pushV:
            stack.append(i)
            while len(stack) and stack[-1] == popV[0]:
                stack.pop()
                popV.pop(0)
        if len(stack):
            return False
        return True

from time import time
start=time()
print(Solution1().IsPopOrder(list(range(100000)),list(range(100000))))
print(time()-start)

