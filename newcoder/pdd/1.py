k ,n = [int(i) for i in input().split(' ')]

N = [int(i) for i in input().split(' ')]
res = 0
for id,i in enumerate(N):
    if i==k and id!=n-1:
        print('paradox')
        break
    elif i<=k:
        k-=i
    else:
        k=i-k
        res +=1
else:
    print(k, res)
'''
10 2
6 3

10 4
6 3 3 3

6 3
4 2 6
'''