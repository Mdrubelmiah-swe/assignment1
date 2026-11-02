num = int(input("Enter a number :"))

num = abs (num)

total = 0
digit = 0

while num > 0  :
     
    total += digit % 10
    digit += 1
    num //= 10
print("total digit is:", digit)
print(" total sum of digit is:", total)