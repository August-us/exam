# 索引传值
from typing import List


def permuteUnique_list(string):
    # 分析可知，交换两个字符的时候，如果后面的字符已经出现在这个位置，就会产生重复，如果要避免相同的字符回溯的时候出现在同一个位置，则加一个判断即可。
    def dfs(string,begin):
        if len(string)==begin+1:
            res.append( string[:])
            return
        alread[begin]=set()
        for i in range(begin,len(string)):
            if string[i] not in alread[begin]:
                alread[begin].add(string[i])
                string[i],string[begin]=string[begin],string[i]
                dfs(string,begin+1)
                string[i], string[begin] = string[begin], string[i]
    res=[]
    if not isinstance(string,list):
        string=list(string)
    alread = [set() for i in range(len(string))]

    dfs(string,0)
    return res
def permuteUnique( nums: List[int]) -> List[List[int]]:
    def dfs(nums, size, depth, path, used, res):
        if depth == size:
            res.append(path.copy())
            return
        for i in range(size):
            if not used[i]:
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue

                used[i] = True
                path.append(nums[i])
                dfs(nums, size, depth + 1, path, used, res)
                used[i] = False
                path.pop()

    size = len(nums)
    if size == 0:
        return []

    nums.sort()
    used = [False] * len(nums)
    res = []
    dfs(nums, size, 0, [], used, res)
    return res

def permute_list(string):
    def dfs(string,begin):
        if len(string)==begin+1:
            res.append(''.join(string))
            # res.append(string.copy())
            return
        for i in range(begin,len(string)):
            string[i],string[begin]=string[begin],string[i]
            dfs(string,begin+1)
            string[i], string[begin] = string[begin], string[i]
    res=[]
    if not isinstance(string,list):
        string=list(string)
    dfs(string,0)
    return res

# 拷贝传值
def permute(string):
    def dfs(string,path):
        for i in range(len(string)):
            dfs(string[:i]+string[i+1:],path+[string[i]])
        if len(string)==0:
            res.append(path)
    res=[]
    dfs(string,[])
    return res


# 以下两种方式采用哈希来去重，效率较低
def combination(string,n):
    res=set()

    def dfs(string,n,pre):
        if len(string) < n:
            return
        if n==0:
            res.add(''.join(pre))
            return
            # res.add(pre)
        dfs(string[1:],n-1,pre+string[0:1])
        dfs(string[1:],n,pre)
    dfs(string,n,'')
    return res

def combination_list(string,n):
    res=set()
    if not isinstance(string,list):
        string=list(string)
    def dfs(begin,n,pre):
        if len(string)-begin < n:
            return
        if n==0:
            # res.add(''.join(map(str,pre)))
            res.add(tuple(pre.copy()))

            return
        pre.append(string[begin])
        dfs(begin+1,n-1,pre)
        pre.pop()
        dfs(begin+1,n,pre)
    dfs(0,n,[])
    return res

# 从n个数中找出k个数的组合，返回列表
def combine( n: int, k: int) -> List[List[int]]:
    # 非常慢的一种回溯
    res = []
    n+=1
    cur=list(range(1,k))+[0]
    ind=k-1
    while -1<ind:
        if ind>0 :
            cur[ind]=max(cur[ind-1],cur[ind])
        cur[ind]=(cur[ind]+1)%n
        if cur[ind]==0:
            ind-=1
            # 回溯
        elif ind!=k-1:
            ind+=1
        else:
            res.append(cur.copy())
    return res

def combine_fast(self, n: int, k: int) -> List[List[int]]:
    '''
    按照字典序回溯
    4 3 2 1    4 3 2 1    4 3 2 1    4 3 2 1    4 3 2 1    4 3 2 1
    0 0 1 1    0 1 0 1    0 1 1 0    1 0 0 1    1 0 1 0    1 1 0 0

    1,2        1,3        2,3        1,4        2,4        3,4

    将 nums 初始化为从 1 到 k的整数序列。 将 n + 1添加为末尾元素，起到“哨兵”的作用。
    将指针设为列表的开头 j = 0.
    While j < k :
    将nums 中的前k个元素添加到输出中，换而言之，除了“哨兵”之外的全部元素。
    找到nums中的第一个满足 nums[j] + 1 != nums[j + 1]的元素，并将其加一
    nums[j]++ 以转到下一个组合。
    '''

    nums = list(range(1, k + 1)) + [n + 1]

    output, j = [], 0
    while j < k:
        # add current combination
        output.append(nums[:k])

        j = 0
        while j < k and nums[j + 1] == nums[j] + 1:
            nums[j] = j + 1
            j += 1
        nums[j] += 1
    return output


# 对已经排好序的数组进行去重组合，返回所有不重复的子集(不包括空集)
def combination_Dup(self, res,nums,cur=list(), start=0):
    pre=-1  # nums需要是已经排好序的数组，对于排好序的数组只需要记录上一个出现的数字就能防止重复
    for i in range(start,len(nums)):
        if(pre==-1 or pre!=nums[i]):
            cur.append(nums[i])
            res.append(cur.copy())
            self.combination_Dup(res,nums,cur,i+1)
            cur.pop()
            pre=nums[i]


# 返回n个数的第k个排列
def getPermutation(n: int, k: int) -> str:
    last=[str(i) for i in range(1,n+1)]
    i=perm=1
    k-=1
    res=[]
    for _ in range(2,n):perm*=_
    while k:
        res.append(last.pop(k//perm))
        k%=perm
        perm=perm//(n-i)
        i+=1
    res.extend(last)
    return ''.join(res)



if __name__ == '__main__':
    a=''.join(map(str,range(1,10)))
    a="abcdefghij"
    print(len(a))
    from time import time
    start=time()
    a='1234'
    for i in range(1,4):(print(combination(a,i)))
    print(len(permute(a)))
    print(time()-start)
    start=time()
    print(len(permute_list(a)))
    for i in range(1,4):(print(combination_list(a,i)))
    print(time()-start)
    print(getPermutation(4, 9))
