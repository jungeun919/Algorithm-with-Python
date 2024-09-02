n, w, L = map(int, input().split()) # 트럭 수, 다리 길이, 최대하중
trucks = list(map(int, input().split()))

bridge = [0] * w
time = 0

while bridge:
	bridge.pop(0)
	if trucks:
		if sum(bridge) + trucks[0] <= L:
			bridge.append(trucks[0])
			trucks.pop(0)
		else:
			bridge.append(0) # 빈 공간
	time += 1

print(time)
