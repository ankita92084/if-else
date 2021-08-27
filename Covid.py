girl=12
vacinated=input("are you vacinated or not?: /yes /no   ")
if vacinated=="yes":
    report=input("do you have report:/yes / no")
    if report=="yes":
        print("no qurentine")
        room=int(input("allot the room"))
        if room==408:
            print("let me check there bed is avilable or not")
            bed=int(input("enter the bed quantity"))
            if bed>girl:
                print("this room is full you can go to 420")
                room=int(input("allot the room"))
                if room==420:
                    print("checking")
                    bed=int(input("enter the bed quantity"))
                    if bed<girl:
                        print(girl-bed," seats are avilable , you can go to this room")
                    else:
                        print("you cannot go to this rrom")
                else:
                    print("this room is not in ng")
            else:
                print("beds are not avilable")
        else:
            print("not allowed")
    else:
        print("quarentine ")
else:
    print("qurentine for 3 days")

    
    