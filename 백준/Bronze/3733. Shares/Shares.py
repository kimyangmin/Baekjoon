while True:
    try:
        N, S = list(map(int, input().split()))
        print(S // (N+1))
    except:
        break
    