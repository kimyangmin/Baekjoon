dice = list(map(int,input().split()))

if dice[0] == dice[1] and dice[1] == dice[2]:
    print(10000 + dice[1] * 1000)
elif dice[0] == dice[1] or dice[1] == dice[2] or dice[0] == dice[2]:
    if dice[0] == dice[1]:
        print(1000 + dice[0] * 100)
    elif dice[1] == dice[2]:
        print(1000 + dice[1] * 100)
    else:
        print(1000 + dice[0] * 100)
else :
    print(max(dice) * 100)