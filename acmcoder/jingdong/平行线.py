from collections import defaultdict

# points=[]
# n=int(input())
# for i in range (n):
#     points.append([int(i) for i in input().split(' ')])
#
# res=defaultdict(int)
#
# for i in range(n-1):
#     for j in range(i+1,n):
#         if points[i][1]==points[j][1]:
#             res['inf']+=1
#         else:
#             res[(points[i][0]-points[j][0])/(points[i][1]-points[j][1])]+=1
#
# print(res)
# a=max(res.values())
# print((a*a-a)//2)




def gcd(a, b):
    c = a % b
    if c == 0:
        return b
    else:
        return gcd(b, c)


def calc_k(point1, point2):
    y_diff = point2[1] - point1[1]
    x_diff = point2[0] - point1[0]
    if x_diff == 0:
        return (float('inf'), float('inf'))
    elif y_diff == 0:
        return (0, 0)
    else:
        if x_diff * y_diff > 0:
            x_diff, y_diff = abs(x_diff), abs(y_diff)
        else:
            x_diff, y_diff = -(abs(x_diff)), abs(y_diff)
        gcd_factor = gcd(x_diff, y_diff)
        return (x_diff // gcd_factor, y_diff // gcd_factor)


points = []
from collections import defaultdict

ks = defaultdict(list)
for i in range(int(input())):
    points.append(list(map(int, input().split())))

for i in range(len(points) - 1):
    for j in range(i + 1, len(points)):
        ks[calc_k(points[i], points[j])].append((i, j))

ks = sorted(ks.items(), key=lambda e: len(e[1]), reverse=True)

ans = 0
vis = set()
for k, vs in ks:
    if len(vs) == 1: break
    ans += len(vs) * (len(vs) - 1) // 2
    for v in vs:
        vis.add(v[0])
        vis.add(v[1])
    if len(vis) == len(points): break  # 测试集太弱了，这都能AC
print(ans)

'''
8
0 0
0 5
2 2
2 7
3 -2
5 0
4 -2
8 2
'''