N = int(input())

for i in range(N-1):
    print((" " * (N-1-i)) + ("*" * (i*2+1)))
for i in range(N-1, -1, -1):
    print((" " * (N-1-i)) + ("*" * (i*2+1)))