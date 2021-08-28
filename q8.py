number=int(input("entee the number"))
if number%5==0:
    print("divisible by 5 ")
    if number%15==0:
        print("divisible by 15 ")
    else:
        print("not divisible by 15")
else:
    print("not divisible by 5  and 15")

