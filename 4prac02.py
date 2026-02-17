'''Marks=[]
s1=int(input("Enter a 1st student "))
Marks.append(s1)
s2=int(input("Enter a 2nd student "))
Marks.append(s2)
s3=int(input("Enter a 3rd student ")) 
Marks.append(s3)
s4=int(input("Enter a 4th student "))
Marks.append(s4)
s5=int(input("Enter a 5th student "))
Marks.append(s5)
s6=int(input("Enter a 6th student "))
Marks.append(s6)
s7=int(input("Enter a 7th student "))
Marks.append(s7)
print(sorted(Marks))'''
marks = []

# Loop 7 times to get fruit names
for i in range(1, 8):
    fruit = int(input(f"Enter the marks here {i}: "))
    marks.append(fruit)

print("Your Marks list:", sorted(marks))

t=(tuple(marks))
print(t)
