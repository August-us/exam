# 请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。例如，字符串"+100","5e2","-123","3.1416"和"-1E-16"都表示数值。 但是"12e","1a3.14","1.2.3","+-5"和"12e+4.3"都不是。
class Solution:
    def isInt(self, s):
        if not s:
            return False
        if s[0] == '+' or s[0] == '-':
            s = s[1:]
        for i in s:
            if i not in '0123456789 ':
                return False
        return True

    def isNumber(self, s: str) -> bool:
        if 'E' in s:
            s = s.split('E')
        elif 'e' in s:
            s = s.split('e')
        else:
            return self.isInt(s.replace('.', '', 1))
        s[0] = s[0].replace('.', '', 1)
        return self.isInt(s[0]) and self.isInt(s[1])
class Solution1:
    '''牛客提交版本'''
    def isNumber(self, s: str) -> bool:
        index = self.scanInt(s, 0)
        if not index:
            return False
        if index < len(s):
            if s[index] == '.':
                index = self.scanUnsignedInt(s, index + 1)
            if index == len(s): return True
            if s[index] == 'E' or s[index] == 'e':
                return True if self.scanInt(s, index + 1) == len(s) else False
        return index == len(s)

    def scanUnsignedInt(self, s, start):
        for i in range(start, len(s)):
            if s[i] not in '1234567890':
                return i
        return len(s)

    def scanInt(self, s, start):
        if start == len(s):
            return False
        if s[start] == '+' or s[start] == '-':
            return self.scanUnsignedInt(s, start + 1)
        return self.scanUnsignedInt(s, start)

class Solution2:
    '''leetcode提交版本'''
    def isNumber(self, s: str) -> bool:
        s=s.strip()
        if not s:return False
        oldIndex=int(s[0] in ['+','-'])
        index = self.scanInt(s, oldIndex)
        isNumber=(oldIndex!=index)
        if index < len(s) and  s[index] == '.':
            oldIndex=index
            index = self.scanUnsignedInt(s, index + 1)
            isNumber=isNumber or  index!=oldIndex+1
        if not isNumber:return False
        if index < len(s) and (s[index] == 'E' or s[index] == 'e'):
            return self.scanInt(s,index+1)==len(s)
        return index == len(s)

    def scanUnsignedInt(self, s, start):
        for i in range(start, len(s)):
            if s[i] not in '1234567890':
                return i
        return len(s)

    def scanInt(self, s, start):
        if start == len(s):
            return False
        if s[start] == '+' or s[start] == '-':
            a=self.scanUnsignedInt(s, start + 1)
            if a==start+1:
                return start
            else:
                return a
        return self.scanUnsignedInt(s, start)

class DFA:
    '''
    有限状态机
    state	blank	+/-	0-9	.	e	other
    0	0	1	6	2	-1	-1
    1	-1	-1	6	2	-1	-1
    2	-1	-1	3	-1	-1	-1
    3	8	-1	3	-1	4	-1
    4	-1	7	5	-1	-1	-1
    5	8	-1	5	-1	-1	-1
    6	8	-1	6	3	4	-1
    7	-1	-1	5	-1	-1	-1
    8	8	-1	-1	-1	-1	-1

    '''
    def isNumber(self, s: str) -> bool:
        state=0
        finals=0b101101000 # 记录哪些状态可以正常退出，省略了遇到#的状态
        transfer=[
            [0, 1, 6, 2, -1],
            [-1, -1, 6, 2, -1],
            [-1, -1, 3, -1, -1],
            [8, -1, 3, -1, 4],
            [-1, 7, 5, -1, -1],
            [8, -1, 5, -1, -1],
            [8, -1, 6, 3, 4],
            [-1, -1, 5, -1, -1],
            [8, -1, -1, -1, -1],
        ]
        indentity={' ':0,'+':1,'-':1,'.':3,'e':4,'E':4}
        number=['0','1','2','3','4','5','6','7','8','9',]
        for char in s:
            if char in indentity:
                id=indentity[char]
            elif char in number:
                id=2
            else:return False
            state=transfer[state][id]
            if state<0:
                return False
        return (1<<state & finals)>0



a = ["+100", "5e2", "-123", "3.1416", "-1E-16", "12e", "1a3.14", "1.2.3", "+-5", "12e+4.3"]
a=['e9','.','1.','.1',"",'. 1','.e1','4e+','-1.','+.8','-.','+E3','6e6.5']
# a=["+.8"]
for i in a:
    print(i, DFA().isNumber(i))




