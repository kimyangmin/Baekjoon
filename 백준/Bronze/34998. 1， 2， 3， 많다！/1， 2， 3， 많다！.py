n = int(input())
for _ in range(n):
    x = int(input())
    a = input()
    if a.find("!") == -1:
        answer = eval(a)
        if answer > 9:
            print("!")
        else:
            print(answer)
    else:
        print("!")