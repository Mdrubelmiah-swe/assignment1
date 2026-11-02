n = int (input("Enter an integer number:"))

a = 0
b = 1
count = 0

if n < 0 :
    print ("please enter the integer nunber: ")

else:
    print ("the fibonacci seriz is :", end=" ")

    while count < n :
        print (a, end= " ")

        c = a + b
        a = b
        b = c
        count += 1

