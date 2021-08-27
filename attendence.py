total=int(input("Enter the total number of classes held"))
attended=int(input("Enter the number of classes attended"))
percent=(attended*100)/total
if percent>=75:
    print("your attendance is",percent,"%","you are allowed to sit for the examination")
    if percent<75:
        print("your attendence is ", percent,"%","you are not allowed to sit in examination")
    else:
        print("sorry you can try next semester")
else:
    print("all the best for exam")
    
    

