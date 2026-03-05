def val():
    username = input("Enter the Username: ")
    if username == "Sahil":
        password = input("Enter the Password: ")
        if password == "1000":
            print("Access Granted")
        else:
            print("Wrong Password")
    else:
        print("Wrong Username")
val()