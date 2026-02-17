'''student = {"name": "Rahul", "age": 20}
print(student.get("age"))
print(student.get("grade"))'''

fruit = {}
fkey=input("Enter the fruit ")
fvalue=input("Enter the fruit ")
fruit.update({fkey:fvalue})
print(fruit)
print(fruit.get(fkey))