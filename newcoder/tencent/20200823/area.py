n = int(input())
for i in range(n):
    A, B,C,D = [int(i) for i in input().split(' ')]
    print('%.6f'%abs((A * (C * C * C - D * D * D) / 3 + (C * C - D * D) / 2 + B * (C- D))), end='')