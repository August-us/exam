'''
给定两个整数，分别表示分数的分子 numerator 和分母 denominator，以字符串形式返回小数。

如果小数部分为循环小数，则将循环的部分括在括号内。

示例 1:

输入: numerator = 1, denominator = 2
输出: "0.5"
示例 2:

输入: numerator = 2, denominator = 1
输出: "2"
示例 3:

输入: numerator = 2, denominator = 3
输出: "0.(6)"
    '''''
class Solution:

    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        index = {}
        res = []
        if (numerator>=0) ^ (denominator>=0):res.append('-')
        numerator,denominator = abs(numerator),abs(denominator)
        if numerator > denominator:
            res.append(numerator // denominator)
            numerator = numerator % denominator
        else:
            res.append('0')
        if numerator: res.append('.')
        while numerator:
            index[numerator] = len(res)
            numerator = numerator * 10
            res.append(numerator // denominator)
            numerator = numerator % denominator
            if numerator in index:
                n = index[numerator]
                res = list(map(str,res))
                return ''.join(res[:n]) + "(" + ''.join(res[n:]) + ")"
        return ''.join(map(str,res))
print(Solution().fractionToDecimal( numerator = -50, denominator = 8))
