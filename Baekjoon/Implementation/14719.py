h, w = map(int, input().split())
heights = list(map(int, input().split()))

total = 0

for i in range(1, w-1):
	left_max = max(heights[:i])
	right_max = max(heights[i+1:])

	small_height = min(left_max, right_max)

	if heights[i] < small_height:
		total += small_height - heights[i]

print(total)
