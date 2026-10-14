
# find the greatest number from the given input
a = int(input(" enter a first no"))
b = int(input(" enter a second no"))
c = int(input(" enter a third no"))
if a>b and a>c:
    print(" a is greater no")
elif b>a and b>c:
    print(" b is greater no")
else: 
     print("c is greater no") 

# Find the number is +ve, -ve or zero
d = int(input(" enter a number ="))
if d>0:
    print(" number is positive")
elif d<0:
    print(" number is negative")
else:
    print(" number is zero")

# given the total count of the input no
# if given is 5 it will be 15
n = int(input(" enter a number"))
total = 0
for i in range(1,n+1):
  total = i + total
print(total)

# Find the even numbers from the given list
numbers =[3, 8, 10, 5, 7, 12]
count = 0
for i in numbers: 
    if i% 2 ==0:
        count+=1
print(count)

# find the highest values from the list
values =[12, 4, 25, 9, 18]    
highest = values[0]
for i in values:
    if i > highest:
     highest = i
print(highest)

# reverse the name 
name =input("enter a name=")
print(name[::-1])

# palindrome
word = input(" enter a word=")
rev = word[::-1]
if word == rev:
    print("it is palindrome")
else:
    print("it is not a palindrome")

# Find the lowest value of the given list
numbers =[14,6,23,2,11] 
small = numbers[0]
for i in numbers:
    if i< small:
        small = i
print(small) 

# find the number of vowels of the given word
word =input("enter a word=")
count = 0
for i in word:
    if i in "aeiou":
        count+=1
print(count)        


     




