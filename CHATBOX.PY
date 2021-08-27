print("WHTSAPP CHAT")
greeting=input("send whish")
if greeting in "good morning":
    print("gd morning")
    chat1=input("start chat")
    if chat1 in "hii":
        print("hello")
        chat2=input("ask for health")
        if chat2 in "how are your":
            print("i am good thankyou for asking ND HOW R U?")
            reply=input("give reply")
            if reply in "i m also good":
                print("good")
            else:
                print("i am not good")
        else:
            print("how r you doing")
    else:
        print("hey")
else:
    print("it was great talking with you")