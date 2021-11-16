password=input("enter the password ")
if password>="a" and  password<="Z" or password>="A" and password<="z":
    print("next")
    password1=int(input("enter number "))
    if password1>=1 and password1<=100000:
        print("next")
        password2=input("enter ")
        if password2=="#" or "$" or "@":
            print("next : ")
            sum=password+str(password1)+password2
            if sum==sum:
                print(sum)
                print("password is valid")
            else:
                print("invalid")
        else:
            print("please enter speacial charecter ")
    else:
        print("please enter only numerci ")
else:
    print("enter only alphabet here ")