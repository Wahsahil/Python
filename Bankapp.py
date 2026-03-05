#Create a program that authenticate and verify from the data base the login system
from getpass import getpass
bank_data = {1001 : ['Sahil','sah',10000],
            1002 : ['ketan','keh',5000],
             1003 : ['Rahul','rah',6000]}
list(bank_data.keys())[-1]+1
def signup():
    user_name = input("Enter the Username : ")
    password = getpass("Enter the Password : ")
    lower = 0
    upper = 0
    special = 0
    digit = 0
    for i in password:
        if i.isdigit():
            digit+=1
        elif i.isupper():
            upper +=1
        elif i.islower():
            lower +=1
        elif not(i.isidentifier()):
            special +=1
    if lower>=1 and upper >=1 and digit >=1 and special>=1 and len(password)>=8:
        print("Initial amout of 2000 is required to open an account")
        choice = input("Enter your choice(y/n) : " ).lower()
        if choice == 'y':
            acc_no = list(bank_data.keys())[-1]+1
            balance = 2000
            bank_data.update({acc_no:[user_name,password,balance]})
            print("Account is Created. Your account no. is ",acc_no)
        else:
            print("Initial amount is required. Thankyou for giving your time..... ")
    else:
        print("Password is not Valid !!!!")
signup()

#Bank login
def login():
    acc_no = int(input("Enter Account no. : ")) 
    password=getpass("Enter you password : ")
    if acc_no in bank_data.keys() and password in bank_data[acc_no]:
        print("Welcome !")
        
        print("1 Credit ")
        print("2 Debit ")
        print("3 Change password !")
        print("4 Bank Balance") 
        print("5 Show Details") 
        print("6 Logout")
        choice = int(input("Press anyone choice : "))
        amount = bank_data[acc_no][2]
        if choice == 1:
            c_balance=int(input("Enter Deposite amount : "))
            bank_data[acc_no][2]=amount+c_balance
            print("...")
            print("Your tansaction is completed")
        elif choice ==2:
            d_balance =int(input("Enter debit amount : "))
            if d_balance <=bank_data[acc_no][2]:
                print("Please wait your transaction is waiting....")
                print(".")
                print("..")
                print("...")
                print("Your transaction is Complete.")
                bank_data[acc_no][2]=amount-d_balance
            else:
                print("Balance is insufficient...")
        elif choice==3:
            cur_pass = getpass("Enter your current passsword : ")
            if cur_pass in bank_data[acc_no]:
                new_pass = getpasss("Enter your new password : ")
                lower = 0
                upper =0
                special =0
                digit=0
                for i in new_pass:
                    if i.isdigit():
                        digit+=1
                    elif i.isupper:
                        upper+=1
                    elif i.islower:
                        lower+=1
                    elif not(i.isidentifier()):
                        special+=1
                if lower>=1 and upper>=1 and special>=1 and digit>=1 and len(new_pass)>=8:
                    bank_data[acc_no][1]=new_pass
                    print("Your password is Sucessfuly changed")
                else:
                    print("New Password is wrong!!!")
            else:
                print("Your Password is Wrong")
        elif choice==4:
            print("Balance : ",bank_data[acc_no][2])
        elif choice ==5:
            print("User name : ",bank_data[acc_no][0])
            print("Account number : ",acc_no)
            print("Balance : ",bank_data[acc_no][2])
        elif choice ==6:
            print("Thankyou !!")
        else:
            print("Invalid Choice............!!!!!")
    else:
        print("Invalid Account number or password !!!!")
login()