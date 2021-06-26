n,m = [int(i) for i in input().split(' ')]

pixel = []
for i in range(n):
    pixel.append( [int(i) for i in input().split(' ')])


def mean(i, j):
    k=5
    s = pixel[i][j]
    if i==0:
        k -=1
    else:
        s += pixel[i-1][j]
    if i == n - 1:
        k -=1
    else:
        s += pixel[i + 1][j]
    if j==0:
        k-=1
    else:
        s += pixel[i][j-1]
    if j==m-1:
        k-=1
    else:
        s += pixel[i][j + 1]
    return round(s/k)




for i in range(n):
    for j in range(m):
        pixel[i][j] = mean(i,j)
    print(' '.join(map(str, pixel[i])))
'''
2 2
10 20
30 40
'''