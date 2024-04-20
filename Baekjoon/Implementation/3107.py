addr = input()
addr = addr.split(":")

full_addr = []
double_colon = False

for check in addr:
    if check == '' and double_colon == False:
        for _ in range(8 - len(addr) + 1):
            full_addr.append("0000")
        double_colon = True
    else:
        four_digit = "0" * (4 - len(check)) + check
        full_addr.append(four_digit)

print(':'.join(full_addr))
