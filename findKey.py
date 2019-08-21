import sys
matrix=list(input().split('],'))
mat=[]
success=False
def DFS(k,a):
    if len(k)!=0:
        for i in mat[a]:
            if i and int(i) in k:
                k.remove(int(i))
                DFS(k,int(i))
    else:
        global success
        success=True
        return


for i in range (len(matrix)):
    mat.append(list(matrix[i].lstrip('[').rstrip(']').split(',')))
k=list(range(1,len(mat)))
DFS(k,0)
if success==True:
    print('true')
else:
    print ('false')



# [[1,3],[3,0,1],[2],[0]]
# [[1],[2],[3],[]]

