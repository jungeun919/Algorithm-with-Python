n = int(input())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

# b는 재배열x (문제에 명시됨)
a_list.sort()
sum = 0

for i in range(n):
    a = a_list[i]
    b = b_list.pop(b_list.index(max(b_list)))
    sum += a * b
    
print(sum)
