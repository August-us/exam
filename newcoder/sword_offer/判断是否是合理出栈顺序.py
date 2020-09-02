# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        stack=[]
        nextPush=0
        for i in range(len(popV)):
            tmp=popV[i]
            if stack and stack[-1]==tmp:
                stack.pop()
            else:
                try:
                    k=pushV.index(tmp,nextPush)
                except ValueError:
                    return False
                stack.extend(pushV[nextPush:k])
                nextPush=k+1
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
import random
pushV=list(range(1000000))
popV=list(range(1000000))
random.shuffle(popV)
start=time()
print(Solution().IsPopOrder(pushV,popV))
print(time()-start)
start=time()
print(Solution2().IsPopOrder(pushV,popV))
print(time()-start)


