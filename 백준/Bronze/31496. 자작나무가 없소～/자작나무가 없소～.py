import sys
input = sys.stdin.readline

n, s = input().split()
n = int(n)

cnt = 0

for _ in range(n):
    a, b = input().split()
    b = int(b)

    words = a.split("_")
    
    if s in words:
        cnt += b

print(cnt)