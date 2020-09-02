from typing import List


def lcs(a, b):
    lena = len(a)
    lenb = len(b)
    c = [[0 for i in range(lenb + 1)] for j in range(lena + 1)]
    flag = [[0 for i in range(lenb + 1)] for j in range(lena + 1)]
    for i in range(lena):
        for j in range(lenb):
            if a[i] == b[j]:
                c[i + 1][j + 1] = c[i][j] + 1
                flag[i + 1][j + 1] = 'ok'
            elif c[i + 1][j] > c[i][j + 1]:
                c[i + 1][j + 1] = c[i + 1][j]
                flag[i + 1][j + 1] = 'left'
            else:
                c[i + 1][j + 1] = c[i][j + 1]
                flag[i + 1][j + 1] = 'up'
    return c, flag

def lcString(a, b):
    lena = len(a)
    lenb = len(b)
    Maxstr=''
    c = [[0 for i in range(lenb + 1)] for j in range(lena + 1)]
    for i in range(lena):
        for j in range(lenb):
            if a[i] == b[j] :
                c[i + 1][j + 1] = c[i][j] + 1
                cur=c[i+1][j+1]
                print(a[i],i,j)
                if cur>len(Maxstr) and i+j-cur==lena-2:
                    Maxstr=a[i-cur+1:i+1]
            else:
                c[i + 1][j + 1] = 0
    print(Maxstr)
    return c

def printLcs(flag, a, i, j):
    if i == 0 or j == 0:
        return
    if flag[i][j] == 'ok':
        printLcs(flag, a, i - 1, j - 1)
        print(a[i - 1], end='')
    elif flag[i][j] == 'left':
        printLcs(flag, a, i, j - 1)
    else:
        printLcs(flag, a, i - 1, j)


a = [1,2,3,4,5,1,3,5,7,8,34]
b = [2,2,3,9,7,4]
c, flag = lcs(a, b)
c=lcs(a,b)
for i in c:
    print(i)
print('')
for j in flag:
    print(j)
print('')
printLcs(flag, a, len(a), len(b))
print('')

# 最长上升子序列的长度,事实上不需要存储索引，因为没什么用处，可以考虑直接存这个上升的序列。
def lengthOfLIS_withindex( nums: List[int]) -> int:
    longest=[]
    for i,num in enumerate(nums):
        if not longest or num>nums[longest[-1]]:
            longest.append(i)
        else:
            start,end=0,len(longest)-1
            while start<=end:
                mid=(start+end)>>1
                if nums[longest[mid]]==num:
                    break
                elif nums[longest[mid]]>num:
                    end=mid-1
                else:
                    start= mid + 1
            else:
                longest[start]=i
    return len(longest)

def lengthOfLIS(nums: List[int]) -> int:
    # 最终的d不能代表最长上升子序列
    d = []
    for n in nums:
        if not d or n > d[-1]:
            d.append(n)
        else:
            l, r = 0, len(d) - 1
            loc = r
            while l <= r:
                mid = (l + r) // 2
                if d[mid] >= n:
                    loc = mid
                    r = mid - 1
                else:
                    l = mid + 1
            d[loc] = n
    return len(d)

print(lengthOfLIS([3,5,6,2,5,4,19,5,6,7,12]))
