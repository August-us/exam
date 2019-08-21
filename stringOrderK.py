import sys
def string():
    input_num=sys.stdin.readline().strip().split(' ')

    n,m,k=int(input_num[0]),int(input_num[1]),int(input_num[2])
    string='a'*n+'z'*m
    for i in range(k):
        for j in range(m+n):
            if string[j]=='z':
                for l in range(j,-1,-1):
                    if string[l]=='a':
                        string=string[0:l]+'z'+string[l+1:j]+'a'+string[j+1:]
                        break
    print (string)
def iter():
    import itertools
    input_num = sys.stdin.readline().strip().split(' ')
    pp=set()

    n, m, k = int(input_num[0]), int(input_num[1]), int(input_num[2])
    for itera in list(itertools.permutations([1] * m + [0] * n, m + n)):
        binNum=''
        for num in itera:
            binNum+=str(num)
        pp.add(int(binNum))
    pp=list(pp)
    pp.sort()
    number=str(pp[k-1])
    result=''
    for i in range(len(number)):
        if number[i]=='0':
            result+='a'
        else:result+='z'
    result=(m+n-len(result))*'a'+result
    print (result)


if __name__=="__main__":
    iter()
    string()