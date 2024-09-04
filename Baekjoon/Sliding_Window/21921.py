N, X = map(int, input().split()) # 지난 일수, 기간
visitor = list(map(int, input().split()))

if max(visitor) == 0:
	print("SAD")
else:
	curr_visitor = sum(visitor[:X])
	max_visitor = curr_visitor
	count = 1

	for i in range(X, N):
		# 슬라이딩 윈도우
		# 윈도우: 고정 길이, 단방향
		# 구간 합에서 맨 앞 인덱스 빼기, 마지막 다음 인덱스 더하기
		curr_visitor -= visitor[i - X]
		curr_visitor += visitor[i]

		if curr_visitor > max_visitor:
			max_visitor = curr_visitor
			count = 1
		elif curr_visitor == max_visitor:
			count += 1
	
	print(max_visitor)
	print(count)
