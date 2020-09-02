from typing import List

'''
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
示例:

输入: [0,1,0,2,1,0,1,3,2,1,2,1]
输出: 6

'''
class Solution:
    def trap1(self, height: List[int]) -> int:
        n=len(height)
        maxValue=0
        maxIndex=0
        for i,num in enumerate(height):
            if num>maxValue:
                maxValue=num
                maxIndex=i
        res=0
        curMax=0
        for begin in range(maxIndex):
            if height[begin]>curMax:
                curMax=height[begin]
            else:
                res+=curMax-height[begin]
        curMax = 0
        for begin in range(n-1,maxIndex,-1):
            if height[begin]>curMax:
                curMax = height[begin]
            else:
                res += curMax - height[begin]
        return res

    def trap_froce(self, height: List[int]) -> int:
        # 对于数组中的每个元素，我们找出下雨后水能达到的最高位置，等于两边最大高度的较小值减去当前高度的值。
        ans=0
        size=len(height)
        for i in range(1,size-1):
            max_left=max(height[:i+1])
            max_right=max(height[i:])
            ans+=min(max_left,max_right)-height[i]
        return ans

    def trap(self, height: List[int]) -> int: # 双指针
        left,right=0,len(height)-1
        leftMax=rightMax=0
        res=0
        while left<right:
            if height[left]<height[right]:
                if height[left]>=leftMax:
                    leftMax=height[left]
                else:
                    res+=leftMax-height[left]
                left+=1
            else:
                if height[right]>=rightMax:
                    rightMax=height[right]
                else:
                    res+=rightMax-height[right]
                right-=1
        return res






height=[0,1,0,2,1,0,1,3,2,1,2,1]
print(Solution().trap(height))
