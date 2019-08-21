a=int(input())
list_input1=[]
list_input2=[]
max1=0
max2=0
for i in range(a):
    task=input().split(' ')
    for i in range(len(task)):
        task[i]=int(task[i])
    if task[0]==1:
        if task[2]>max1:
            max1=task[2]
        list_input1.append(task)
    else:
        if task[1]>max2:
            max2=task[1]
        list_input2.append(task)
l1=[0]*(max1+1)
l2=[0]*(max2+1)
for i in list_input1:
    for j in range(i[1],i[2]+1):
        if l1[j]==0:
            l1[j] = i[3]
        if i[3]>l1[j]:
            l1[j]=i[3]
for i in list_input2:
    if l2[i[1]]==0:
        l2[i[1]] = i[2]
    if i[2]>l2[i[1]]:
        l2[i[1]]=i[2]
score=0
for i in l1:
    score+=i
for i in l2:
    score += i
print (score)
