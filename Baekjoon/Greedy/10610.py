n = list(input())

if "0" not in n:
    print(-1)
else:
    total = 0 # 각 자릿수의 합
    for i in n:
        total += int(i)
    
    if total % 3 != 0:
        print(-1)
    else:
        n.sort(reverse=True)
        print("".join(n))
