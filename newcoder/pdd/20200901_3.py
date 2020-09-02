
def solve(vlist,wlist,totalWeight):
    resArr = [0 for i in range(totalWeight+1)]
    for i in range(1,len(vlist)):
        for j in range(totalWeight,0,-1):
            if wlist[i] <= j:
                resArr[j] = max(resArr[j],resArr[j-wlist[i]]+vlist[i])
    return resArr[-1]


m,n = [int(i) for i in input().split(' ')]
vlist, wlist = [0], [0]
for i in range(n):
    w,v = [int(i) for i in input().split(' ')]
    vlist.append(v)
    wlist.append(w)
print(solve(vlist, wlist, m))


'''
4 4
-1 -1
1 -1
-1 1
6 6
'''

'''
4 4
1 1
1 -1
1 1
6 6

'''