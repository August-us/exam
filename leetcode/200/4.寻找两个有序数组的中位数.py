from typing import List
'''
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
你可以假设 nums1 和 nums2 不会同时为空。
示例 1:
nums1 = [1, 3]
nums2 = [2]
则中位数是 2.0
示例 2:
nums1 = [1, 2]
nums2 = [3, 4]
则中位数是 (2 + 3)/2 = 2.5
'''

'''
分析：肯定存在两个分片可以把两个数组分成两个部分，第一部分的最大数比第二部分的最小数小，并且两部分的数字差不超过1，且第一部分最多
比第二部分多1。则第一部分的数字数目为    (len(nums)+len(nums)+1)//2，因为下标从0开始。
     这个问题的另一个难点在于两个数组查找的边界条件不好找，
'''

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m,n=len(nums1),len(nums2)
        if m>n:
            nums1,nums2=nums2,nums1
            m,n=n,m
        # if len(nums1)==0:return
        mid=(len(nums1)+len(nums2)+1)>>1
        start=0
        end=len(nums1)

        while start<=end:
            split1 =(start+end)>>1
            split2 = mid - split1
            if split1<end and nums1[split1]<nums2[split2-1]:
                start=split1+1
            elif split1>start and nums1[split1-1]>nums2[split2]:
                end=split1-1
            else:
                if(split1==0):
                    maxLeft=nums2[split2-1]
                elif split2==0:
                    maxLeft=nums1[split1-1]
                else:
                    maxLeft=max(nums2[split2-1],nums1[split1-1])
                if (m^n)&1:
                    return maxLeft

                if(split1==m):
                    minRight=nums2[split2]
                elif split2==n:
                    minRight=nums1[split1]
                else:
                    minRight=min(nums2[split2],nums1[split1])
                return (maxLeft+minRight)/2.0

        return 0.

class Solution1:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m,n=len(nums1),len(nums2)
        if m>n:
            nums1,nums2=nums2,nums1
        mid=(len(nums1)+len(nums2)+1)>>1
        median=self.getMedian(nums1,nums2,0,len(nums1),mid)
        return median

    def getMedian(self, nums1, nums2, start, end,mid):
            split1 =(start+end)>>1
            split2 = mid - split1
            if split1<end and nums1[split1]<nums2[split2-1]:
                return self.getMedian(nums1,nums2,split1+1,end,mid)

            elif split1>start and nums1[split1-1]>nums2[split2]:
                return self.getMedian(nums1,nums2,start,split1-1,mid)

            else:
                if split1==0:
                    maxLeft=nums2[split2-1]
                elif split2==0:
                    maxLeft=nums1[split1-1]
                else:
                    maxLeft=max(nums2[split2-1],nums1[split1-1])
                if (len(nums1)+len(nums2))%2:
                    return maxLeft

                if(split1==len(nums1)):
                    minRight=nums2[split2]
                elif split2==len(nums2):
                    minRight=nums1[split1]
                else:
                    minRight=min(nums2[split2],nums1[split1])
                return (maxLeft+minRight)/2.0


nums1 = [1, 3]
nums2 = [2]

print(Solution1().findMedianSortedArrays(nums1,nums2))
print((2^3)&1)
