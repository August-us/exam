'''

'''

T=int(input())
for i in range(T):
    n,m=[int(i) for i in input().split(' ')]
    grid=[[0]*(n+1) for i in range(m+1)]
    x1,y1,x2,y2=[int(i) for i in input().split(' ')]
    k=int(input())
    for i in range(k):
        x,y,op=input().split(' ')
        x, y = int(x), int(y)
        if grid[x][y]:
            if grid[x][y]=='l':
                for _ in range(x):
                    if grid[_][y] == 'l':
                        grid[_][y]=0
            elif grid[x][y] == 'r':
                for _ in range(x+1,n+1):
                    if grid[_][y] == 'r':
                        grid[_][y] = 0
            elif grid[x][y] == 'u':
                for _ in range(y):
                    if grid[x][_] == 'u':
                        grid[x][_] = 0
            elif grid[x][y] == 'd':
                for _ in range(y+1,m+1):
                    if grid[x][_] == 'd':
                        grid[x][_] = 0

        if op=='B':
            grid[x][y]='B'
        else:
            grid[x][y] =op
            if grid[x][y]=='l':
                for _ in range(x):
                    if grid[_][y] == 0:
                        grid[_][y]='l'
                    else:
                        break
            elif grid[x][y] == 'r':
                for _ in range(x+1,n+1):
                    if grid[_][y] == 0:
                        grid[_][y] = 'r'
                    else:
                        break

print(grid)


'''
2
3 3
1 1 3 3
2
2 1 r
2 3 B
3 2
1 2 3 1
2
2 1 B
2 2 B

'''