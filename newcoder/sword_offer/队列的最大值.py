# 给定一个数组和一个滑动窗口的大小，找出所有滑动窗口中的最大值

def maxInWindows(nums,size):
    maxWindow=[]
    maxNumber=[]
    for i in range(0,len(nums)):
        if not maxWindow or nums[i]>nums[maxWindow[0]]:
            maxWindow=[i]
        else:
            if nums[i]>nums[maxWindow[-1]]:
                maxWindow[-1]=i
            else:
                maxWindow.append(i)
        if i>=size-1 and (i+1)-size<=maxWindow[0]:
            maxNumber.append(nums[maxWindow[0]])
        if (i+1)-size>=maxWindow[0]:
            maxWindow.pop(0)
    return maxNumber
print(maxInWindows([10,14,12,11],0))


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