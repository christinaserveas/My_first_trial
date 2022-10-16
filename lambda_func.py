from pickle import TRUE


x = lambda a : a + 10
print(x(5))

x = lambda a, b : a * b
print(x(5, 6))

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

def vowels(variable):
    letters = ["a","e","i","o","u"]
    if variable in letters:
        return True
    else:
        return False

sequence = ["a","b","c","d","e"]
list(filter(vowels,sequence)) 

from time import perf_counter
start = perf_counter()
list(filter(vowels,sequence)) 
stop = perf_counter()
print(f"the program ends in:{(start-stop)}")