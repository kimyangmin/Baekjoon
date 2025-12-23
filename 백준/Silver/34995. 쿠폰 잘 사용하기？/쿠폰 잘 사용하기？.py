n, ns = input().split()
n = int(n)

a = int(input())

if ns.isnumeric():
    # print(ns.isnumeric())
    if a <= int(ns):
        print(ns)
    else:
        print(-1)

else:
    ns = ns.replace("?", "9")
    if a <= int(ns):
        print(ns)
    else:
        print(-1)