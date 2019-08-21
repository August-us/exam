import sys
from collections import defaultdict

input_num=sys.stdin.readline().strip().split(' ')

n,k=int(input_num[0]),int(input_num[1])
height=[]
order=[]
h=sys.stdin.readline().strip().split(' ')
for j in range(n):
    height.append(int(h[j]))
    order.append(j+1)
    for i in range(j, 0, -1):
        if height[i] < height[i - 1]:
            height[i], height[i - 1] = height[i - 1], height[i]
            order[i], order[i - 1] = order[i - 1], order[i]
        else:
            break

# print (height)
# print (order)
result=[]
end=0
for i in range(k):
    end = i + 1
    if height[n-1]==height[0]:
        break
    height[n-1]-=1
    height[0]+=1
    result.append((order[n-1],order[0]))
    for i in range(n-1, 0, -1):
        if height[i] < height[i - 1]:
            height[i], height[i - 1] = height[i - 1], height[i]
            order[i], order[i - 1] = order[i - 1], order[i]
        else:
            break
    for i in range(n):
        if height[i] > height[i + 1]:
            height[i], height[i +1] = height[i + 1], height[i]
            order[i], order[i + 1] = order[i +1], order[i]
        else:
            break

print (height[n-1]-height[0],end)
for i in range(k):
    print(result[i][0],result[i][1])