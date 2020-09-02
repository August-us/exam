from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        assert len(nums) !=0
        self.num = [0]*len(nums) + nums
        for i in range(len(nums)-1,0,-1):
            self.num[i] = self.num[i*2] + self.num[i*2+1]
        self.num[0] = len(nums)


    def update(self, i: int, val: int) -> None:
        i += self.num[0]
        val = self.num[i] - val
        while i:
            self.num[i] -= val
            i >>=1


    def sumRange(self, l: int, r: int) -> int:
        # return sum([l, r])
        l,r = l+self.num[0], self.num[0]+r
        res = 0
        while l<=r:
            if l&1:
                res += self.num[l]
                l += 1
            if r&1==0:
                res += self.num[r]
                r -= 1
            l //= 2
            r //=2
        return res



print(NumArray([1,2,3,4]))