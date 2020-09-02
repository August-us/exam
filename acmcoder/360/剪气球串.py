#encoding=utf-8
import numpy as np
'''
									
小明买了一些彩色的气球用绳子串在一条线上，想要装饰房间，每个气球都染上了一种颜色，每个气球的形状都是各不相同的。我们用1到9一共9个数字表示不同的颜色，如12345则表示一串5个颜色各不相同的气球串。但小明
希望得到不出现重复颜色的气球串，那么现在小明需要将这个气球串剪成多个较短的气球串，小明一共有多少种剪法？如原气球串12345的一种是剪法是剪成12和345两个气球串。
注意每种剪法需满足最后的子串中气球颜色各不相同（如果满足该条件，允许不剪，即保留原串）。两种剪法不同当且仅当存在一个位置，在一种剪法里剪开了，而在另一种中没剪开。详见样例分析。


输入
第一行输入一个正整数n（1≤n≤100000），表示气球的数量。
第二行输入n个整数a1，a2，a3...an，ai表示该气球串上第i个气球的颜色。对于任意i，有1≤ai≤9。

样例输入
3
1 2 3

输出
输出一行，第一行输出一个整数，表示满足要求的剪法，输出最终结果除以1000000007后的余数。
样例输出
4

这是一个动态规划问题，第i个字符，可以和前面与他不同的任意一个字符组合，假如可以和第j个字符组合，那么dp[i]+=dp[j] # 后面是j~i组合的情况
'''
n=input()
colors=np.random.randint(1,10,n)
# colors=[5,5,1,7,2,3,4,7,1,3]


# colors=[int(i) for i in raw_input().split(' ')]
dp=[1]*(n+1)
lastapperence=[-1]*10
lastDup=-1
for i,c in enumerate(colors):
    lastDup=max(lastapperence[c],lastDup)  # 比较该字符上一次出现的位置，和上一个重复的字符谁更大
    dp[i+1]=sum(dp[lastDup+1:i+1])
    lastapperence[c]=i
print(dp[-1]%1000000007)
print colors

dp = [1]
for i in xrange(1,n+1):
    d = 0;
    col =  [0]*10;
    for j in xrange(i):
        col[colors[i - j - 1]] += 1;
        if(col[colors[i - j - 1]] > 1): break;
        d += dp[i-1-j]
    dp.append(d)
print dp[-1] % 1000000007
