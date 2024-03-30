# n : 배열의 크기
# m : 숫자가 더해지는 횟수
# k : 연속해서 최대 k번까지 더함
n, m, k = map(int, input().split())

data = list(map(int, input().split()))

data.sort()
first = data[n - 1]
second = data[n - 2]

count = int(m / (k + 1)) * k
count += m % (k + 1)

result = 0
result += (count) * first
result += (m - count) * second

print(result)
