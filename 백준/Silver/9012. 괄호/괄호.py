N = int(input())

for _ in range(N):
    a = input()
    while "()" in a:
        a = a.replace("()", "")
    
    if a == "":
        print("YES")
    else:
        print("NO")