area = [input() for i in range(6)]
res = 1
def get(i,j):
    if 0<=i<6 and 0<=j<6 and area[i][j]=='#':
        return 1
    return 0

for i in range(6):
    for j in range(6):
        if area[i][j]=='#':
            other = get(i-1,j) + get(i,j-1)
            if other==2:
                if get(i-1,j-1):
                    res = res//6*25
                else:
                    res = res//36 *25
            elif other==1:
                res *= 5
            else:
                res *=6
            res %= 1000000009
print(res)



'''
#*****
******
******
******
******
*****#

#****
##****
******
******
******
******
'''

'''
##****
#*****
******
******
******
******
'''