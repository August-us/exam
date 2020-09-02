'''
将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。
比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：
L   C   I   R
E T O E S I I G
E   D   H   N
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。
'''
class Solution1:
    def convert(self, s: str, numRows: int) -> str:
        if numRows<2:return s
        res=['' for i in range(numRows)]
        circul=2*numRows-2
        s+=' '*(circul-len(s)%circul)
        T=len(s)//circul
        for row in range(numRows):
            if row==0 or row==numRows-1:
                res[row]=''.join([s[i*circul+row] for i in range(T)]).strip()
            else:
                res[row]=''.join([s[row+i*circul]+s[(i+1)*circul-row]for i in range(T)]).strip()

        return ''.join(res)

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2: return s
        res = ["" for _ in range(numRows)]
        i, flag = 0, -1
        for c in s:
            res[i] += c
            if i == 0 or i == numRows - 1: flag = -flag
            i += flag

        return "".join(res)




from TestCase import alpha
import numpy as np
alpha=np.array(list(alpha[len(alpha)//2:]))
s=''.join(alpha[np.random.randint(0,26,100000)])
from time import time
start=time()
(Solution1().convert(s,3))
print(time()-start)
start=time()
(Solution().convert(s,3))
print(time()-start)
