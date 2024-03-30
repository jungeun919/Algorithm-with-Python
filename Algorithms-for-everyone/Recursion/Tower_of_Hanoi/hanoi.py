# 하노이의 탑 알고리즘

# 총 3개의 기둥 (from_pos / aux_pos / to_pos)

def hanoi(n, from_pos, to_pos, aux_pos):
    if n == 1:
        print(from_pos, "->", to_pos)
        return

    # 원반 n-1개를 aux_pos로 이동 (보조기둥으로 to_pos를 사용)
    hanoi(n-1, from_pos, aux_pos, to_pos)
    # 가장 큰 원반을 목적지로 이동
    print(from_pos, "->", to_pos)
    # aux_pos에 있는 n-1개를 목적지로 이동 (보조기둥으로 from_pos를 사용)
    hanoi(n-1, aux_pos, to_pos, from_pos)

print("n(옮기려는 원반의 개수) = 1")
hanoi(1, 1, 3, 2)
print()

print("n(옮기려는 원반의 개수) = 2")
hanoi(2, 1, 3, 2)
print()

print("n(옮기려는 원반의 개수) = 3")
hanoi(3, 1, 3, 2)
print()