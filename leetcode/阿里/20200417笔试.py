from algorithm.permute import permute

def permute_list(string):
    def dfs(string,begin):
        if len(string)==begin+1:
            for i in range(begin, len(string)):
                for j in range(i):
                    for k in range(j + 1, i):
                        if string[k] * 2 == string[j] + string[i]:
                            return
            print(' '.join(map(str,string)))
            return
        for i in range(begin,len(string)):
            for j in range(i-1):
                for k in range(j+1,i):
                    if string[k]*2==string[j]+string[i]:
                        break
            else:
                string[i], string[begin] = string[begin], string[i]
                dfs(string,begin+1)
                string[i], string[begin] = string[begin], string[i]
    dfs(string,0)
n=int(input())
permute_list(list(range(1,n+1)))



n,q=[int(i) for i in input().split(' ')]
A=[int(i) for i in input().split(' ')]
res=[]
for i in range(q):
    s,e=[int(i) for i in input().split(' ')]
    p=abs(s-e)/n
    if p>0.5:
        p=1-p
    res.append(p)