import sys

input = sys.stdin.readline

n = int(input())

target = input().rstrip()

def check_similar(word):
	cp_target = list(target)
	diff_count = 0

	for _ in range(len(word)):
		w = word.pop(0)
		if w in cp_target:
			cp_target.remove(w)
		else:
			diff_count += 1
	
	if len(cp_target) > 1 or diff_count > 1:
		return False
	return True

count = 0

for _ in range(n - 1):
	word = list(input().rstrip())
	if check_similar(word) == True:
		count += 1

print(count)
