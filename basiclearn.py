
numbers = [1,2,3,4,5,6,7,8]
highest = numbers[0]
for i in numbers:
   if i > highest: 
      highest = i
print(highest)

word = input("enter the name =")
if word == word[:: -1]:
   print("it is a palindrome")
else:
   print("it is not a palindrome") 


a = int(input("enter a first no =")) 
b = int(input("enter a second no= "))
sum = a + b
print(sum) 
 


a = int(input("enter a first no =")) 
b = int(input("enter a second no= "))
sub = a - b
print("sub =",sub)  



x = int(input("enter a first no ="))
y = int(input("enter a second no ="))
sum = x+y
sub = x-y
mul = x*y
div = x/y
print("sum =",sum)
print("sub =",sub)
print("mul =",mul)
print("div =",div)


c = int(input("enter a first no="))
d = int(input("enter a second no="))
temp = c
c = d
d = temp
print("c =", c)
print("d =", d)

f = int(input("enter a number="))
d = f % 2 ==0
print("even" if d else "odd")





