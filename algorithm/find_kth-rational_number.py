from algorithm.heap_sort import get_rank_num

if __name__=="__main__":
    number=int(input())
    rank=[]
    result=[]
    dict_result={}
    for i in range(number):
        tmp_list1=[]
        tmp_list = []
        cont=input().split(' ')
        k=int(cont[0])
        for i in range(1,len(cont)):
            tmp_list1.append(int(cont[i]))
        for i in range(len(tmp_list1)):
            for j in range(i+1,len(tmp_list1)):
                a=float(tmp_list1[i])/tmp_list1[j]
                tmp_list.append(a)
                dict_result[a]=(tmp_list1[i],tmp_list1[j])
        result.append(get_rank_num(3,tmp_list,0,len(tmp_list)-1))

    for i in result:
        for x in dict_result[i]:
            print (x,end=' ')
