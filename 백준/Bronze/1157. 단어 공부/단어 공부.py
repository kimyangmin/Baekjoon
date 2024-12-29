word = input().upper()
word_dict = {}
ls = []
for a in word:
    if a not in word_dict:
        word_dict[a] = 1
    else:
        word_dict[a] += 1

for a in word:
    if word_dict[a] == max(word_dict.values()) and a not in ls:
        ls.append(a)

if len(ls) > 1:
    print("?")
else:
    print(ls[0])