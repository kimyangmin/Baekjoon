import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
list_a = []
for i in range(N):
    list_a.append(int(input()))

list_a.sort()
for i in range(N):
    print(list_a[i])