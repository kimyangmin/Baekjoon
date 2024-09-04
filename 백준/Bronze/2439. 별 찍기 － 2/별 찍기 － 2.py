N = int(input())
output = ""
for i in range(N):
    for j in range(N-i-1):
        output += " "
    output += "*" * (N-(N-i-1))
    output += "\n"
print(output)