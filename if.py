a = int(input("Enter a first number "))
b = int(input("Enter a second number "))
c = int(input("Enter a third number "))
d = int(input("Enter a fourth number "))
print(a,b,c,d)
if(a>b and a>c and a>d):
    print(f"{a} is greater")
if(b>a and b>c and b>d):
    print(f"{b} is greater")
if(c>a and c>b and c>d):
    print(f"{c} is greater")
else:
    print(f"{d} is the greatest number")


