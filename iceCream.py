n, m = [int(i) for i in input().strip().split(' ')]
pro=list(map(int,input().strip().split()))
price=list(map(int,input().strip().split()))
pp=list(zip(pro,price))
pp.sort()
print(pp)
money=[0]
for i in range(1,n):
    money.append(pp[i-1][1]+money[i-1])
    v=(pp[i][0]-pp[i-1][0])*money[i]
    if m-v<0:
        print(int(m/money[i])+pp[i-1][0])
        m=0
        break
    m=m-v
if m>0:
    print(int(m/(money[-1]+pp[-1][1]))+pp[-1][0])
'''
题目描述：输入第一行表示冰淇淋的种类和拥有的钱，第二行表示配料的数量，第三行表示每种配料的价格，使用这些配料和钱最多可以制作多少冰淇淋

3 10
2 5 3
2 1 3

'''