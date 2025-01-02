def fibo(n):
    ls = [0,1]
    if n == 0:
        return 0
    else:
        for i in range(2, n+1):
            ls.append(ls[i-1]+ls[i-2])
    return ls[-1]
print(fibo(int(input())))