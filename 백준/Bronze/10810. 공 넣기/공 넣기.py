N, M = map(int,input().split())

basket = []

for i in range(N):

    basket.append(0)

    

for t in range(M):

    i, j, k = map(int,input().split())

    for z in range(i-1,j):

        basket[z] = k

for i in basket:
    print(i,end=' ')