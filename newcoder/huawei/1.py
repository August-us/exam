k = int(input())
ideal_apprence = [int(i) for i in input().split(' ')]
ideal_value = [int(i) for i in input().split(' ')]

n = int(input())
rea_apprence = [int(i) for i in input().split(' ')]
rea_value = [int(i) for i in input().split(' ')]


def get_next(lenk):
    k = 0
    next = [0 for i in range(lenk)]
    for i in range(1, lenk):
        while k>0 and (ideal_apprence[k]!= ideal_apprence[i] or ideal_value[k] != ideal_value[i]):
            k = next[k-1]
        if (ideal_apprence[k]== ideal_apprence[i] and ideal_value[k] == ideal_value[i]):
            k = k+1
        next[i] = k
    return next

def kmp(lenk):
    next = get_next(lenk)

    k = 0
    for i in range(n):
        while k>0 and (ideal_apprence[k]!= rea_apprence[i] or ideal_value[k] != rea_value[i]):
            k = next[k-1]
        if ideal_apprence[k] == rea_apprence[i] and ideal_value[k] == rea_value[i]:
            k = k + 1

        if k==lenk:
            return i-lenk +2
    return 0

print(kmp(k))

'''
3
1 2 3
3 2 1
6
1 2 3 3 2 1
3 2 1 1 2 3


3
1 2 3
3 2 1
6
1 2 1 2 3 3
5 4 3 2 1 1


10
1 1 1 1 1 1 1 1 1 1 
1 1 1 1 1 1 1 1 1 1 
6
1 2 3 3 2 1
3 2 1 1 2 3
'''

