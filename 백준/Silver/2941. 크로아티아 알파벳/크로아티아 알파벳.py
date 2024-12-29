word = input()
alpha = ["c=", "c-", "d-", "lj", "nj", "s=", "z="]
count = 0

count += word.count("dz=")
word = word.replace("dz=", " ")

for al in alpha:
    if al in word:
        count += word.count(al)
        word = word.replace(al, " ")

word = word.replace(" ", "")
count += len(word)

print(count)