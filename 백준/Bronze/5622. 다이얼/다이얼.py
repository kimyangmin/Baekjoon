alpha = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
input = input()
sec = 0

for inp in input:
    flag = False
    sec += 2
    for word in alpha:
        if flag == True:
            break
        sec += 1
        for w in word:
            if inp == w:
                flag = True

print(sec)