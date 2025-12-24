import sys
input = sys.stdin.readline

N = int(input())

deck = []

def push_front(x):
    deck.insert(0, x)

def push_back(x):
    deck.append(x)

def pop_front():
    if not deck:
        print(-1)
        return
    print(deck.pop(0))

def pop_back():
    if not deck:
        print(-1)
        return
    print(deck.pop())

def size():
    print(len(deck))

def empty():
    if not deck:
        print(1)
        return
    else:
        print(0)

def front():
    if not deck:
        print(-1)
        return
    print(deck[0])

def back():
    if not deck:
        print(-1)
        return
    print(deck[-1])

for _ in range(N):
    cmd = list(input().split())

    if len(cmd) == 1:
        eval(f"{cmd[0]}()")

    else:
        eval(f"{cmd[0]}({cmd[1]})")