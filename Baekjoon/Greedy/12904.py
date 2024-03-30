# s->t <-> t->s
# 뒤에 A 추가 <-> 뒤에서 A 제거
# 뒤집고 뒤에 B 추가 <-> 뒤에서 B 제거하고 뒤집기

s = list(input())
t = list(input())

res = 0
while t:
    if t[-1] == 'A':
        t.pop()
    elif t[-1] == 'B':
        t.pop()
        t.reverse()
    
    if t == s:
        res = 1
        break

print(res)
