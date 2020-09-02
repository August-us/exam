n=input()
seqence=[int(i) for i in raw_input().split(' ')]
dp=[0]*(n+1)
dp[0]=1
for i in range(n):
    for j in range(1,i+2):
        if seqence[i]%j==0:
            dp[j]+=dp[j-1]

print (sum(dp)-1)%998244353


'''
2
3 1
2

'''