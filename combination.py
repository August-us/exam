from time import time


N,S=[int(i) for i in input().strip().split(' ')]

def getCount(v,k,m):
    '''
    给出正整数集合v，从中依次选择k个数，使得和等于m，可以重复，一定有多少种取法。
    '''
    sum=[[0 for i in range(m+1)] for j in range(k+1)]
    sum[0][0]=1
    for i in range(k):
        for j in range(m):
            for l in range(len(v)):
                print(i+1,j+1,v[l],j+1>=v[l],sum[i][j+1-v[l]])
                sum[i+1][j+1]+= sum[i][j+1-v[l]] if j+1>=v[l] else 0
    print(sum)
    return sum[k][m]


def dfs(v,k,m):
    '''
        给出正整数集合v，从中依次选择k个数，使得和等于m，不能重复，一定有多少种取法。
    '''
    print(v,k,m)
    if v*(v+1)/2<m or m<0 or k<0 or v<1:
        return 0
    if k==0 and m==0:
        return 1
    try:
        if dp[v][k][m]!=0:
            return dp[v][k][m]!=0
    except:
        print(v,k,m)
        exit()
    s=dfs(v-1,k-1,m-v)+dfs(v-1,k,m)
    dp[v][k][m]=s
    return s



v=list(range(1,int(S-N*(N-2)/2)))
dp=[[[0 for i in range(S+1)] for j in range(N+1)]for k in range(int(S-N*(N-2)/2))]
# print(getCount(v,N,S))
print(dfs(int(S-N*(N-2)/2)-1,N,S))
for i in dp:
    print(i)