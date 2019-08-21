if __name__=="__main__":
    number=int(input())
    input_cont=[]
    result=[]
    for cont in range(number):
        input_cont.append(list(map(int,input().split(' ')[1:])))
    for list_cont in input_cont:
        for cycle in range(1,list_cont[-1]-list_cont[0]+1):
            flag=1
            for list_cont_cont in list_cont:
                if list_cont_cont+cycle<list_cont[-1] and list_cont_cont+cycle not in list_cont:
                    flag=0
                    break
                if list_cont_cont - cycle > list_cont[0] and list_cont_cont-cycle not in list_cont:
                    flag=0
                    break
            if flag==1:
                result.append(cycle)
                break

    for result_cont in result:
        print (result_cont)
    a='1'

