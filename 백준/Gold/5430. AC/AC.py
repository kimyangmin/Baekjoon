import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

def parse(s:str):
    a = s[1:-1]
    a = a.replace(",", " ")

    return deque(map(int, a.split()))

for _ in range(T):
    p = input().rstrip()
    n = int(input())
    x = parse(input().rstrip())
    flag = False
    test = False

    if not x and p.count("D") != 0:
        test = True

    # if p.count("R") == len(p) and n != 1:
    #     if p.count("R") % 2 == 0:
    #         pass
    #     else:
    #         flag = True
    #     test = True

    for s in p:
        # print(x)
        if test:
            break

        if s == "R":
            if len(x) != 1:
                
                flag = not flag
        if s == "D":
            if not x:
                test = True
                break
            else:
                if flag:
                    x.pop()
                else:
                    x.popleft()
    if not test:
        if flag:    
            x.reverse()
        
        a = list(x)
        print(str(a).replace(" ", ""))
    else:
        print("error")