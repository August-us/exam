'''
第一行输入怪物的数量，和勇士的防御，第二行输入怪物的攻击，最后一行输入怪物的伤害，如果勇士的防御小于怪物的攻击，那么勇士就要承受对应的伤害，没对抗一个怪物，勇士的防御增加1，输出勇士最少承受的伤害
3 50
100 50 51
1000 1000 1000

5 50
50 50 51 52 53
1 1 2 3 4
'''


n,defense=[int(i) for i in input().split(' ')]


ma=[int(i) for i in input().split(' ')]
md=[int(i) for i in input().split(' ')]
monster=sorted(zip(ma,md))
res=0
for ma,md in monster:
    if ma>defense:
        res+=md
    defense+=1

print(res)

'''
# 每次没有怪物可打，则打破防最高的
n, D = map(int, input().split())
pf = map(int, input().split())
sh = map(int, input().split())
arr = list(zip(pf,sh))

#print(sorted(arr))
arr = sorted(arr)
count = 0
while(len(arr)):
    if arr[0][0] < D:
        D += 1
        #count += arr[0][1]
        del arr[0]
    else:
        D+=1
        count += arr[-1][1]
        del arr[-1]
print(count)
'''



