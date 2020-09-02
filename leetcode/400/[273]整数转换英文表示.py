# 将非负整数转换为其对应的英文表示。可以保证给定输入小于 231 - 1 。
#
#  示例 1:
#
#  输入: 123
# 输出: "One Hundred Twenty Three"
#
#
#  示例 2:
#
#  输入: 12345
# 输出: "Twelve Thousand Three Hundred Forty Five"
#
#  示例 3:
#
#  输入: 1234567
# 输出: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
#
#  示例 4:
#
#  输入: 1234567891
# 输出: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thou
# sand Eight Hundred Ninety One"
#  Related Topics 数学 字符串
#  👍 87 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numberToWords(self, num: int) -> str:
        if num==0:return "Zero"

        num = str(num)
        d = ['', 'Thousand', 'Million', 'Billion']
        pre = len(num)
        res = []
        for i, j in zip((range(len(num) - 3, -3, -3)), d):
            p = self.read(num[max(i, 0):pre])
            if p:
                res.append( p+' ' + j)
            pre = i
        return ' '.join(res[::-1]).strip()

    def read(self, n):
        mapn = {'1': 'One', '2': 'Two', '3': 'Three', '4': 'Four', '5': 'Five', '6': 'Six', '7': 'Seven', '8': 'Eight',
                '9': 'Nine'}
        mapTens = {'2': 'Twenty', '3': 'Thirty', '4': 'Forty', '5': 'Fifty', '6': 'Sixty', '7': 'Seventy',
                   '8': 'Eighty', '9': 'Ninety'}
        mapTen = {'10': 'Ten', '11': 'Eleven', '12': 'Twelve', '13': 'Thirteen', '14': 'Fourteen', '15': 'Fifteen',
                  '16': 'Sixteen',
                  '17': 'Seventeen', '18': 'Eighteen', '19': 'Nineteen'}
        res = []
        if len(n) > 2 and n[0]!='0':
            res.append(mapn[n[0]] + ' Hundred')
        if len(n) > 1 and n[-2]!='0':
            if n[-2] != '1' :
                res.append(mapTens[n[-2]])
            elif n[-2]=='1':
                res.append(mapTen[n[-2:]])
                return ' '.join(res)
        if n[-1]!='0':
            res.append(mapn[n[-1]])
        return ' '.join(res)
# leetcode submit region end(Prohibit modification and deletion)
