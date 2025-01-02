import sys
input = sys.stdin.readline
stack = []
def push(n):
    global stack
    stack.append(n)

T = int(input())
for _ in range(T):
    cmd = input()
    if 'push' in cmd:
        com, N = cmd.split()
        push(N)
    elif 'top' in cmd:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
    elif 'size' in cmd:
        print(len(stack))
    elif 'empty' in cmd:
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif 'pop' in cmd:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())