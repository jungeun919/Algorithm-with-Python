# l : 사용 일수
# p : 연속 일수
# v : 휴가 일수

# 5 8 20 -> 14 (5 + (3) + 5 + (3) + 4)
# 5 8 17 -> 11 (5 + (3) + 5 + (3) + 1)
# 5 8 22 -> 15 (5 + (3) + 5 + (3) + 5)

idx = 1
while True:
    l, p, v = map(int, input().split())
    
    if l == p == v == 0:
        break
    
    full = v // p
    rest = v % p
    if l < rest:
        rest = l
    res = full * l + rest
    print("Case %d: %d" % (idx, res))
    idx += 1
