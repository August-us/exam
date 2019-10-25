while True:
    try:
        A=[int(i) for i in input().split(' ')]
        if len(A)!=6:
            break
        visited=[0 for i in range(6)]
        def dfs(i):
            visited[i] = 1
            for j in range(len(A)):
                if not visited[j]:
                    tmp = abs(A[j] - A[i])
                    if tmp == 1 or tmp == 10:
                        dfs(j)
        dfs(0)
        if 0 in visited:
            print(0)
        else:
            print(1)
    except:
        break

'''
1 2 3 4 5 11
1 2 11 14 25 15
^D
'''