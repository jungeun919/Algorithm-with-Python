import sys

input = sys.stdin.readline

while True:
    try:
        hole_w = int(input()) # cm
        hole_w *= 10**7 # nm

        n = int(input())
        piece = []
        for _ in range(n):
            piece.append(int(input()))

        piece.sort()

        left, right = 0, n-1
        res = []

        while left < right:
            temp = piece[left] + piece[right]
            if temp == hole_w:
                res = [piece[left], piece[right]]
                break
            elif temp < hole_w:
                left += 1
            else:
                right -= 1

        if res:
            print("yes %d %d" % (res[0], res[1]))
        else:
            print("danger")

    except: # eof
        break
