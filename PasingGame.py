n,k=[int(i) for i in input().strip().split(' ')]
dp=[[0,0] for j in range(k+1)]
import numpy as np
dp=np.zeros((k+1,2))
dp[0][0]=1
for i in range(1,k+1):
    dp[i][0]=dp[i-1][1]
    dp[i][1]=max(0,dp[i-1][0]*(n-1)+dp[i-1][1]*(n-2))
print(dp[:,0])
print(dp[:,1])
print(dp[k,0])
'''
一朵花，从A开始，有n个人，每次需要传给别人，传递k次回到自己手上的情况次数
3 3:1->2->3->1  1->3->2->1
'''