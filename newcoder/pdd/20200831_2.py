from collections import defaultdict
n = int(input())
res1 = defaultdict(lambda :0)
res2 = defaultdict(lambda :0)

for i in range(n):
    cur = [int(i) for i in input().split(' ')]
    o = 0
    if cur[0] < cur[1]:
        o+=1
    if cur[2]<cur[3]:
        o +=1
    if cur[4]<cur[5]:
        o+=1

    a, b, c = tuple(sorted(cur[:2])), tuple(sorted(cur[2:4])), tuple(sorted(cur[4:]))
    if a[0]<b[0] :
        o+=1
    if a[0]<c[0]:
        o+=1
    if b[0]<c[0]:
        o+=1
    if o&1:

        res1[tuple(sorted([a,b,c]))]+=1
    else:
        res2[tuple(sorted([a,b,c]))]+=1

print(len(res1)+len(res2))
print(* sorted(list(res1.values())+list(res2.values()), reverse=True))


'''
2
1 2 3 4 5 6
1 2 6 5 3 4


3
1 2 3 4 5 6
1 2 6 5 3 4
1 2 3 4 6 5

10
2 5 1 3 4 6
5 4 3 2 1 6
1 4 6 2 3 5
1 5 6 3 4 2
6 4 2 1 5 3
3 6 4 5 2 1
1 6 3 4 2 5
5 1 4 2 6 3
6 2 3 1 5 4
5 3 6 1 4 2
'''