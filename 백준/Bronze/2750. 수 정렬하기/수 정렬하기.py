N = int(input())
ls = []
for _ in range(N):
    ls.append(int(input()))

ls.sort()
for i in ls:
    print(i)