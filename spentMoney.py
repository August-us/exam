# n=int(input())
# price=[0 for i in range(n)]
# for i in range(n):
#     price[i]=int(input())
# money=int(input())
#
# price.sort(reverse=True)

# speed test
n=99
price=[i for i in range(99,0,-1)]
money=10000

from time import time
start=time()
# 复杂度过于大,需要加备忘录
flag=[0 for i in range(money+1)]
def lost(m,k):
    if m<0:
        return float('inf')
    if flag[m]:
        return flag[m]
    if m%price[0]==0:
        flag[m]= k+int(m//price[0])
    else:
        flag[m] = min(map(lost,[m-price[i] for i in range(n)],[k+1 for i in range(n)]))
    return flag[m]
res=lost(money,0)
print(-1) if res==float('inf') else print(res)
print(time()-start)

# 如果能通过dp加一迭代，那么就可以翻滚迭代，time[i+k]=min{time[i]+time[k]}
start=time()
flag=[0 for i in range(money+1)]
def dp(money):
    k = 0
    p1 ={0}
    p2 = set()
    while p1:
        k+=1
        for v in p1:
            for good in price:
                a=v+good
                if flag[a]:
                    continue
                if a<=money:
                    p2.add(a)
                    flag[a]=k
                    if a==money:
                        return k
        p1,p2=p2,set()
    return -1
print(dp(money))
print(time()-start)


'''
题目描述：给定n个货物，接下来n行输入物品的价格，给定预算的money，用money去买货物，需要把钱花完，最少能买多少件物品，如果不能花完输出-1
4
1
2
3
4
10
输出：3

'''
