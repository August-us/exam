# 给定一个数组和一个滑动窗口的大小，找出所有滑动窗口中的最大值

def maxInWindows(nums,size):
    maxWindow=[]
    maxNumber=[]
    for i in range(0,len(nums)):
        while maxWindow and nums[i] > nums[maxWindow[-1]]:
            maxWindow.pop()
        else:
            maxWindow.append(i)
        if i>=size-1 and (i+1)-size<=maxWindow[0]:
            maxNumber.append(nums[maxWindow[0]])
        if (i+1)-size>=maxWindow[0]:
            maxWindow.pop(0)
    return maxNumber
print(maxInWindows([9,10,9,-7,-4,-8,2,-6], 5))


# 这个题目可以扩展为，如果需要构造一个队列，要用O(1)的时间找到队列的最大值，则需要构建一个辅助队列。
class MaxQueue:
    queue=[]
    maxQueue=[]
    def push_back(self,value):
        if not self.maxQueue or value>self.maxQueue[0]:
            self.maxWindow=[value]
        else:
            if value>self.maxQueue[-1]:
                self.maxQueue[-1]=value
            else:
                self.maxQueue.append(value)
    def pop_front(self):
        value=self.queue.pop(0)
        if value==self.maxQueue[0]:
            self.maxQueue.pop(0)
        return value


    def max(self):
        return self.maxQueue[0]


class Solution:
    def maxSlidingWindow(self, nums: 'List[int]', k: 'int') -> 'List[int]':
        n = len(nums)
        if n * k == 0:
            return []
        if k == 1:
            return nums

        left = [0] * n
        left[0] = nums[0]
        right = [0] * n
        right[n - 1] = nums[n - 1]
        for i in range(1, n):
            # from left to right
            if i % k == 0:
                # block start
                left[i] = nums[i]
            else:
                left[i] = max(left[i - 1], nums[i])
            # from right to left
            j = n - i - 1
            if (j + 1) % k == 0:
                # block end
                right[j] = nums[j]
            else:
                right[j] = max(right[j + 1], nums[j])

        output = []
        for i in range(n - k + 1):
            output.append(max(left[i + k - 1], right[i]))

        return output
print(Solution().maxSlidingWindow([9,10,9,-7,-4,-8,2,-6], 5))
