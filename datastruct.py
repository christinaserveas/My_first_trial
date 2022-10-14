#unmutable - tuple
#mutable -list set dictionary

from tkinter import Y


data_structure = "list,set,tuple,dictionary"

#LIST & Array methods

#append()	Adds an element at the end of the list
fruits = ['apple', 'banana', 'cherry']
fruits.append("orange")

#clear()	Removes all the elements from the list
fruits = ['apple', 'banana', 'cherry', 'orange']
fruits.clear()

#copy()	Returns a copy of the list
fruits = ['apple', 'banana', 'cherry', 'orange']
x = fruits.copy()

#count()	Returns the number of elements with the specified value
fruits = ['apple', 'banana', 'cherry']
y = fruits.count("cherry")
y
#extend()	Add the elements of a list (or any iterable), to the end of the current list
fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars)

#index()	Returns the index of the first element with the specified value
fruits = ['apple', 'banana', 'cherry'] #indexing starts from zero
z = fruits.index("cherry")
z

#insert()	Adds an element at the specified position
fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, "orange")
fruits

#pop()	Removes the element at the specified position
fruits = ['apple', 'banana', 'cherry']
fruits.pop(1)

#remove()	Removes the first item with the specified value
fruits = ['apple', 'banana', 'cherry']
fruits.remove("banana") #useful when we dont know the position of the element

#reverse()	Reverses the order of the list
fruits.reverse()
fruits.reverse()
fruits
#sort()	Sorts the list
elements = [4,6,3,8,2,7]
elements.sort()
elements

#SET FUNTIONS

#a set will never allow duplicates - no two same elements
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

#length of the set
thisset = {"apple", "banana", "cherry"}
print(len(thisset))

#Set Items - Data Types
'''Set items can be of any data type:
Example
String, int and boolean data types:'''

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

#A set can contain different data types:strings, integers and boolean values:

set4 = {"abc", 34, True, 40, "male"}

#for loops

thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

#checkout
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)

#Add an item to a set, using the add() method:

thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

#add new set to the present set
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

#adding non set value - list, tuple
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)

