from collections import defaultdict
'''
有些同学关系很差们不能坐在一起，输出所有的座位排列，输入n,k，n代表同学数目，k代表关系数目，接下来k行表示不能坐在一起的同学标号
3 2
1 2
2 1
超时
'''
n,k=[int(i) for i in input().split(' ')]
from time import time

relation=defaultdict(set)

for i in range(k):
    a,b=[int(i) for i in input().split(' ')]
    relation[a].add(b)
    relation[b].add(a)


def dfs(pre,last):
    if len(last)==0:
        # print(' '.join(map(str,pre)))
        return
    else:
        if pre:
            stu=pre[-1]
            for i in set(last)-relation[stu]:
                if i not in relation[stu]:
                    if len(last)==1:
                        # print(' '.join(map(str, pre+last)))
                        return
                    pre.append(i)
                    last.remove(i)
                    dfs(pre,last)
                    pre.pop()
                    last.append(i)
start=time()



for i in range(1,n+1):
    dfs([i],list(range(1,i))+list(range(i+1,n+1)))
print(time()-start)
start=time()

flag = [[True for i in range(n)]for i in range(n)]
#     flag[a-1][b-1] = False
#     flag[b-1][a-1] = False
def permuta(path,arr):
    if len(path) == n:
        # print(path)
        return
    for i in range(len(arr)):
        if  len(path)>0:
            if (flag[path[-1]-1][arr[i]-1]) == True:
                permuta(path+[arr[i]], arr[:i] + arr[i+1:])
        else:
            permuta([arr[i]], arr[:i] + arr[i+1:])

permuta([], [i for i in range(1,n+1)])
print(time()-start)

