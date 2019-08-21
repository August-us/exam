n=int(input().strip())
max_=[[0,0,0]for i in range(n)]
min_=[[0,0,0]for i in range(n)]
score=[]
for i in range(n):
    score.append([int(i) for i in input().strip().split(' ')])
max_[0]=min_[0]=score[0]
for i in range(1,n):
    if score[i][0]==0:
        max_[i][0]=-min(min_[i-1][0:2])
        min_[i][0]=-max(max_[i-1][0:2])
    else:
        max_[i][0]=max(max_[i-1][0:2])+score[i][0]
        min_[i][0] = min(min_[i - 1][0:2]) + score[i][0]
    if score[i][1] == 0:
        max_[i][1] = -min(min_[i - 1])
        min_[i][1] = -max(max_[i - 1])
    else:
        max_[i][1]=max(max_[i-1])+score[i][1]
        min_[i][1] = min(min_[i - 1]) + score[i][1]
    if score[i][2] == 0:
        max_[i][2] = -min(min_[i - 1][1:])
        min_[i][2] = -max(max_[i - 1][1:])
    else:
        max_[i][2] = max(max_[i - 1][1:]) + score[i][2]
        min_[i][2] = min(min_[i - 1][1:]) + score[i][2]
print(max_,'\n',min_)
print(max(max_[-1]))

'''
每走一个格子，意味着获取当前格子的得分，但是值为0的格子表示当前分数变为原来的相反数。从第一行任意一个格子往下走，每次可以只能直接向下
或者往左右相邻的格子下面走，最多得分是多少分。
6
1 2 3
8 9 10
5 0 5
-9 -8 -10
0 1 2
5 4 6
'''