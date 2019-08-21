# 只能使用三种操作，移位，加一，减一，以此最快的实现从0到任意一个数的次数
a=str(bin(int(input())))[2:]
step = -1
i = 0
while i < len(a):
    if a[i] == '1':
        i += 1
        step += 2
        if i < len(a) and a[i] == '1':
            i += 1
            step += 3
            while i < len(a) and a[i] == '1':
                step += 1
                i += 1
    else:
        i += 1
        step += 1
print(step)
