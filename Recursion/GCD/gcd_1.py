# 최대공약수 구하기

def gcd(a, b):
    i = min(a, b)
    while True:
        if a % i == 0 and b % i == 0:
            return i
        i -= 1

print(gcd(60, 25)) # 5
print(gcd(81, 27)) # 27