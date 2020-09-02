a=raw_input()
trans={str(i+1):j for i,j in enumerate(raw_input().split(' '))}
trans['-']='-'
trans['+']='+'
res=['']*len(a)
for i,a in enumerate(a):
    res[i]=trans[a]
print ''.join(res)
'''
1234567
9 8 7 6 5 4 3 2 1

73598793378342493
1 3 6 1 6 8 9 1 3
'''