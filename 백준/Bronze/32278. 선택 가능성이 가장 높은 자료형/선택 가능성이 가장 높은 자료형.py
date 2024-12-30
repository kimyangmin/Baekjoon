N = int(input())

if N >= -2**15 and N <= (2**15)-1:
    print("short")
elif N >= -2**31 and N <= (2**31)-1:
    print("int")
else:
    print("long long")