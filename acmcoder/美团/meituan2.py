n=input()
radis=[int(i)**2 for i in raw_input().split(' ')]

res=0
for i in range(n-1,0,-2):
    res+=radis[i]-radis[i-1]
if n&1:
    res+=radis[0]
print "%.5f"%(3.141592653589793*res)





'''
5
1 2 3 4 5

47.12389
'''