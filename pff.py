'''city = ['BENGALURU', 'MYSURU', 'HUBBALLI', 'MANGALURU']
num = [85, 90, 78,66]
district = {}
for i in range(len(city)):
    district[city[i]] = num [i]
print(district)'''

#list comprehension
'''values = [1,2,5,4,7,8,96,23,7]
new_values = [item+2 for item in values]
print(new_values)

#write a pgm to print 1 10 square numbers without taken a input from user and manulally
u =int(input("range "))
sq = [x for x in range (u+1)]
new_values = [item**2 for item in sq if item%2==0]
print(f"this numbers are divisible by 2 {new_values}")

#find how many char is there in the word
city = ['BENGALURU', 'MYSURU', 'HUBBALLI', 'MANGALURU']
new={x:len(x) for x in city}
print(new)'''


