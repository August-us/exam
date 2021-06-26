from itertools import combinations


P = int(input())
n = int(input())

desc = []
for i in range(n):
    string, a,b = input().split(' ')
    desc.append([string, int(a), int(b)])

desc.sort(key = lambda x:x[1])


def backward(index, cur):
    for i in range(26):
        cur[index[0]] = chr(ord('a')+i)
        if len(index) > 1:
            for i  in backward(index[1:], cur):
                yield i
        else:
            yield cur

def validation(word, test):
    p = q = 0
    for i in range(len(word)):
        if test[0][i] in word:
            if test[0][i] == word[i]:
                p += 1
            else:
                q += 1
    if p==test[1] and q == test[2]:
        return True
    else:
        return False



for index in combinations(range(P), P-desc[-1][1]):
    cur = ['a' for i in range(P)]
    for i in range(P):
        if i not in index:
            cur[i] = desc[-1][0][i]
    for r in backward(index, cur):
        for test in desc[:-1:]:
            if not validation(r, test):
                break
        else:
            print(''.join(r))
            exit(0)