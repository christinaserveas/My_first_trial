
#practicing while function
#it runs until the condition becomes false
from tkinter import Y


i = 20
while i <= 100:
    print(f"the value of is is {i}")
    i += 20

i = 100
while i > 10:
    print(f"the value of i{i}")
    i-=1



#for loop
#Python for loops are used to loop through an iterable object (like a list, tuple, set, etc.) and perform the same action for each entry.

my_list = {"meena","kavya","priya","deepa"}
for name in my_list:
    print(name)

for each_letter in "Christina":
    print(f"The letters are:{each_letter}")


#nested loop function

traveling = input("yes or no")
while traveling == "yes":
    num = int(input("number of people traveling:" ))
    for num in range (1, num+1):
        name = input("name = ")
        gender = input("male or female:")
        print (name)
        print (gender)
    break



#find even or odd
numbers = [1,2,3,4,5,6,7,8,9,10]
for i in numbers:
    if i % 2 == 0:
        print(f"value of i is even {i}")
    else:
        print(f"the value of i is odd {i}")



#find the given input even or odd
numbers = int(input())
if  numbers %2==0:
        print(f" The number {numbers} is even")

if numbers %2 !=0:
        print(f"The number {numbers} is odd")




numbers = 3
if  numbers %2 != 0:
        print(f" The number {numbers} is Weird")

if numbers %2 ==0:
     if numbers in range[2,5]:
        print(f"The number {numbers} is Not Weird")
     elif numbers in range [6,20]:
        print(f"The number {numbers} is Weird")
     else:
        print (f"the number{numbers} is Not Weird") 




#range(start,stop,step/skip)
list(range(1,20,2))
list(range(1,20,1))

for i in (list(range (0,10))):
    print(f"{i}")
    for j in (list(range(11,20))):
        print(f"{j}")



nums = [1,2,3,4,5,6,7,8]
# basic for and while and learning that else will be printed no matter what
for i in nums:
    print(i)
else:
    print("chris")

j = 3
while j <=10:
    print(j)
    j=j+2
else:
    print('chris')




#break continue assert pass

#pass function, when the value is not matching the contition given it passes to the next variable in the list
i = range(1,20)
for i in range(1,20):
    if i <=20:
        if i % 2 ==0:
            print(f"even:{i}")
        else:
            pass #continue to loop
            print(f" continuing to loop as {i} is not even")
    else:
        print(i)
#pass
i = range(1,20)
for i in range(1,20):
    if i <=20:
        if i % 2 ==0:
            print(f"even:{i}")
        else:
            pass #continue to loop
            
    else:
        print(i)
#break 
#comparing 2 ranges to learn break (3,21,3) and (3,21)
i = range(1,20)
for i in range(3,21,3):
    if i <=20:
        if i % 3 ==0:
            print(f"multiple of 3 :{i}")
        else:
            break #continue to loop
    else:
        print(i)
 
 i = range(1,20)
for i in range(3,21):
    if i <=20:
        if i % 3 ==0:
            print(f"multiple of 3 :{i}")
        else:
            break # does not continue to loop or skin and run, it stops when it does not match the condition
    else:
        print(i)

#continue
i = range(1,20)
for i in range(3,21):
    if i <=20:
        if i % 3 ==0:
            print(f"multiple of 3 :{i}")
        else:
            continue 
 #"the function continues the loop no matter what the condition is"
    else:
        print(i)

name = "samuuel"
''.join(sorted(set(name), key=name.index))

n = int(input())
if (n%2)==0 and n in range(2,5):
  print("Not Weird")
if (n%2)==0 and n in range(6,20):
  print("Weird")
if (n%2)==0 and n > 20:
  print("Not Weird")
if (n%2) !=0:
  print("Weird")

  n = int(input())
if n % 2 == 1:
    print("Weird")
elif n % 2 == 0 and 2 <= n <= 5:
    print("Not Weird")
elif n % 2 == 0 and 6 <= n <= 20:
    print("Weird")
else:
    print("Not Weird")