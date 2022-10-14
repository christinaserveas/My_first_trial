#indexing & splicing

student_list = []
for i in range(8):
    student_name = input ("please enter your name: ")
    student_list.append(student_name)

student_list
student_list.index('7')

from numpy.random import randint, choice

list1 = choice(randint(0,500,20))
list2 = randint(0,2,list1).tolist()
print(list2)
list2[-1]
list2[-2]
list2[5:14]

list3 = ["han","can", "man","tan","van"]
list3[1:3+1]
list3[-3:-1]
list3[:]

#sets cannot have indexing 