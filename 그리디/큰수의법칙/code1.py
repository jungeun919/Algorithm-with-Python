# n : 배열의 크기
# m : 숫자가 더해지는 횟수
# k : 연속해서 최대 k번까지 더함
n, m, k = map(int, input().split())

data = list(map(int, input().split()))

data.sort()
first = data[n - 1]
second = data[n - 2]

result = 0

while True:
  for i in range(k):
    if m == 0:
      break
    result += first
    m -= 1
  if m == 0:
    break
  result += second
  m -= 1

print(result)