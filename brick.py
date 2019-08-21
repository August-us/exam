import numpy as np
N=int(input().strip())
L=list(map(int,input().strip().split()))
W=list(map(int,input().strip().split()))
data=zip(L,W)
data=sorted(data)
weight=np.zeros(len(L)+1)
layer=np.zeros(len(L)+1)

for j in range(len(L)):
    l=1
    w=data[j][1]
    for i in range(j):
        if data[i][0]>=data[j][0]:
            break
        if weight[i+1]<=7*data[j][1]:
            if layer[i+1]+1>l:
                l=layer[i+1]+1
                w=weight[i+1]+data[j][1]
    layer[j+1]=l
    weight[j+1]=w
print('The max layer Base this brick: ',layer)
print('The max weight Base this brick: ',weight)





'''
题目描述：堆积木，下面的积木必须比上面大，且上面的重量不成超过下面重量的7倍，输入三行，1：样例数目，2：积木边长，3：积木重量
10
1 2 3 4 5 6 7 8 9 10
1 1 1 1 1 1 1 1 1 10
'''
