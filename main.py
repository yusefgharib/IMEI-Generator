from random import randint


def generate_imei(digits):
    luhn_sum = 0
    imei_digits = []
    for i in range(14):
        try:
            digit = digits[i]
        except IndexError:
            digit = str(randint(0, 9))
        imei_digits.append(digit)
        if i % 2 != 0:
            digit = str((int(digit) * 2))
        for num in digit:
            luhn_sum = luhn_sum + int(num)
    remainder = luhn_sum % 10
    check_digit = 0 if remainder == 0 else 10 - remainder
    return "".join(imei_digits) + str(check_digit)


amount = int(input("Enter the amount of IMEIs you want to generate\n"))
tac = input("\nEnter the TAC + any digits you want to specify\n")
print()
for i in range(amount):
    imei = generate_imei(tac)
    print(f"IMEI {i + 1}: {imei}")
