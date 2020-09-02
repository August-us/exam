'''
首先定义上升字符串，s[i]≥s[i−1],比如aaa，abc是，acb不是
给n个上升字符串，选择任意个拼起来，问能拼出来的最长上升字符串长度
'''
from typing import List


def longestAscString(strs:List[str])-> int:
    strs=sorted(strs,key=lambda x:(x[-1],-ord(x[0])))
    dp=[0]*26
    res=0
    last=0
    for string in strs:
        begin=ord(string[0])-ord('a')
        end=ord(string[-1])-ord('a')
        for i in range(last,end):
            dp[i+1]=dp[last]
        dp[end]=max(dp[end],dp[begin]+len(string))
        res=max(res,dp[end])
        last=end

    print(dp)
    return res


def hard():
    # 固定使用26*26的空间，O(n)的复杂度
    strs = [[0] * 26 for i in range(26)]
    n = int(input())  # 字符串的数目
    for i in range(n):
        s = input()
        begin = ord(s[0]) - ord('a')
        end = ord(s[-1]) - ord('a')
        if s[0] == s[-1]:
            strs[begin][begin] += len(s)
        else:
            strs[begin][end] = max(len(s), strs[begin][end])
    dp = [0] * 26
    for end in range(26):
        for begin in range(end):
            dp[end] = max(dp[begin] + strs[begin][end], dp[end])
        dp[end] += strs[end][end]
    print(dp[-1])

a=[
    "bcdefhijk",
    "bcd",
    "aaa",
    "eeeefghhh",
    "zzzz",
]
b=['abc',
'hpq',
'qrt',
'jklmnopqr',
'abcjklmnopqr',]

c=['abcd',
'deft',
'efghmnt',
'defghjkl',
'abcddefghjkl',]
print(longestAscString(c))
hard()


