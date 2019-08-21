string =list(input().strip().split(' '))
end={}
start={}
for s in string:
    if s[0] not in start:
        start[s[0]]=1
    else:
        start[s[0]]+=1
    if s[-1] not in end:
        end[s[-1]] = 1
    else:
        end[s[-1]] += 1
flag=True
for (k,v) in start.items():
    if k not in end or end[k]!=v:
        flag=False
if flag:
    print('true')
else:print('false')

"""
题目描述：给定一个字符串数组，判断所以字符串能否构成环
AB BA true
AB BC false
"""