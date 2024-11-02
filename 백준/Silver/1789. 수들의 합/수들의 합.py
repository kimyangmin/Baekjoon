import math

# 입력을 받습니다.
S = int(input())

# 최대 N을 계산합니다.
max_N = int((-1 + math.sqrt(1 + 8 * S)) // 2)

# 결과를 출력합니다.
print(max_N)
