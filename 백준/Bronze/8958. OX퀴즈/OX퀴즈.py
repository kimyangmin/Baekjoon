T = int(input())

for _ in range(T):
    a = 1
    score = 0
    b = input()
    for i in b:
        if i == 'O':
            score += a
            a += 1
        else:
            a = 1
    print(score)