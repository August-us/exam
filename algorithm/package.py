import numpy as np
def solve(vlist,wlist,totalWeight,totalLength):
    resArr = np.zeros((totalLength+1,totalWeight+1),dtype=np.int32)
    for i in range(1,totalLength+1):
        for j in range(1,totalWeight+1):
            if wlist[i] <= j:
                resArr[i,j] = max(resArr[i-1,j-wlist[i]]+vlist[i],resArr[i-1,j])
            else:
                resArr[i,j] = resArr[i-1,j]
    return resArr[-1,-1]

def solve2(vlist,wlist,totalWeight,totalLength):
    resArr = np.zeros((totalWeight)+1,dtype=np.int32)
    for i in range(1,totalLength+1):
        for j in range(totalWeight,0,-1):
            if wlist[i] <= j:
                resArr[j] = max(resArr[j],resArr[j-wlist[i]]+vlist[i])
    return resArr[-1]

if __name__ == '__main__':
    v = [0,60,100,120]
    w = [0,10,20,30]
    weight = 50
    n = 3
    result = solve(v,w,weight,n)
    print(result)

    V = [0]
    W = [0]
    N, T = [int(i) for i in input().strip().split()]
    for i in range(N):
        v, i, c = [int(i) for i in input().strip().split()]
        W.extend([v for k in range(c)])
        V.extend([i for j in range(c)])
    print(solve(V, W, T, len(V) - 1))

'''
2 10
1 1 1
1 1 1
3 100
26 100 4
5 1 4
5 2 2
'''