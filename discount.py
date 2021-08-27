top=int(input("enter the first amount"))
shirt=int(input("enter the second amount"))
discount=(top*1000)/100
if discount>=1000:
    print("discountable by 100")
    if discount<1000:
        print("discountable by 50")
    else:
        print("not % by 50")
else:
    print("not % by 100")


