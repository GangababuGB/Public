#lambda 'argument of function' : 'expresson to be solved in this function and to be returned'
x=lambda a: a+10
print(x(5))

x=lambda a,b: a*b
print(x(5,6))

s=lambda x : x*x if(x>0) else 55
print(s(2))

s=lambda x : x*x if(x>0) else 55
print(s(0))

s=lambda x : x*x if(x>0) else None
print(s(6))
        


def fun(n):
    return lambda a:a*n#print(a,n,a*n)
mydoubler=fun(2)
print(mydoubler(11))

def my_function(*kids):#when don't know number of arguments
    print("The youngest child is " + kids[2])
    print(kids)
my_function("a","b","c","d","e")

def my_function(**kid):#don't know number of keywords passed
    print("His last name is "+kid["lname"])
my_function(fname="ansh",lname="raj")

import math as mt
print(dir(mt)) #print all methods inside math module

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

