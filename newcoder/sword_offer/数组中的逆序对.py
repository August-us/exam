# -*- coding:utf-8 -*-
# 在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组,求出这个数组中的逆序对的总数P。并将P对1000000007取模的结果输出。

class Solution2:
    def InversePairs1(self, array):
        # 采用排序之后对比序列，序列的位置差异代表最终要移动多少次才可以有序，然后前移和后移加起来除二，但是好像不对
        # 用这方方式显然{8,7,5,1} 和{7,8,5,1}的结果一致
        time=0
        tmp=sorted(array)
        for i in range(len(array)):
            time+=abs(i-tmp.index(array[i]))
        return time//2%1000000007
    def InversePairs(self, array):
        # 采用排序之后对比序列，序列的位置差异代表最终要移动多少次才可以有序，只计算前移，和上面InversePairs1结果一样
        time=0
        tmp=sorted(array)
        for i in range(len(array)):
            if i-tmp.index(array[i])>0:
                time+=i-tmp.index(array[i])
        return time%1000000007

# -*- coding:utf-8 -*-
class Solution1:
    def InversePairs(self, array):
        # 采用插排的思想，但是错误了
        time=0
        for i in range(1, len(array)):
            if array[i - 1] > array[i]:
                temp = array[i]
                index = i
                while index > 0 and array[index - 1] > temp:
                    array[index] = array[index - 1]
                    index -= 1
                    time+=1
                time%=1000000007

                array[index] = temp
        return time


class Solution3:
    def InversePairs(self, data):
        global count
        def MergeSort(lists):
            global count
            if len(lists) <= 1:
                return lists
            num = int( len(lists)/2 )
            left = MergeSort(lists[:num])
            right = MergeSort(lists[num:])
            r, l=0, 0
            result=[]
            while l<len(left) and r<len(right):
                if left[l] < right[r]:
                    result.append(left[l])
                    l += 1
                else:
                    result.append(right[r])
                    r += 1
                    count += len(left)-l
            result += right[r:]
            result += left[l:]
            return result
        MergeSort(data)
        return count%1000000007

    def InversePairs1(self, data):
        # 采用蒂姆排序
        global count
        def MergeSort(lists):
            global count
            if len(lists) <= 8:
                for i in range(1, len(lists)):
                    if lists[i - 1] > lists[i]:
                        temp = lists[i]
                        index = i
                        while index > 0 and lists[index - 1] > temp:
                            lists[index] = lists[index - 1]
                            index -= 1
                            count += 1
                        lists[index] = temp
                return lists
            num = int( len(lists)/2 )
            left = MergeSort(lists[:num])
            right = MergeSort(lists[num:])
            r, l=0, 0
            result=[]
            while l<len(left) and r<len(right):
                if left[l] < right[r]:
                    result.append(left[l])
                    l += 1
                else:
                    result.append(right[r])
                    r += 1
                    count += len(left)-l
            result += right[r:]
            result += left[l:]
            return result
        MergeSort(data)
        return count%1000000007

num=[364,637,341,406,747,995,234,971,571,219,993,407,416,366,315,301,601,650,418,355,460,505,360,965,516,648,727,667,465,849,455,181,486,149,588,233,144,
     174,557,67,746,550,474,162,268,142,463,221,882,576,604,739,288,569,256,936,275,401,497,82,935,983,583,523,697,478,147,795,380,973,958,115,773,870,259,
     655,446,863,735,784,3,671,433,630,425,930,64,266,235,187,284,665,874,80,45,848,38,811,267,575]
# 2519
count = 0
import time,random
num=random.sample(range(1,int(1e6)),int(5e5))
start=time.time()
print(Solution1().InversePairs(num))
print(time.time()-start)
start=time.time()
print(Solution3().InversePairs(num))
print(time.time()-start)