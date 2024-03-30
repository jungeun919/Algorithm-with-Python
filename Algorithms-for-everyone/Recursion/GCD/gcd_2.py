# 유클리드 방식으로 최대공약수 구하기

# gcd(a, b) = gcd(b, a%b)
# gcd(a, 0) = a

def gcd(a, b):
    print("gcd: ", a, b)
    if b == 0:
        return a
    return gcd(b, a%b)

print(gcd(60, 25)) # 5
print(gcd(81, 27)) # 27