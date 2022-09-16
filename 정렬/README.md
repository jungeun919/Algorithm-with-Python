# Sort

* 정렬이란 데이터를 특정한 기준에 따라서 순서대로 나열하는 것을 의미
* 정렬은 이진 탐색의 전처리 과정

# 선택 정렬 (Selection Sort)
* 매번 가장 작은 것을 선택해서 앞으로 보내는 과정을 반복
* 시간복잡도 : O(N^2)
```python
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
	min_index = i
	for j in range(i + 1, len(array)):
		if array[min_index] > array[j]:
			min_index = j
	array[i], array[min_index] = array[min_index], array[i]

print(array)
```

# 삽입 정렬 (Insertion Sort)
* 필요할 때만 위치를 바꾸므로 '데이터가 거의 정렬되어 있을 때' 훨씬 효율적
* 특정한 데이터가 적절한 위치에 들어가기 이전에, 그 앞까지의 데이터는 이미 정렬되어 있다고 가정
* 시간복잡도 : O(N^2)
* 최선의 경우 : O(N) -> 정렬이 거의 되어 있는 상황
```python
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
	for j in range(i, 0, -1):
		if array[j] < array[j - 1]:
			array[j], array[j - 1] = array[j - 1], array[j]
		else:
			break

print(array)
```

# 퀵 정렬 (Quick Sort)
* 피벗(기준)을 설정한 다음 큰 수와 작은 수를 교환한 후 리스트를 반으로 나누는 방식으로 동작
* 피벗을 설정하고 리스트를 분할하는 방법에 따라서 여러 가지 방식으로 퀵 정렬을 구분
* 퀵 정렬을 재귀 함수 형태로 작성했을 때 종료 조건 -> 리스트의 원소가 1개일 때
* 시간복잡도 : O(N * logN)
* 최악의 경우 : O(N^2) -> 이미 정렬되어 있는 경우
```python
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
	if start >= end:
		return
	pivot = start
	left = start + 1
	right = end

	while left <= right:
		while left <= end and array[left] <= array[pivot]:
			left += 1
		while right > start and array[right] >= array[pivot]:
			right -= 1
		if left > right:
			array[right], array[pivot] = array[pivot], array[right]
		else:
			array[left], array[right] = array[right], array[left]
	
	quick_sort(array, start, right - 1)
	quick_sort(array, right + 1, end)

quick_sort(array, 0, len(array) - 1)
print(array)
```

```python
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
	if len(array) <= 1:
		return array
	
	pivot = array[0]
	tail = array[1:]

	left_side = [x for x in tail if x <= pivot]
	right_side = [x for x in tail if x > pivot]

	return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))
```

# 계수 정렬 (Counting Sort)
* 특정한 조건이 부합할 때만 사용할 수 있자만 매우 빠른 알고리즘
* 데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때만 사용 가능 (max - min < 1,000,000)
* 모든 크기를 담을 수 있는 크기의 리스트(배열)를 선언하고 그 안에 정렬에 대한 정보를 담는다는 특징을 가짐
* 동일한 값을 가지는 데이터가 여러 개 등장할 때 적합
* 모든 데이터가 양의 정수인 상황에서 데이터의 개수가 N, 데이터 중 최댓값의 크기가 K일 때
* 시간복잡도 : O(N + K) -> 최악의 경우에도 보장
* 공간복잡도 : O(N + K)
```python
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

count = [0] * (max(array) + 1)

for i in range(len(array)):
	count[array[i]] += 1

for i in range(len(count)):
	for j in range(count[i]):
		print(i, end = ' ')
```

# 파이썬 정렬 라이브러리
* sorted() 함수
	* 리스트, 딕셔너리 자료형 등을 입력받음
	* 집합 자료형이나 딕셔너리 자료형을 입력받아도 결과는 리스트 자료형
* sort() 함수
	* 리스트 객체의 내장 함수
	* 별도의 정렬된 리스트가 반환되지 않고 내부 원소가 바로 정렬
