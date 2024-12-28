def fibonacci(n):
    fibonacci_list = []
    use_dict = {0:0, 1:0}
    
    if n <= 1:
        use_dict[n] += 1
        
    elif n == 2:
        use_dict = {0:1, 1:1}
    else:
        fibonacci_list = [0, 1]
        for i in range(2, n+1):
            fibonacci_list.append(fibonacci_list[i-2] + fibonacci_list[i-1])
        use_dict[0] = fibonacci_list[-2]
        use_dict[1] = fibonacci_list[-1]

    return f"{use_dict[0]} {use_dict[1]}"

a = int(input())
for s in range(a):
    print(fibonacci(int(input())))