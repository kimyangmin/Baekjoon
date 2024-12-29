pieces = [1, 1, 2, 2, 2, 8]

include_pieces = list(map(int, input().split())) # 0 1 2 2 2 7
no_pieces = [0, 0, 0, 0, 0, 0]
for i in range(len(include_pieces)):
    while include_pieces[i] != pieces[i]:
        if include_pieces[i] > pieces[i]:
            include_pieces[i] -= 1
            no_pieces[i] -= 1
        elif include_pieces[i] < pieces[i]:
            include_pieces[i] += 1
            no_pieces[i] += 1
            
a = []
for i in no_pieces:
    a.append(str(i))

print(" ".join(a))