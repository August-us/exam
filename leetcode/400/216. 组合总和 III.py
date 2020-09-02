from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int,start=0) -> List[List[int]]:
        return ([[n]] if n < 10 else []) if k == 1 else [[i]+j for i in range(start+1, min((n+1)//2, 10)) for j in self.combinationSum3(k-1, n-i, i)]

    def combinationSum3(self, k: int, n: int, end=9) -> List[List[int]]:
        upper = (2*end-k+1)*k //2
        lower = (k+1)*k //2
        res = []
        if upper>= n >= lower:
            if k == 1:
                return [[n]]
            for i in range(end, 0, -1):
                for j in self.combinationSum3(k-1, n-i, i-1):
                    if j:res.append([i]+j)
            return res
        else:return []

print(Solution().combinationSum3(k = 3, n = 7))