n = int(input())

for i in range(n):
    already = set()
    numsCircle = int(input())
    for j in range(numsCircle):
        cur = tuple(sorted([int(i) for i in input().split(' ')]))
        if cur in already:
            print('YES')
            for j in range(j+1, numsCircle):
                cur = tuple(sorted([int(i) for i in input().split(' ')]))
            break
        already.add(cur)
    else:
        print('NO')

'''
2
2
1 2 3 4 5 6
2 3 4 5 6 1
3
1 2 3 4 5 6
8 5 4 1 2 3
2 3 4 5 6 7


'''