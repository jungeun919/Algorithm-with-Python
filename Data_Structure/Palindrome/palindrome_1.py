# 주어진 문장이 회문인지 아닌지 찾기 (큐와 스택의 특징을 이용)

def palindrome(s):
    qu = []
    st = []

    # 1. 알파벳 문자를 각각 큐와 스택에 넣음
    for x in s:
        # 해당 문자가 알파벳이면 큐와 스택에 각각 그 문자를 추가
        if x.isalpha():
            qu.append(x.lower())
            st.append(x.lower())

    # 2. 큐와 스택에 있는 문자를 꺼내면서 비교
    while qu:
        if qu.pop(0) != st.pop():
            return False

    return True

print(palindrome("Wow")) # True
print(palindrome("Madam, I'm Adam.")) # True
print(palindrome("Madam, I am Adam.")) # False