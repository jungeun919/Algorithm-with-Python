# s->t <-> t->s
# 뒤에 A 추가 <-> 뒤에서 A 제거
# 뒤에 B 추가 후 뒤집기 <-> 앞에서 B 제거하고 뒤집기

s = list(input())
t = list(input())

res = 0

def dfs(t):
    global res

    if t == s:
        res = 1
        return

    if len(t) == 0:
        return

    if t[-1] == 'A':
        dfs(t[:-1])

    if t[0] == 'B':
        dfs(t[1:][::-1])

dfs(t)
print(res)
