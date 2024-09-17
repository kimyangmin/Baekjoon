lst = []

no = []

for i in range(1, 29):

    lst.append(int(input()))

for i in range(1,31):

    if i not in lst:

        no.append(i)

print(no[0])

print(no[1])