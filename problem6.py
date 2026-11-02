a = float(input("Enter the first number: "))
op = input("Enter the operator :(+, -, *, /)")
b = float(input("Enter the second number: "))

if op == "+" :
    print("result =", a + b)
elif op == "-" :
    print("result =", a - b)
elif op == "*" :
    print("result = ",a * b)
elif op == "/" :
    if b != 0 :
        print("result =", a / b)
    else :
        print("cant devide by 0")
else :
    print("invalid operator")