a=input().split(' ')
m,n=int(a[0]),int(a[1])
result=[]
i=0
flag=0
while(m%n!=0):
    m=m*10%n
    if m in result:
        print (result.index(m),i)
        flag=1
        break
    result.append(m)
    i+=1
if flag==0:
    print (i,0)