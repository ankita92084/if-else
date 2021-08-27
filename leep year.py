year=int(input("enter the year"))
if year%4==0:
    print("this is leep year")
    if year%100==0:
        print("this is centurey")
        if year%400==0:
            print("leep year")
        else:
            print("not a year")
    else:
        print("this is not a centurey")
else:
    print("this is not a leep year")
    

    

