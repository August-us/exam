from typing import List
'''
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的每个数字在每个组合中只能使用一次。


说明：
所有数字（包括 target）都是正整数。
解集不能包含重复的组合。 
示例 1:
输入: candidates = [10,1,2,7,6,1,5], target = 8,
所求解集为:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
示例 2:

输入: candidates = [2,5,2,1,2], target = 5,
所求解集为:
[
  [1,2,2],
  [5]
]
'''
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort(reverse=True)
        if not candidates or target<candidates[-1]:
            return []

        return self.combinationSumCore(candidates,0,target)

    def combinationSumCore(self, candidates: List[int],start:int, target: int) -> List[List[int]]:
        if start==len( candidates) or target < candidates[-1]:
            return []
        res=[]
        while start<len(candidates):
            n=candidates[start]
            if target<n:
                start+=1
            elif target==n:
                res.append([n]*(target//n))
            else:
                r=self.combinationSumCore(candidates,start+1, target - n)
                for i in r:
                    if i:
                        res.append([n]+i)
                start+=1
            while start < len(candidates) and candidates[start] == n:
                start += 1
        return res


candidates =[1]
target=1
print(Solution().combinationSum2(candidates,target))