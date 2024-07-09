import sys

input = sys.stdin.readline

N = int(input()) # 스위치 개수
status = [-1] + list(map(int, input().split())) # 스위치 상태
M = int(input()) # 학생 수

def switch(num):
    if status[num] == 0:
        status[num] = 1
    else:
        status[num] = 0

for _ in range(M):
    gender, num = map(int, input().split())

    if gender == 1: # 남자
        for i in range(num, N+1, num):
            switch(i)

    elif gender == 2: # 여자
        switch(num)
        for j in range(N//2):
            if num + j > N or num - j < 1:
                break
            if status[num+j] == status[num-j]:
                switch(num+j)
                switch(num-j)
            else:
                break

for i in range(1, N+1):
    print(status[i], end=" ")
    if i % 20 == 0:
        print()
