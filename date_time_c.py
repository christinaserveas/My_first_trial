from datetime import datetime, date
datetime.today()
datetime.today().day
datetime.today().month
datetime.today().year
datetime.now()
datetime.now().hour
datetime.now().minute
datetime.now().second

datetime.today().strftime('%d/%B/%y')
datetime.today().strftime("%D")
datetime.today().strftime('%d/%b/%Y')
datetime.today().strftime('%d/%m/%y')


#print & return

def my_add(a,b):
    c = a+b
    print(c)
x = my_add(6,9)
print(x)#gives none and does not print the defined func

# hence we should use return
def addmine(a,b):
    c = a+b
    return c #returns remembers and gives the values back outside the func when called

x = addmine(12,4)
print (x)