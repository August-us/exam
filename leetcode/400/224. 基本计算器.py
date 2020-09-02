from operator import add, sub, mul, floordiv


'''
实现一个基本的计算器来计算一个简单的字符串表达式的值。

字符串表达式可以包含左括号 ( ，右括号 )，加号 + ，减号 -，非负整数和空格  。

示例 1:

输入: "1 + 1"
输出: 2
示例 2:

输入: " 2-1 + 2 "
输出: 3
示例 3:

输入: "(1+(4+5+2)-3)+(6+8)"
输出: 23
'''
class Solution:
    def calculate(self, s: str) -> int:
        '''
        使用双栈的方式，为了避免陷入判断的泥潭，需要每次运算完成后，不管什么情况，都把结果入栈

        '''''
        num_stack = []
        opear_stack = []
        opeard = {'+': add, '-': sub}
        level = {')': 1, '+': 1, '-': 1, '(': 2, '$': 0}
        i = n = 0
        s += '$'
        for i, c in enumerate(s):
            if c == ' ':
                continue
            if c.isdigit():
                n = n * 10 + int(c)
                if not s[i + 1].isdigit():
                    num_stack.append(n)
                    n = 0
            else:
                if not opear_stack or level[opear_stack[-1]] < level[c]:
                    opear_stack.append(c)
                else:
                    while opear_stack[-1] != '(':
                        n1 = num_stack.pop()
                        num = num_stack.pop()
                        o = opear_stack.pop()
                        num_stack.append(opeard[o](num, n1))
                    if c == ')':
                        opear_stack.pop()
                    else:
                        opear_stack.append(c)

        return num_stack[-1]

    def calculate(self, s: str) -> int:
        '''
        双栈的方法比较通用，因为只涉及加减法，可以把问题    简化，只需要将第一个操作数当做正数，然后后面就每次加上一个符号数。
        遇到括号就把符号和操作数一起入栈，遇到右括号，再逐步出栈
        '''
        stack = []
        sign = 1
        n = num = 0
        for c in s:
            if c == ' ':
                continue
            if c.isdigit():
                n = n * 10 + int(c)
            elif c == '(':
                stack.append((sign, num))
                num = 0
                sign = 1
                n = 0
            else:
                num += sign * n
                if c == ')':
                    sign, n = stack.pop()
                    num = n + sign * num
                else:
                    sign = 1 if c == '+' else -1
                n = 0
        num += sign * n
        return num


print(Solution().calculate("1+1"))
'''
227
实现一个基本的计算器来计算一个简单的字符串表达式的值。

字符串表达式仅包含非负整数，+， - ，*，/ 四种运算符和空格  。 整数除法仅保留整数部分。

示例 1:

输入: "3+2*2"
输出: 7
示例 2:

输入: " 3/2 "
输出: 1
示例 3:

输入: " 3+5 / 2 "
输出: 5
'''


class Solution:
    def calculate(self, s: str) -> int:
        num_stack, opera_stack = [], []
        level = {'+':1, '-':1, '*':2, '/':2, '$':0}
        opear = {'+': add, '-': sub, '*': mul, '/': floordiv}
        n = 0
        def appendNum(n, c):
            if not opera_stack or level[opera_stack[-1]] < level[c]:
                num_stack.append(n)
                opera_stack.append(c)
            else:
                n = opear[opera_stack.pop()](num_stack.pop(), n)
                appendNum(n, c)
        for c in s:
            if c == ' ':
                continue
            if c.isalnum():
                n = n*10 + int(c)
            else:
                appendNum(n, c)
                n = 0
        if n:
            appendNum(n, '$')
            return num_stack[-1]
        return 0
print(Solution().calculate(" 3"))