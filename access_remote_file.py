from re import X
from statistics import mode


f = open('Pinky_1.txt','w')
with open('Pinky_1.txt', 'w') as f:f.write( "hello everyone, the world is beautiful, enjoy its goodness")


#with open('Pinky_1.txt', 'r') as f: f.read()
with open('pinky_1.txt', 'r') as f: x = f.read() 
print(x)
