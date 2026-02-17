Name=input("Enter your name ")
Age=int(input("Enyter your age "))

if(Age%2==0):
    print("Even number")
else:
    print("Odd")

if(Age>=18):
    print(f"Hi {Name} your age is {Age} so you can access this ")
elif(Age<=0):
    print("Invalid Age , please enter vaild age ")
else:
    print(f"Hi {Name} your age is {Age} so you can't access this ")
print("Thank You...")
    