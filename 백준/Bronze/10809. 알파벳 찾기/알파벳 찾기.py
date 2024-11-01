S = input()
alpha = []
asc = 97
cnt = []
for i in range(26):
    alpha.append(-1)
    cnt.append(0)

for i in range(26):
    for j in range(len(S)):
        if S[j] == chr(asc+i) and cnt[i] == 0:
            alpha[i] = j
            cnt[i] += 1

print(" ".join(map(str,alpha)))