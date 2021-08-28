leter=1
leter2=10
water=int(input("enter the leter of water"))
if water<leter:
    print("water needs to be filled")
elif water>leter and water<leter2:
    print("no needs to be filled")
else:
    print("water is overflow")
