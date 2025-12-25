n = int(input())
doro = list(input().split())
print_doro = ""
for i in range(n):
    if i != n-1:
        print_doro += (doro[i] + "DORO ")
    else:
        print_doro += (doro[i] + "DORO")
        
print(print_doro)