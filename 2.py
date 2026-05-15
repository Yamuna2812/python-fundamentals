def is_armstrong(num):
    power = len(str(num))
    total = 0
    temp = num

    while temp > 0:
        digit = temp % 10
        total += digit ** power
        temp //= 10

    return total == num


start = int(input("Enter start: "))
end = int(input("Enter end: "))

for i in range(start, end + 1):
    if is_armstrong(i):
        print(i)
