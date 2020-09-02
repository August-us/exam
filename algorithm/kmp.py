def get_next(T):
    n=len(T)
    next=[-1]*n
    i,j=0,-1
    while i<n-1:
        if j==-1 or T[i]==T[j]:
            i+=1
            j+=1
            next[i]=j
        else:
            j=next[j]
    return next

def get_next(T):
    n=len(T)
    next=[-1]
    i,j=0,-1
    while i<n-1:
        if j==-1 or T[i]==T[j]:
            i+=1
            j+=1
            next.append(j)
        else:
            j=next[j]
    return next
def kmp(S:str,T:str)->int:
    lens,lent=len(S),len(T)
    if lent==0:
        return 0
    next=get_next(T)
    i=j=0
    while i<lens and j <lent:
        if j==-1 or S[i]==T[j]:
            i+=1
            j+=1
        else:
            j=next[j]
    return i-j if j==lent else -1


def sunday(S: str, T: str) -> int:
    # Func: 计算偏移表
    def calShiftMat(st):
        shift={c:len(st)-i for i,c in enumerate(st)}
        return shift

    # 其他情况判断
    lent=len(T)
    lens=len(S)
    if lent>lens: return -1
    if lent==0: return 0

    # 偏移表预处理
    shift = calShiftMat(T)
    idx = 0
    while idx<= lens-lent:
        # 待匹配字符串
        for i in range(lent):
            if T[i]!=S[idx+i]:
                if idx+lent>=lens:
                    return -1
                idx+=shift.get(S[idx+lent],lent+1)
                break
        else:return idx

    return -1 if idx + len(T) >= len(S) else idx


if __name__ == '__main__':
    haystack = "hello"
    needle = "ll"
    # print(kmp(haystack,needle))
    print(sunday(haystack,needle))



