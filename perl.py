L,N=[int(i) for i in input().strip().split(' ')]
A=[int(i)+L if int(i)<L/2 else int(i) for i in input().strip().split(' ')]
dis=0
mean=int(sum(A)/N)
l=[i for i in A if i<=mean ]
g=[i for i in A if i>mean ]
l.sort()
g.sort()
for i in range(0,len(l)):
    dis+=mean-l[len(l)-i-1]-i

for j in range(0,len(g)):
    dis+=g[j]-j-mean-1

print(dis)





'''
输入：L,N表示存放珍珠的位置总数和珍珠的数目，第二行N个珍珠的初始位置，移动最少的次数让珍珠移动到相邻的位置，位置是可以循环的
1000 4
1 4 998 995
1->0 4->1 998->999 995->998  共移动8次

10 5
1 3 5 7 9
移动6次
'''