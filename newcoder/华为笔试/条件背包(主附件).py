# 题目描述
# 公司发给N元的年终奖。王强决定把年终奖用于购物，他把想买的物品分为两类：主件与附件，附件是从属于某个主件的，下表就是一些主件与附件的例子：
# 如果要买归类为附件的物品，必须先买该附件所属的主件。每个主件可以有 0 个、 1 个或 2 个附件。附件不再有从属于自己的附件。每件物品规定了一个重要度，分为 5 等：用整数 1 ~ 5 表示，第 5 等最重要。物品价格（都是 10 元的整数倍）。他希望在不超过 N 元（可以等于 N 元）的前提下，使每件物品的价格与重要度的乘积的总和最大。
#     设第 j 件物品的价格为 v[j] ，重要度为 w[j] ，共选中了 k 件物品，编号依次为 j 1 ， j 2 ，……， j k ，则所求的总和为：
# v[j 1 ]*w[j 1 ]+v[j 2 ]*w[j 2 ]+ … +v[j k ]*w[j k ] 。（其中 * 为乘号）
#     请你帮助王强设计一个满足要求的购物单。
#  输入描述:
# 输入的第 1 行，为两个正整数，用一个空格隔开：N m
#
# （其中 N （ <32000 ）表示总钱数， m （ <60 ）为希望购买物品的个数。）
# 从第 2 行到第 m+1 行，第 j 行给出了编号为 j-1 的物品的基本数据，每行有 3 个非负整数 v p q
# （其中 v 表示该物品的价格（ v<10000 ）， p 表示该物品的重要度（ 1 ~ 5 ）， q 表示该物品是主件还是附件。如果 q=0 ，表示该物品为主件，如果 q>0 ，表示该物品为附件， q 是所属主件的编号）
#
# 输出描述:
#  输出文件只有一个正整数，为不超过总钱数的物品的价格与重要度乘积的总和的最大值（ <200000 ）。

while True:
    try:
        weight,n=[int(i) for i in input().split(' ')]
        dp=[[0]*(weight//10+1) for i in range(n)]
        weights=[]
        for i in range(n):
            w=[int(i) for i in input().split(' ')]
            w[0]//=10
            w[1]*=w[0]
            weights.append(w)
        for i in range(n):
            w=weights[i]
            index=i
            if w[2]!=0:
                for j in range(i-1,w[2]-1,-1):
                    if weights[j][2]!=0 and weights[j][2]!=w[2]:
                        weights[j][2]+=1
                    weights[j+1]=weights[j]
                    index=j
                weights[index]=w

        for i in range(n):
            for j in range(1,weight//10+1):
                if weights[i][2]==0:
                    if j >= weights[i][0]:
                        dp[i][j]=max(dp[i-1][j],dp[i-1][j-weights[i][0]]+weights[i][1])
                    else:
                        dp[i][j]=dp[i-1][j]
                else:
                    if j > weights[i][0]+weights[weights[i][2]-1][0]:
                        dp[i][j] = max(dp[i - 1][j], dp[weights[i][2]-1][j - weights[i][0]-1] + weights[i][1])
                    else:
                        dp[i][j]=dp[i-1][j]
        print(dp[-1][-1]*10)
        # for i in range(weight//100+1):
        #     print(dp[i])
    except Exception:
        break

'''
4500 12
100 3 0
400 5 0
300 5 0
1400 2 0
500 2 0
800 2 4
1400 5 4
300 5 0
1400 3 8
500 2 0
1800 4 0
440 5 10

16700
'''