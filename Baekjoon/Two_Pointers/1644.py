n = int(input())

prime_num = []
is_prime = [True] * (n+1)
is_prime[0] = False
is_prime[1] = False

for i in range(2, n+1):
    if is_prime[i]:
        prime_num.append(i)
        for j in range(i*2, n+1, i):
            is_prime[j] = False

count = 0

start, end = 0, 1
while start < end and end <= len(prime_num):
    temp = sum(prime_num[start:end])
    if temp == n:
        count += 1
        start += 1
    elif temp < n:
        end += 1
    else:
        start += 1

print(count)
