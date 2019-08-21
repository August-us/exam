def permute(string):
    def dfs(string,path,res):
        for i in range(len(string)):
            dfs(string[:i]+string[i+1:],path+[string[i]],res)
        if len(string)==0:
            res.append(path)
    res=[]
    dfs(string,[],res)
    return res

k=[int(i) for i in input().split(' ')]
s=sum(k)
p=[]
if s<9:
    s+=1
elif s<189:
    s=(s-9)/2+10
else:
    s=(s-189)/3+100
A=[0 for i in range(10)]
for i in range(1,int(s)+1):
    for c in str(i):
        A[int(c)]+=1
for i in range(10):
    for j in range(A[i]-k[i]):
        p.append(i)
p=permute(list(map(str,p)))
for i in p:
    if i[0]!=0:
        print(int(s),''.join(i))


'''
0 1 0 1 1 1 1 1 1 1

2 12 9 3 3 3 3 2 2 2
'''