def LastRemaining_Solution(n, m):
    # write code here
    # 用列表来模拟环，新建列表range(n)，是n个小朋友的编号
    if not n or not m:
        return -1
    lis = list(range(n))
    i = 0
    while len(lis) > 1:
        i = (m - 1 + i) % len(lis)  # 递推公式
        lis.pop(i)
    return lis[0]
