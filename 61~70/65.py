# a = [1,2,3,4]
# b = [a,b,c,d]
# 이런 리스트가 있을 때 [[1,a],[b,2],[3,c],[d,4]] 이런식으로 a,b리스트가 번갈아가면서 출력되게 해주세요.

list1 = input("첫번째 리스트의 원소를 입력하세요: ").split(' ')
list2 = input("두번째 리스트의 원소를 입력하세요: ").split(' ')

res = []
count = 0
for i, j in zip(list1, list2):
	if count % 2 == 0:
		res.append([i, j])
	else:
		res.append([j, i])
	count += 1

print(res)