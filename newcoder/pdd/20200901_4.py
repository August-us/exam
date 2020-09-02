n,m = [int(i) for i in input().split(' ')]

base = []
for i in range(m):
    base.append(int(input()))

res = 0
cur = [1 for i in range(len(base))]

mins = min(map(lambda x: cur[x] * base[x], range(len(base))))

while  mins <= n:
    for i,l in enumerate(base):
        if mins%l==0:
            cur[i]+=1
    mins = min(map(lambda x: cur[x] * base[x], range(len(base))))
    res +=1
print(res)







'''
10 3
2
3
5

10 2
2
3
'''

# n,m = [int(i) for i in input().split(' ')]
#
# base = []
# for i in range(m):
#     base.append(int(input()))
#
# res = 0
# for i in range(1, n+1):
#     for j in base:
#         if i%j==0:
#             res +=1
#             break
# print(res)


# n,m = [int(i) for i in input().split(' ')]
#
# res = [0 for i in range(n+1)]
# pre = []
# for i in range(m):
#     base = int(input())
#     if base==1:
#         print(n)
#         exit(0)
#     for j in pre:
#         if base%j==0:
#             continue
#     for j in range(base, n+1, base):
#         res[j]=1
#     pre.append(base)
# print(sum(res))