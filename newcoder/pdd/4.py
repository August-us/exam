H ,W = [int(i) for i in input().split(' ')]
mod = int(1e9+7)
if H < W:
    H,W = W, H
if W == 1:
    print(1)
if W == 2:
    f0, f1 = 1, 1
    for i in range(H-1):
        f0, f1 = f1, f0+f1
    print(f1 % mod)
else:
    print(0)


'''
4 2

3 3

5 2
'''