M,N=list(map(int,input().strip().split()))
process=list(map(int,input().strip().split()))
flag=[True]*M
dep={}

for i in range(N):
    A,B = list(map(int, input().strip().split()))
    if B not in dep:
        dep[B]=[A]
    else:
        dep[B].append(A)
result=[]

for i in range(M):
    print(dep)
    min=float('inf')
    minProcess=-1
    for i in range(M):
        if (i+1 not in dep or len(dep[i+1])==0) and process[i]<min and flag[i]:
            min=process[i]
            minProcess=i+1
    result.append(minProcess)
    flag[minProcess-1]=False
    print(process)
    for k,v in dep.items():
        if minProcess in v:
            v.remove(minProcess)

print(' '.join(map(str,result)))


'''
题目描述：在进程依赖的情况下实现最短进程优先算法，输入样例：1.M,N  M表示进程数，N表示依赖数  2.进程的执行时间  3-2+N 表示后面的进程依赖于前面的进程
5 6
1 2 1 1 1
1 2
1 3
1 4
2 5
3 5
4 5
'''