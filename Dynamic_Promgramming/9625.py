# i a b
# 0 1 0 (A)
# 1 0 1 (B)
# 2 1 1 (BA)
# 3 1 2 (BAB)
# 4 2 3 (BABBA)
# 5 3 5 (BABBABAB)

k = int(input())

a, b = 1, 0
for _ in range(k):
    a, b = b, a + b
print(a, b)
