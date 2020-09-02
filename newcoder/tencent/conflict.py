m,n= [int(i) for i in input().split()]
m = m%10003

power = n-1
a,b = 1,1
basem, basem1 = m, m - 1

# 快速幂部分，求m和m-1的n-1次方，顺带对100003取模了
while power:
    if power&1:
        a = (a * basem) % 100003
        b = (b * basem1) %100003
    power >>= 1
    basem = (basem*basem) % 100003
    basem1 = (basem1*basem1) % 100003

print (m*(a-b)%100003)
