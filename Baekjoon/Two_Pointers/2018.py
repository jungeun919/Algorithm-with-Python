n = int(input())

start = 0
end = 0
total = 0
count = 0

while end <= n:
	if total < n:
		end += 1
		total += end
	elif total > n:
		total -= start
		start += 1
	else:
		count += 1
		end += 1
		total += end

print(count)
