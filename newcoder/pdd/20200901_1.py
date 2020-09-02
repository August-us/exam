from math import atan2,pi, atan, ceil

n = int(input())


matrix = [[0 for i in range(n)] for j in range(n)]
half = (n-1) / 2


for i in range(n):
    for j in range(n):
        if i == half or j == half or abs(i - half)==abs(j - half):
            print(0,  end=' ')
        else:
            tmp = ceil(atan2(i - half, j - half)/pi * 4)
            tmp = abs(tmp) if tmp<0 else 8-tmp
            print(tmp, end=' ')
    print()


'''
5 
0 2 0 1 0
3 0 0 0 8
0 0 0 0 0
4 0 0 0 7
0 5 0 6 0

4
0 2 1 0
3 0 0 8
4 0 0 7
0 5 6 0
'''