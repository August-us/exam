cinput=[]
str1=input()
while str1:
    cinput.append(str1)
    str1 = input()
i=0
print (str1)
while i<len(cinput):
    if cinput[i].startwith(';'):
        i+=1
        continue
    if cinput[i].startwith('[section'):
        section=cinput[i][-2]
        i+=1
        result={}
        while cinput[i].startwith('key'):
            k=cinput[i][3]
            key,value=input().strip().split('=')
            result[k]='{section'+section+'}{'+key+'}{'+value+'}'
            i+=1
    for v in result.values():
        print( v)

