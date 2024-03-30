# 절댓값 구하기

import math

# 1. 부호 판단
def abs_sign(a):
    if a >= 0:
        return a
    else:
        return -a

# 2. 제곱후 제곱근
def abs_square(a):
    b = a * a
    return math.sqrt(b)

print(abs_sign(5)) # 5
print(abs_sign(-5)) # 5

print(abs_square(3)) # 3
print(abs_square(-3)) # 3