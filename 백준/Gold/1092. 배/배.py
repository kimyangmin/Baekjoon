import sys
input = sys.stdin.readline

n = int(input())

crain = list(map(int, input().split()))
boxN = int(input())
boxW = list(map(int, input().split()))

crain.sort(reverse=True)
boxW.sort(reverse=True)

class Main():
    def __init__(self):
        self.n = n
        self.crain = crain
        self.boxN = boxN
        self.boxW = boxW
        

    def run():
        minute = 0
        # print(crain)
        # print(boxW)

        if max(crain) < max(boxW):
            print(-1)
        else:
            while boxW:
                for c in crain:
                    if c < boxW[-1]:
                        break
                    for box in boxW:
                        if c >= box:
                            # print(f"{c} : {boxW}")
                            boxW.pop(boxW.index(box))
                            break

                    if not boxW:
                        break
                
                minute += 1
            print(minute)
Main.run()