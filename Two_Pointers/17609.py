# 회문 : 0
# 유사회문 : 1
# 그 외 : 2

import sys

input = sys.stdin.readline

T = int(input())

def is_palindrome(word):
    left = 0
    right = len(word) - 1

    while left < right:
        if word[left] != word[right]:
            rm_left = word[left+1:right+1]
            if rm_left == rm_left[::-1]:
                return 1

            rm_right = word[left:right]
            if rm_right == rm_right[::-1]:
                return 1

            return 2

        left += 1
        right -= 1

    return 0

for _ in range(T):
    word = input().rstrip()
    diff = is_palindrome(word)
    print(diff)
