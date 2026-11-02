# age classifier:

age = float(input("Enter the persons age: "))

if age <= 0:
    print ('invalid age!!')
elif age <= 1 :
    print ('infant')
elif age <= 3 :
    print ('toddler')
elif age <= 12 :
    print ('child')
elif age <= 19 :
    print ('teenager')
else :
    print ('adult')
