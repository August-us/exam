a=[int(i) for i in input().split(',')]

res={}
r=0
for i in a:
    if i not in res:
        res[i]=1
    else:
        res[i]+=1
for k,v in res.items():
    if v%(k+1)==0:
        r+=v
    else:
        a=v//(k+1)+1
        r+=a*(k+1)
print(r)
