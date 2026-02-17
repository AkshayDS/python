fru=[]
f1=input("Enter a fruits ")
fru.append(f1)
f2 = input("Enter another fruit ")
fru.append(f2) 
f3 = input("Enter third fruit ")
fru.append(f3)
f4 = input("Enter 4th fruit ")
fru.append(f4)
f5 = input("Enter 5 fruit ")
fru.append(f5)
f6 = input("Enter 6 fruit ")
fru.append(f6)
f7 = input("Enter 7 fruit ")
fru.append(f7)
print(fru)

#short cut by using for loop
fru = []

# Loop 7 times to get fruit names
for i in range(1, 8):
    fruit = input(f"Enter fruit {i}: ")
    fru.append(fruit)

print("Your fruits list:", fru)