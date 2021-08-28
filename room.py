Ng=150
girls=int(input("enter the no. of girls"))
if girls==Ng:
    print("fine")
elif girls>Ng:
    print(Ng-girls,"girls are extra")
elif girls<Ng:
    print(Ng-girls,"girls wants")
else:
    print("extra girls")
