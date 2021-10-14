# 1부터 100까지 모두 더하는 Code를 <pass> 부분에 완성하세요. for를 사용해야 합니다.

s = 0

for i in range(1, 101):
    s += i
    # print("i의 값: %d\ts의 값: %d" % (i, s))
    print('i의 값: {}\ts의 값: {}'.format(i, s))