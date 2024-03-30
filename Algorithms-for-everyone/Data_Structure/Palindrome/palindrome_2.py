# 주어진 문장이 회문인지 확인 (문자열의 앞뒤를 서로 비교)

def palindrome(s):
    i = 0 # 문자열의 앞에서 비교할 위치
    j = len(s) - 1 # 문자열의 뒤에서 비교할 위치

    while i < j:
        # i위치에 있는 문자가 알파벳 문자가 아니면 뒤로 이동
        if s[i].isalpha() == False:
            i += 1
        # j위치에 있는 문자가 알파벳 문자가 아니면 앞으로 이동
        elif s[j].isalpha() == False:
            j -= 1
        # i와 j위치에 둘 다 알파벳 문자가 있으면 비교
        elif s[i].lower() != s[j].lower():
            return False
        else:
            i += 1
            j -= 1

    return True

print(palindrome("Wow")) # True
print(palindrome("Madam, I'm Adam.")) # True
print(palindrome("Madam, I am Adam.")) # False