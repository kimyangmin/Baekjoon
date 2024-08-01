A, B = map(int,input().split())
C = int(input())
B += C

while(True):
    if (B) >= 60:
        A += 1
        B -= 60
    else:
        break
    if A == 24:
        A = 0

print("{} {}".format(A, B))