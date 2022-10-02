# n : 떡의 개수
# m : 요청한 떡의 길이
# array : 각 떡의 개별 높이 정보
n, m = list(map(int, input().split(' ')))
array = list(map(int, input().split()))

start = 0
end = max(array)

result = 0
while (start <= end):
	total = 0
	mid = (start + end) // 2

	for x in array:
		if x > mid:
			total += x - mid

	# 떡의 양이 부족한 경우
	if total < m:
		end = mid - 1
	# 떡의 양이 충분할 경우
	else:
		result = mid
		start = mid + 1

print(result)
