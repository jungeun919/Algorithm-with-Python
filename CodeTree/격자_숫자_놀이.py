from collections import Counter

r, c, k = map(int, input().split())

arr = []
for _ in range(3):
    arr.append(list(map(int, input().split())))

def sort_rows(row, col):
    new_arr = []
    max_col = 0

    for i in range(row):
        new_row = []

        # 0 제외하고 카운트
        filtered_row = [num for num in arr[i] if num != 0]
        # a. 출현 빈도 수 정렬
        # b. 출현 횟수 같을 경우, 숫자 순으로 정렬
        counter = Counter(filtered_row) # Counter({숫자1: 개수}, {숫자2: 개수})
        sorted_row = sorted(counter.items(), key=lambda x: (x[1], x[0]))

        for i in sorted_row:
            new_row.extend(i)
        
        new_arr.append(new_row)
        max_col = max(max_col, len(new_row))
    
    zero_arr = []
    for row in new_arr:
        zero_arr.append(row + [0] * (max_col - len(row)))
    return zero_arr

def sort_cols(row, col):
    new_arr = [[] for _ in range(col)]
    max_row = 0

    for j in range(col):
        new_col = []

        filtered_col = [arr[i][j] for i in range(row) if arr[i][j] != 0]
        counter = Counter(filtered_col)
        sorted_col = sorted(counter.items(), key=lambda x: (x[1], x[0]))
        
        for i in sorted_col:
            new_arr[j].extend(i)
            max_row = max(max_row, len(new_arr[j]))


    zero_arr = [[0] * col for _ in range(max_row)]
    for j in range(col):
        for i in range(len(new_arr[j])):
            zero_arr[i][j] = new_arr[j][i]
    return zero_arr

time = 0
while True:
    if time > 100:
        print(-1)
        break
    
    row, col = len(arr), len(arr[0])
    if row >= r and col >= c and arr[r-1][c-1] == k:
        print(time)
        break
    
    if row >= col:
        arr = sort_rows(row, col)
    else:
        arr = sort_cols(row, col)
    
    time += 1
