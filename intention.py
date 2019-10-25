th=int(input())
minLen=int(input())
maxLen=int(input())
L1=input().split(',')
L2=input().split(',')
index=[[] for i in range(len(L2))]

def minDistance(word1, word2):
    if not word1:
        return len(word2 or '') or 0

    if not word2:
        return len(word1 or '') or 0

    size1 = len(word1)
    size2 = len(word2)

    last = 0
    tmp = list(range(size2 + 1))
    value = None

    for i in range(size1):
        tmp[0] = i + 1
        last = i
        # print word1[i], last, tmp
        for j in range(size2):
            if word1[i] == word2[j]:
                value = last
            else:
                value = 1 + min(last, tmp[j], tmp[j + 1])
                # print(last, tmp[j], tmp[j + 1], value)
            last = tmp[j+1]
            tmp[j+1] = value
        # print tmp
    return value

for i in range(len(L2)):
    try:
        a=L1.index(L2[i])
        while a>0:
            index[i].append(a)
            a=L1.index(L2[i],a+1)
    except:
        continue
print(index)
a=0
import time
start=time.time()
for i in range(minLen+1,maxLen):
    for j in range(len(L1)-i):
        for k in range(len(L2)-i):
            print(L1[j:j+i],L2[k:k+i])
            if minDistance(L1[j:j+i],L2[k:k+i])<=th:
                a+=1
print(a,time.time()-start)




'''
1
3
5
weather,joke,music,stock,joke,news,taxi,temperature,pm2.5
joke,music,news,stock,joke,news,taxi

'''