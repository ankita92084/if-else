print("GMAIL LOGIN")
user_id=(input("enter your mail id or user id"))
if user_id in "ankita92084@gmail.com":
    print("mail id ")
    password=int(input("enter the password"))
    if password<999999999:
        print("forgot password")
        mobile=int(input("enter your mobile number"))
        if mobile<9999999999:
            print("your mobile number has beeen verified")
            new_password=int(input("make new password"))
            if new_password<1000000:
                print("generated suceeessfully")
            else:
                print("not valid")
        else:
            print("enter registered mobile number")
    else:
        print("password does not matched")
else:
    print("enter registered mail id")

