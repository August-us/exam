# less函数用于创建大根堆
def less(left, right):
    return left<right

def greater(left,right):
    return left>right

def siftup(heap, startpos, pos,func=less):
    newitem = heap[pos]
    while pos>startpos:
        parentpos = (pos - 1) >> 1
        parent = heap[parentpos]
        if func(parent,newitem):
            heap[pos] = parent
            pos = parentpos
            continue
        break
    heap[pos] = newitem

def siftdown(heap, pos,func=less,endpos=None):
    if endpos is None:
        endpos=len(heap)
    newitem = heap[pos]
    childpos = 2*pos + 1    # leftmost child position
    while childpos<endpos:
        rightpos = childpos + 1
        if rightpos<endpos and func(heap[childpos],heap[rightpos]):
            childpos = rightpos
        if func(newitem,heap[childpos]):
            heap[pos] = heap[childpos]
            pos = childpos
            childpos = 2*pos + 1
        else:
            break

    heap[pos] = newitem
def heapRemove(heap: list, item, func=less):
    if item not in heap:return
    count = heap.index(item)
    if count==len(heap)-1:
        heap.pop()
        return
    a = heap.pop()
    heap[count] = a
    siftdown(heap, count, func=func)

def heappush(heap, item, func=less):
    heap.append(item)
    siftup(heap, 0, len(heap) - 1,func)

def heappop(heap,func=less):
    lastelt = heap.pop()
    if heap:
        returnitem = heap[0]
        heap[0] = lastelt
        siftdown(heap, 0,func)
        return returnitem
    return lastelt

def heapify(x, func=less):
    n=len(x)
    for i in reversed(range(n//2)):
        print(i,heap)
        siftdown(x, i,func=func)
    print(heap)


def HeapSort(heap):
    heapify(heap)
    for i in range(len(heap)-1,0,-1):
        heap[0],heap[i] = heap[i],heap[0]
        siftdown(heap, 0,endpos=i)

    return heap


class DymaicArray():
    _min=[]
    _max=[]
    def findMedian(self) -> float:
        if not self._max:
            raise Exception('No elements are available')
        if len(self._max) ^ len(self._min):
            return self._max[0]
        else:
            return (self._max[0]+self._min[0])/2

    def addNum(self, num: int) -> None:
        if len(self._max) ^ len(self._min):
            if num<self._max[0]:
               heappush(self._max,num,less)
               num=heappop(self._max,less)
            heappush(self._min,num,greater)
        else:
            if self._min and num>self._min[0]:
                heappush(self._min,num,greater)
                num=heappop(self._min,greater)
            heappush(self._max,num,less)



if __name__=="__main__":
    # heap=[int(i)  for i in input().split(' ')]
    import numpy as np
    # heap=np.random.choice(range(1,100),10).tolist()
    heap=[71, 11, 53, 20, 33, 34, 92, 22, 38, 40]
    print(HeapSort(heap))

    a = DymaicArray()
    a.addNum(1)
    print(a.findMedian())

