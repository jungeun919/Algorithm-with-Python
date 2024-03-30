n = int(input())

win = ["SK", "CY", "SK", "SK"]

if n <= 4:
    print(win[n - 1])
else:
    for i in range(4, n):
        if win[i - 1] == "CY" or win[i - 3] == "CY" or win[i - 4] == "CY":
            win.append("SK")
        else:
            win.append("CY")
    print(win[n - 1])
