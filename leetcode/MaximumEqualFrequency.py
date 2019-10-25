import collections
def maxEqualFreq(nums):
    count,freq,maxF,res=collections.Counter(),collections.defaultdict(int),0,0
    for i,num in enumerate(nums,1):
        freq[count[num]]-=1
        count[num]+=1
        freq[count[num]]+=1
        maxF=max(maxF,count[num])
        if maxF==1 and i<len(nums): # Case 1: All numbers in set have occured exactly once
            res=i+1
        elif i==(maxF-1)*(freq[maxF-1]+1)+1:  # Case 3: One number occurs maxF times, the rest occur the maxF-1 times
            res=i
        elif maxF*freq[maxF]+1==i: # Case 2: There is only one single occurence, the rest occur maxF times
            res=i
    return res

if __name__ == '__main__':
    print(maxEqualFreq([1,1,1,2,2,2]))
