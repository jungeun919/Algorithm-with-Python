# print("[방법1]")
# n = int(input())

# for i in range(1, n+1):
# 	print(" " * (n-i) + "*" * (2*i-1))


print("[방법2]")
n = int(input())

for i in range(1, n+1):
	for j in range(n-i):
		print(" ", end='')
	for j in range(i):
		print("* ", end='')
	print("")