n = int(input().strip())
A = list(input().strip().split(' '))
a=A[::2]
b=A[1::2]
a.sort()
b.sort()
while a:
    if a[0]<b[0]:
        a.pop(0)
        print(a[0],end=' ')
    else:
        print(b[0],end=' ')
        b[0]=a[0]
        a.pop(0)
        b.sort()
print(' '.join(b))



'''
字符串中奇数下标和偶数下标的元素可以互换位置，然后尽可能的对字符数组进行排序

10
53941 38641 31525 75864 29026 12199 93522 58200 64784 80987
'''
