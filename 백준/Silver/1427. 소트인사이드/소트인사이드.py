a = input()
lista = []
for i in a:
    lista.append(i)
lista.sort(reverse=True)
for i in lista:
    print(int(i),end="")