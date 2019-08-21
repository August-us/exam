# def qsort(L):
#     # if len(L) <= 1: return L
#     # return qsort([x for x in L[1:] if x<=L[0]])+[L[0]]+qsort([x for x in L if x>L[0]])
#     return L if len(L) <= 1 else qsort([x for x in L[1:] if x<=L[0]])+[L[0]]+qsort([x for x in L if x>L[0]])

q_sort=lambda L: L if len(L) <= 1 else q_sort([x for x in L[1:] if x<=L[0]])+[L[0]]+q_sort([x for x in L if x>L[0]])
# A = [5, -4, 6, 3, 7, 11, 1, 2]
# print (q_sort(A))

