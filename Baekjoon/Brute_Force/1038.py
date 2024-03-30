from itertools import combinations

n = int(input())

arr = []

for digit in range(1, 11):
    for comb in combinations(range(10), digit): # 0~9 숫자로 만든 digit 자리수 조합
        sorted_comb = sorted(list(comb), reverse=True)
        arr.append(int("".join(map(str, sorted_comb))))

arr.sort()

if len(arr) > n:
    print(arr[n])
else:
    print(-1)
