N = int(input())
F = int(input())

sN = str(N)
sN = sN[:-2]
sN += "00"
iN = int(sN)
# print(iN)
a = 0

while True:
    if (iN + a) % F != 0:
        a += 1
    else:
        break

print(str(iN+a)[-2:])