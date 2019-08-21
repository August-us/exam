import time
a=None
def calTriangle():
    global a
    a=[[1 for i in range(int(j/2))] for j in range(2,130)]
    for i in range(1,127,2):
        for j in range(1,len(a[i])):
            a[i][j] = a[i - 1][j - 1] + a[i-1][j]
            a[i+1][j] = a[i][j - 1] + a[i][j ]
        a[i+1][-1]=2*a[i][-1]
        a[i]+=a[i][::-1]
        a[i+1]+=a[i+1][-2::-1]
start=time.time()
calTriangle()
print(time.time()-start)
# while True:
#     n=int(input())
#     start = time.time()
#     if n:
#         for i in range(n):
#             print(' '.join(map(str, a[i])))
#         print()
#         print(time.time() - start)
#         break
#     else:
#         print(time.time()-start)
#         break
def N(lst):
    temp=[1]+lst
    for i in range(1,len(temp)-1):
        temp[i]=temp[i]+temp[i+1]
    return temp
start=time.time()

Y=[[0]]*129
Y[0]=[1]
for n in range(1,129):
    Y[n]=N(Y[n-1])
print(time.time()-start)

'''
def N(lst):
    temp=[1]+lst
    for i in range(1,len(temp)-1):
        temp[i]=temp[i]+temp[i+1]
    return temp
Y=[[0]]*129
Y[0]=[1]
for n in range(1,129):
    Y[n]=N(Y[n-1])
while True:
    m = int(input())
    if m==0:
        break
    for i in range(m):
        print(' '.join(map(str,Y[i])))
    print()
'''