import numpy as np

def gaussianElimination(A,b):
    A=np.matrix(A,dtype=np.float)
    b=np.array(b)
    assert len(A.shape)==2, "Coefficient matrix is not 2d. "
    assert A.shape[0]==b.shape[0], "Coefficient and b do not match."
    A=np.concatenate([A,b[:,None]],axis=1)

    for i in range(b.shape[0]):
        for k in range(i,A.shape[0]):
            if A[k,i]:
                A[i,:],A[k,:]=A[k,:]/A[k,i],A[i,:]
                break
        else:
            continue
        A[i+1:,i:]-=(A[i+1:,i]/A[i,i])*A[i,i:]  # 对角阵
    return A


def _solve(A):
    n=A.shape[1]-1
    flag=(A[:n]!=0).any(axis=1)
    if flag.all():# 可能有唯一解
        x=np.zeros(n)
        for i in range(n-1,-1,-1):
            assert (A[i,i]!=0.), "Equations without solution"
            x[i]=(A[i,n]-np.dot(A[i,:n],x))/A[i,i]
        return x

    else:
        k=flag.sum()
        x = np.zeros(n)
        for i in range(k-1,-1,-1):
            assert (A[i, i] != 0.), "Equations without solution"
            x[i] = (A[i, n] - np.dot(A[i,:n], x)) / A[i, i]
        k=np.eye(n-k)
        return (x,k)


def solve(A,b):
    '''
    :param A: 系数矩阵
    :param b: 常数向量
    :return: 返回线性方程组的解，如果有无数个解，返回特解和通解（元组），如果只有唯一解，返回之
    '''
    A=gaussianElimination(A,b)
    return _solve(A)

if __name__ == '__main__':
    A=[
        [1,0,0,0],
        [1,1,3,3],
        [1,2,2,4],
        [1,3,1,3],
    ]
    b = [4, 18,24,26]
    print(solve(A,b))
