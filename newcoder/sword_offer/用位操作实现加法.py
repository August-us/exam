# 用位实现加法
def Add(num1,num2):
    sum=0
    c=0
    for i in range(32):
        a=num1>>i&1
        b=num2>>i&1
        p=(a^b^c)<<i
        sum  |=p
        c=(a&b)|(b&c)|(a&c)
    if sum >=  (1 << 31):
        sum^=(1<<32)-1
        sum=-sum-1
    return sum

def Add2(num1,num2):
    while num2:
        sum=num1^num2
        num2=(num1&num2)<<1
        num1=sum
    return num1
print(Add2(10,-15))

### 可以只使用两个变量就交换两个变量的值
# a=a+b  b=a-b a=a-b
# a=a^b  b=a^b a=a^b
