spam1 =("Make a lot of money")
spam2 =("buy now")
spam3 =("Subscribe this")
spam4 =("click  this")
comment=input("Enter a comment ")
print(comment)
if (spam1 in comment) or (spam2 in comment) or (spam3 in comment) or (spam4 in comment):
        print("This is a  spam  comment")
else:
        print("there is spam comment")


   
