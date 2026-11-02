#Armstrong Number Checker:

num = int(input("Enter a Number :"))

if num < 0 :
    print ("The number is invalid")
else:
    digit = str(num)
    power = len(digit)
    total = 0

    for digits in digit:
        total += int(digits) ** power

    if total == num:
        print ("The Number is Armstrong :")

    else :
        print ("The Number is not Armstrong :")


