
def chris(a,b,name):
    c = a + b
    print(f'the value of a : {a}')
    print(f'the value of b : {b}')
    print(f'your name:{name}')
    return (f"the value: {c}")

chris()

chris(2,6)
chris(4,7)
chris(69,23,"christina")
#calling a function without repeating codes

#+++++++++++++++++++++++++++++++++++++++++++++++#
#pass arguements on functions#

# 1)default arguement

def math_add(a, b=10):
#b=10 is default 
# default value must be at the end and not first
    c = a + b
    print(f"print c: {c}")

math_add(2)

# 2) Keyword Argument
def hello(a,b):
    print(f"the value of a: {a}")
    print(f"the value of b: {b}")
    c = a//b
    print(f"the value of c: {c}")

hello(b = 1,a = 4)