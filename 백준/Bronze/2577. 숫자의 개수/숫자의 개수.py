A = int(input())
B = int(input())
C = int(input())

total = str(A*B*C)

for i in range(10):
    print(total.count(str(i)))