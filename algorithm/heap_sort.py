def MAX_Heapify(heap,HeapSize,root):
    left = 2*root + 1
    right = left + 1
    larger = root
    if left < HeapSize and heap[larger] < heap[left]:
    # if left < HeapSize and heap[larger] > heap[left]:#minHeap
        larger = left
    if right < HeapSize and heap[larger] < heap[right]:
    # if right < HeapSize and heap[larger] > heap[right]:#minHeap
        larger = right
    if larger != root:
        heap[larger],heap[root] = heap[root],heap[larger]
        MAX_Heapify(heap, HeapSize, larger)

def Build_MAX_Heap(heap):
    HeapSize = len(heap)
    for i in range((HeapSize -2)//2,-1,-1):
        MAX_Heapify(heap,HeapSize,i)

def HeapSort(heap,prior=0):
    if prior==0:
        prior=len(heap)
    Build_MAX_Heap(heap)
    for i in range(len(heap)-1,len(heap)-prior-1,-1):
        heap[0],heap[i] = heap[i],heap[0]
        MAX_Heapify(heap, i, 0)
    return heap


def partition(arr,start,end):
    i=start+1
    j=i
    while(i<=end and j<=end):
        if arr[j]>arr[start]:
            # rankth small
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
        j+=1
    arr[start], arr[i-1] = arr[i-1], arr[start]
    return i-1


def get_rank_num(rank,arr,start,end):
    if start==end:
        return arr[start]
    index=partition(arr,start,end)
    if end-index+1==rank:
        return arr[index]
    elif end-index+1>rank:
        return get_rank_num(rank,arr,index+1,end)
    else:return get_rank_num(rank-end+index-1,arr,start,index-1)



if __name__=="__main__":
    heap=[]
    a=[30, 50, 57, 77, 62, 78, 94, 80, 84]
    cont = input().split(' ')
    for i in cont:
        heap.append(int(i))
    # print HeapSort(a)
    print (get_rank_num(8,a,0,len(a)-1))
