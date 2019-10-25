def fun(strList):
    set1=set()
    for a in strList:
        ja=a[::2]
        oa=a[1::2]
        set1.add(''.join(sorted(ja))+''.join(sorted(ja)))
    return len(set1)

def fun1(strList):
    set1=set([''.join(sorted(a[::2])) + ''.join(sorted(a[1::2])) for a in strList ])
    return len(set1)


a='abcd'
b='adcb'
print(fun1([a,b]))
"""
如果两个字符串通过奇数位置上的字符相互交换，或者偶数位置上的字符串相互交换可以变为一致的，则认为字符串相等，
给定一个列表，判断有多少字符串是相等的

"""