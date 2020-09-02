from operator import add, sub, mul
from typing import List
# 给定一个含有数字和运算符的字符串，为表达式添加括号，改变其运算优先级以求出不同的结果。你需要给出所有可能的组合的结果。有效的运算符号包含 +, - 以及 *
#  。
#
#  示例 1:
#
#  输入: "2-1-1"
# 输出: [0, 2]
# 解释:
# ((2-1)-1) = 0
# (2-(1-1)) = 2
#
#  示例 2:
#
#  输入: "2*3-4*5"
# 输出: [-34, -14, -10, -10, 10]
# 解释:
# (2*(3-(4*5))) = -34
# ((2*3)-(4*5)) = -14
# ((2*(3-4))*5) = -10
# (2*((3-4)*5)) = -10
# (((2*3)-4)*5) = 10

# print(Solution().productExceptSelf([1,2,3,4]))

from itertools import combinations
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        self.numStack = []
        self.opeatStack = ['+']
        n = 0
        for i, c in enumerate(input):
            if c.isdigit():
                n = n*10 + int(c)
                if i+1 == len(input) or not input[i + 1].isdigit():
                    self.numStack.append(n)
                    n = 0
            else:
                self.opeatStack.append(c)
        self.operator = {'+':add, '-':sub, '*':mul}
        self.res = {}

        return self.core(0, len(self.numStack))

    def compent(self, l, r, o):
        return [self.operator[o](x,y)for x in l for y in r]

    def core(self, l, r):
        if r<=1+l:
            return self.numStack[l:r]
        elif r==l+2:
            return [self.operator[self.opeatStack[r-1]](*self.numStack[l:r])]
        else:
            res = []
            for i in range(l,r-1):
                left = self.core(l,i+1)
                right = self.core(i+1,r)
                res.extend(self.compent(left, right, self.opeatStack[i+1]))
            self.res[(l,r)] = res
            return res

    def diffWaysToCompute_dp(self, input: str) -> List[int]:
        numStack = []
        self.opeatStack = ['+']
        n = 0
        for i, c in enumerate(input):
            if c.isdigit():
                n = n*10 + int(c)
                if i+1 == len(input) or not input[i + 1].isdigit():
                    numStack.append(n)
                    n = 0
            else:
                self.opeatStack.append(c)
        res = [[], [[i] for i in numStack]]
        self.operator = {'+':add, '-':sub, '*':mul}

        for gap in range(2, len(numStack)+1):
            res.append([])

            for start in range(len(numStack)-gap+1):
                res[gap].append([])

                for i in range(1, gap):
                    res[gap][start].extend(self.compent(res[i][start], res[gap-i][i+start], self.opeatStack[start+i]))
        return res[-1][0]



print(Solution().diffWaysToCompute_dp("2*3-4*5"))
