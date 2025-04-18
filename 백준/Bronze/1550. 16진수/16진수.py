a = input()
hexnum = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

num = []

for i in range(len(a)):
    for j in range(len(hexnum)):
        if a[i] == hexnum[j]:
            num.append(j)


b = 0
sum = 0

for i in range(len(num)-1, -1, -1):
    if num[i] == 0:
        b += 1
    else:
        sum += (num[i] * (16**b))
        b += 1
print(sum)