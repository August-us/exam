from collections import Counter

'''
给定一个字符串 s1，我们可以把它递归地分割成两个非空子字符串，从而将其表示为二叉树。

下图是字符串 s1 = "great" 的一种可能的表示形式。

    great
   /    \
  gr    eat
 / \    /  \
g   r  e   at
           / \
          a   t
在扰乱这个字符串的过程中，我们可以挑选任何一个非叶节点，然后交换它的两个子节点。

例如，如果我们挑选非叶节点 "gr" ，交换它的两个子节点，将会产生扰乱字符串 "rgeat" 。

    rgeat
   /    \
  rg    eat
 / \    /  \
r   g  e   at
           / \
          a   t
我们将 "rgeat” 称作 "great" 的一个扰乱字符串。

同样地，如果我们继续交换节点 "eat" 和 "at" 的子节点，将会产生另一个新的扰乱字符串 "rgtae" 。

    rgtae
   /    \
  rg    tae
 / \    /  \
r   g  ta  e
       / \
      t   a
我们将 "rgtae” 称作 "great" 的一个扰乱字符串。

给出两个长度相等的字符串 s1 和 s2，判断 s2 是否是 s1 的扰乱字符串。

示例 1:

输入: s1 = "great", s2 = "rgeat"
输出: true
示例 2:

输入: s1 = "abcde", s2 = "caebd"
输出: false

题目分析：这个题是一个3维dp,dp[strat1][start2][length]=dp[strat1][start2][w] && dp[strat1+w][start2+w][length-w]  正向匹配
                                                    || dp[strat1][start2+length-w][w] && dp[strat1+w][start2][length-w] 

但是三维的矩阵中，冗余太严重了，这个时候反而递归具有稀疏性，能得到更快的速度
'''


class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2): return False
        self.dp = [[[None] * len(s1) for i in s1] for j in s1]
        return self.orderS(s1, s2, 0, 0, len(s1))

    def orderS(self, s1: str, s2: str, start1, start2, length) -> bool:
        if self.dp[start1][start2][length - 1] is None:
            if length <= 3:
                self.dp[start1][start2][length - 1] = Counter(s1[start1:start1 + length]) == Counter(
                    s2[start2:start2 + length])
            else:
                origin = Counter()
                new = Counter()
                for i in range(length - 1):
                    origin.update(s1[start1 + i])
                    new.update(s2[start2 + i])
                    if origin == new:
                        self.dp[start1][start2][length - 1] = self.orderS(s1, s2, start1, start2,
                                                                          i + 1) and self.orderS(s1, s2, start1 + i + 1,
                                                                                                 start2 + i + 1,
                                                                                                 length - i - 1)
                        break
                if not self.dp[start1][start2][length - 1]:
                    origin = Counter()
                    new = Counter()
                    for i in range(length - 1):
                        origin.update(s1[start1 + i])
                        new.update(s2[start2 + length - i - 1])
                        if origin == new:
                            self.dp[start1][start2][length - 1] = self.orderS(s1, s2, start1, start2 + length - i - 1,
                                                                              i + 1) and self.orderS(s1, s2,
                                                                                                     start1 + i + 1,
                                                                                                     start2,
                                                                                                     length - i - 1)
                            break
                    else:
                        self.dp[start1][start2][length - 1] = False
        return self.dp[start1][start2][length - 1]


class Solution1:
    def isScramble(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2): return False
        self.dp = {}
        res = self.orderS(s1, s2, 0, 0, len(s1))
        return res

    def orderS(self, s1: str, s2: str, start1, start2, length) -> bool:
        if (start1, start2, length - 1) not in self.dp:
            if length <= 3:
                self.dp[(start1, start2, length - 1)] = Counter(s1[start1:start1 + length]) == Counter(
                    s2[start2:start2 + length])
            else:
                origin = Counter()
                new = Counter()
                for i in range(length - 1):
                    origin.update(s1[start1 + i])
                    new.update(s2[start2 + i])
                    if origin == new:
                        self.dp[(start1, start2, length - 1)] = self.orderS(s1, s2, start1, start2,
                                                                            i + 1) and self.orderS(s1, s2,
                                                                                                   start1 + i + 1,
                                                                                                   start2 + i + 1,
                                                                                                   length - i - 1)
                        break
                if not self.dp.get((start1, start2, length - 1)):
                    origin = Counter()
                    new = Counter()
                    for i in range(length - 1):
                        origin.update(s1[start1 + i])
                        new.update(s2[start2 + length - i - 1])
                        if origin == new:
                            self.dp[(start1, start2, length - 1)] = self.orderS(s1, s2, start1, start2 + length - i - 1,
                                                                                i + 1) and self.orderS(s1, s2,
                                                                                                       start1 + i + 1,
                                                                                                       start2,
                                                                                                       length - i - 1)
                            break
                    else:
                        self.dp[(start1, start2, length - 1)] = False
        return self.dp[(start1, start2, length - 1)]


class Solution_force_re:
    def isScramble(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        if s1 == s2:
            return True
        if sorted(s1) != sorted(s2):
            return False

        for i in range(1, len(s1)):
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]) or \
                    (self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i])):
                return True
        return False


class Solution_force_dp:
    def isScramble(self, s1, s2):  # 判断s2是不是s1的扰乱字符串
        lens1 = len(s1)
        lens2 = len(s2)
        if lens1 != lens2:
            return False
        # 初始化dp3维数组dp[i][j][k]
        # i为0~lens1-1共lens1个， j为0~lens1-1共lens1个， k为1~lens1+1共lens1个
        dp = [[[False] * (lens1 + 1) for _ in range(lens1)] for _ in range(lens1)]

        # 初始化单个字符的情况
        for i in range(lens1):
            for j in range(lens1):
                dp[i][j][1] = s1[i] == s2[j]

        # 前面排除了s1和s2为单个字符的情况，那么我们就要划分区间了，k从2到lens1，也就是划分为s1[:k]和s1[k:]

        # 枚举区间长度2～lens1
        for k in range(2, lens1 + 1):
            # 枚举S中的起点位置
            for i in range(lens1 - k + 1):  # 也就是在s1中枚举i的位置，因为后面会出现i+w的情况，而w最大就是k，
                # 就会有i+k的情况，所以i的取值范围就是0~lens1-k

                # 枚举T中的起点位置
                for j in range(lens1 - k + 1):
                    # 枚举划分位置，s1[:k]中从
                    for w in range(1, k):
                        # 第一种情况：S1->T1,S2->T2
                        if dp[i][j][w] and dp[i + w][j + w][k - w]:
                            dp[i][j][k] = True
                            # print("i,j,k", i, j, k)
                            break

                        # 第二种情况：S1->T2,S2->T1
                        # S1起点i，T2起点j + 前面那段长度k-w，S2起点i+前面长度k
                        if dp[i][j + k - w][w] and dp[i + w][j][k - w]:
                            dp[i][j][k] = True
                            # print("i,j,k", i, j, k)
                            break
        return dp[0][0][lens1]


s1 = "hobobyrqd"
s2 = "hbyorqdbo"
# s1 = "great", s2 = "taerg"
print(Solution_force_dp().isScramble(s1, s2))
print(Solution1().isScramble(s1, s2))


