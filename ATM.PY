print("welcome to union bank","insert your card")
card=(input("choose card type:/debit card/credit card/"))
if card=="debit card" or card=="credit card":
    print("yes")
    language=(input("choose your language:/english/hindi/marathi/"))
    if language=="english" or "hindi":
        print("please wait")
        option=(input("select your option:/withdrwal/"))
        if option=="withdrwal":
            print("next step")
            pin=int(input("enter your pin"))
            if  pin<=9999:
                print("4 digit pin matched")
                amount= int(input("enter your amount"))
                if amount>500 and amount<=10000:
                    print("please wait your transaction is being proceed")
                    reciept=input("would you like to take recipet?:/yes/no/")
                    if reciept=="yes" or "no":
                        print("thnkyou for visiting union bank atm")
                        balance=int(input("check your balance"))
                        if balance<=9999:
                            print(9999-amount,"balance")
                        
                        else:
                            print("there is no balance")

                    else:
                        print("please  select you would like to take recipt or not")               
                    
                else:
                    print("please enter amount between 500 to 10000")
            else:
                print("please enter correct pin")
        else:
            print("please selct available option")
    else:
        print("please select available language")
else:
    print("please select any one type ")








