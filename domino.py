L = list(input())
flag=0
i=0
while(i < len(L)):
    if L[i]=='R':
        j=i+1
        while(j<len(L)):
            if L[j]=='L':
                for k in range(j+1,len(L)):
                    if L[k]=='L':
                        j=k
                    if L[k]=='R':
                        break

                part=j-i+1
                for k in range(0,part/2):
                    L[i+k]='R'
                    L[j-k]='L'
                i=j
                flag=1
                break
            j+=1
        if flag==1:
            continue
        else:
            for j in range(i+1, len(L)):
                L[j]='R'
            flag=1
            break
    i+=1
if flag==0:
    i=0
    while (i < len(L)):
        if L[i]=='L':
            for j in range(i-1):
                L[j]='L'
    i+=1
if flag==1:
    i=0
    while (i < len(L)):
        if L[i]=='R':
            break
        if L[i]=='L':
            for j in range(i):
                L[j]='L'
        i+=1


string=''
for i in L:
    string+=i
print (string)
# .L.R...LR....L.




