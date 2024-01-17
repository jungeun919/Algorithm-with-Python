time = int(input())

if time % 10 != 0:
    print(-1)
else:
    for i in [300, 60, 10]:
        print(time // i, end=" ")
        time = time % i
