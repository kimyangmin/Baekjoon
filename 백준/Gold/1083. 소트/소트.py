import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().rstrip().split()))
S = int(input())

for i in range(N):
    if S == 0:
        break

    idx = i
    for j in range(i+1, min(N, i+S+1)):
        if A[j] > A[idx]:
            idx = j
    
    for j in range(idx, i, -1):
        A[j], A[j-1] = A[j-1], A[j]
    
    S -= (idx - i)

print(" ".join(map(str, A)))