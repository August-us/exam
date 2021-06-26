n = int(input())
coe = [int(i) for i in input().split(' ')]

def get_fx(x, coe=coe):
    result = 0
    n = len(coe)-1
    for i in range(len(coe)):
        result+= coe[i]*x**(n-i)
    return result

flag = False
pre = get_fx(-100)
for i in range(1, 20000):
    x = -100 + i/100
    cur = get_fx(x)
    if cur*pre<0:
        if cur<=pre:
            print('%.2f'%x)
        else:
            print('%.2f'%(x-0.01))
        flag = True
    elif cur==0:
        print('%.2f' % x)
        flag = True
    pre = cur
if not flag:
    print('NO')

'''
2
1 2 1

3
1 4 2 5
'''