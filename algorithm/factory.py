def dp():
    n = int(input())
    A = [int(i) for i in input().strip().split(' ')]
    res = [[A[0] + A[2], A[1]]]
    for i in range(1,n):
        A=[int(i) for i in input().strip().split(' ')]
        t=[]
        t.append(min(A[0]+res[i-1][0],A[0]+A[2]+res[i-1][1]))
        t.append(min(A[1]+res[i-1][1],A[1]+A[2]+res[i-1][0]))
        res.append(t)
    return min(res[-1])

if __name__=="__main__":

    print(dp())

'''
题目描述：n表示有多少棵树需要砍，每一行表示每棵树用锯子、斧子的时间，以及切换工具的时间，一开始工人手拿斧子，问最少需要多长时间能砍完这些树

3
20 40 20
10 4 25
90 100 5
'''