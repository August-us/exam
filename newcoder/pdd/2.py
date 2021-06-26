N,M = [int(i) for i in input().split(' ')]

board = []
trans = []

for i in range(N):
    board.append(input())
    if 'T' in board[-1]:
        start = (i, board[-1].index('T'))

visted = [[False for j in range(M)] for i in range(N)]
dis = 0
queue = [start]
res = []


def visit(i, j, queue):
    for h,w in [[-1, 0], [1, 0], [0,1],[0, -1]]:
        if not (i+h < 0 or i+h >= N or j+w<0 or j+w >= M or board[i+h][j+w] == '1' or visted[i+h][j+w]):
            queue.append((i+h, j+w))
            visted[i+h][j+w] = True
            if board[i+h][j+w] == 'X':
                res.append((i+h, j+w))

while queue:
    dis += 1
    newQueue = []
    for i,j in queue:
        visted[i][j] = True
        visit(i,j, newQueue)
    if res:
        print(dis)
        for i,j in sorted(res):
            print(i,j,end=' ')
        break
    queue = newQueue
else:
    print(0)





'''

5 6
X00100
00000X
01T000
0X1010
00000X

'''