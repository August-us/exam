def permute(string):
    def dfs(string,path,res):
        for i in range(len(string)):
            dfs(string[:i]+string[i+1:],path+[string[i]],res)
        if len(string)==0:
            res.append(path)
    res=[]
    dfs(string,[],res)
    return res

print(permute('12345'))