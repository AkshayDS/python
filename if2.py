'''a=int(input("Enter a sub 1 marks out of 100 = "))
b=int(input("Enter a sub 2 marks out of 100 = "))
c=int(input("Enter a sub 3 marks out of 100 = "))
sum = ((a+b+c)/3)
total = 40
print(f"{sum}%")
if(sum>=total and a>=33 and b>=33 and c>=33):
    print("He is passed")
elif(sum<total):
    print(f"He is failed because the total marks is {sum}% less than 40%  ")
elif(a<=33):
    print(f"He is failed because the sub 1 marks is {a}% less than 33%  ")
elif(b<=33):
    print(f"He is failed because the sub 2 marks is {b}% less than 33% ")
elif(c<=33):
    print(f"He is failed  because the sub 3 marks is {c}% less than 33% ")

    
    #this is clean code

sub1 = int(input("Enter subject 1 marks out of 100: "))
sub2 = int(input("Enter subject 2 marks out of 100: "))
sub3 = int(input("Enter subject 3 marks out of 100: "))
average_marks = (sub1 + sub2 + sub3) / 3
print(f"Total Percentage: {average_marks:.2f}%")


if sub1 < 33:
    print(f"Failed: Subject 1 marks are {sub1}, which is less than 33%")
elif sub2 < 33:
    print(f"Failed: Subject 2 marks are {sub2}, which is less than 33%")
elif sub3 < 33:
    print(f"Failed: Subject 3 marks are {sub3}, which is less than 33%")

elif average_marks < 40:
    print(f"Failed: Total percentage {average_marks:.2f}% is less than 40%")
else:
    print("The student has passed ✅")'''

#this is advance code
marks = []
for i in range(1, 4):
    m = int(input(f"Enter subject {i} marks out of 100: "))
    marks.append(m)

average = sum(marks) / len(marks)
print(f"Total Percentage: {average:.2f}%")

# Check subject-wise
for idx, m in enumerate(marks, start=1):
    if m < 33:
        print(f"Failed: Subject {idx} marks are {m}, less than 33")
        break
else:
    if average < 40:
        print(f"Failed: Total percentage {average:.2f}% is less than 40%")
    else:
        print("The student has passed ✅")




 