import time
A=str(2**1000000)
B=A
start=time.time()
i=len(A)-1
j=len(B)-1
k=len(A)+len(B)-1
res=['0' for i in range(k+1)]
i_,j_=0,0
while i>-1 and j >-1:
    if int(A[i])>int(B[j]):
        res[k]=A[i]
        i-=1
    elif int(A[i])<int(B[j]):
        res[k]=B[j]
        j-=1
    else:
        i_,j_=i,j
        while i_>-1 and j_>-1:
            if int(A[i_]) > int(B[j_]):
                res[k] = A[i]
                i -= 1
                break
            elif int(A[i_]) < int(B[j_]):
                res[k] = B[j]
                j -= 1
                break
            else:
                i_-=1
                j_-=1
        if i_==-1 or j_==-1:
            res[k] = A[i]
            i -= 1
    k-=1


if i>-1:
    print(A[0:i+1]+''.join(map(str,res[i+1:])))
else:
    print(B[0:j+1]+''.join(map(str,res[j+1:])))
print(time.time()-start)
'''
1213
1312
'''