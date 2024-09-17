N, M = map(int,input().split())

lst = []

for i in range(1, N+1):

    lst.append(i)

for Tcase in range(M):

    i, j = map(int,input().split())

    i -= 1

    j -= 1

    temp = lst[i]

    lst[i] = lst[j]

    lst[j] = temp

    

for i in lst:

    print(i, end=' ')