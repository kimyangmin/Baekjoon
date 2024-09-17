a = []

b = []

c = []

for i in range(10):

    a.append(int(input()))

for i in a:

    b.append(i%42)

    

for i in b:

    if i not in c:

        c.append(i)

        

print(len(c))