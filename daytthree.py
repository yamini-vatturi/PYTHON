if True:
    print("valid")
else:
    print("invalid")
    
try:
    a=int(input("enter first number"))
    b=int(input("enter second number"))
    result=a+b
    print("sum",result)
except ValueError:
    print("Invalid input please enter a number")
finally:
    print("Excecution finished")
    
try:
    num=int(input("enter a number"))
    result=10/num
    print("result",result)
except ValueError:
    print("Invalid input please enter a number")
except ZeroDivisionError:
    print("cannot divide by zero")
finally:
    print("Excecution finished")

x=2+3j
print(x.real)
print(x.imag)
print(type(x))

def sum(a,b):
    return a+b
def diff(a,b):
    return a-b
def prod(a,b):
    return a*b
a,b=10,2
s=sum(a,b)
print(s)
d=diff(a,b)
print(d)
p=prod(a,b)
print(p)
