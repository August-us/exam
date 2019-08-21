import re
t=int(input().strip())

def revese(i):
    a=''
    for j in range(len(i)):
        if i[j]=='0':
            a+='1'
        else:
            a+='0'
    return a


for i in range(t):
    base=[]
    S = input()
    T = input()
    base.append(S)
    for j in range(1,len(S)):
        if S[j]!=S[j-1]:
            if S[j]=='0':
                base.append(revese(S[j:]))
            else:
                base.append(S[j:])

    pa='|'.join(base)
    print(pa,re.findall(pattern=pa,string=T))
    if T==''.join(re.findall(pattern=pa,string=T)):
        print('YES')
    else:
        print('NO')

'''
只包含0,1的字符串s，k是优秀的，则rev(s)是优秀的，s+k是优秀的，给定s是优秀的，判断t是否优秀
1
1100
110011
1
1000
100001111
'''