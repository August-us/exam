from typing import List
'''
所有 DNA 都由一系列缩写为 A，C，G 和 T 的核苷酸组成，例如：“ACGAATTCCG”。在研究 DNA 时，识别 DNA 中的重复序列有时会对研究非常有帮助。
编写一个函数来查找目标子串，目标子串的长度为 10，且在 DNA 字符串 s 中出现次数超过一次。
出现多次只需要输出一次
示例：
输入：s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
输出：["AAAAACCCCC", "CCCCCAAAAA"]
'''


class Solution:
    def findRepeatedDnaSequences_slice(self, s: str) -> List[str]:
        tmp = set()
        res = set()
        for i in range(10, len(s)+1,1):
            if s[i-10:i] in tmp:
                res.add(s[i-10:i])
            else:
                tmp.add(s[i-10:i])
        return list(res)
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        '''使用编码转换成数字来判断是否出现过'''
        DNAmap = {'A': '0', 'C': '1', 'G': '2', 'T': '3'}
        DNA = ''.join(map(lambda x: DNAmap[x], s))
        pre = set()
        r = set()
        res = []
        for i in range(10, len(DNA)+1, 1):
            cur = int(DNA[i - 10:i], base=4)
            if cur in pre and cur not in r:
                r.add(cur)
                res.append(s[i-10:i])
            else:
                pre.add(cur)
        return res
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        '''使用位运算来模拟移位和滑动窗口，如果是四进制其实可以通过模和乘法实现位运算'''
        DNAmap = {'A': '00', 'C': '01', 'G': '10', 'T': '11'}
        DNA = ''.join(map(lambda x: DNAmap[x], s))
        pre = set()
        r = set()
        res = []
        cur = int(DNA[:18], base=2) if len(DNA)>18 else 0
        for i in range(20,len(DNA)+1,2):
            cur = cur<<2 | int(DNA[i-2:i], base=2)
            if cur not in pre:
                pre.add(cur)
            elif cur not in r:
                r.add(cur)
                res.append(s[i//2-10:i//2])
            cur &= 0x3ffff
        return res

s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
s = "AAAAAAAAAAA"
print(Solution().findRepeatedDnaSequences(s))


