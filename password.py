password = "123"

attempts = 0

while attempts < 3 :
    user_password = input("Enter the password: ")

    if user_password == password :
        print ("Login successful.")
        break
    else :
        attempts += 1
        print ("incorrect password: ")

        if attempts == 3 :
            print ("Account locked")
