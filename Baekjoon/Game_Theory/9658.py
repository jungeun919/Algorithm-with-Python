n = int(input())

turn = ["SK", "CY", "SK", "CY"]

for i in range(4, n):
    if turn[i - 1] == "CY" and turn[i - 3] == "CY" and turn[i - 4] == "CY":
        turn.append("SK")
    else:
        turn.append("CY")

if turn[n - 1] == "SK":
    win = "CY"
else:
    win = "SK"

print(win)
