import math as m
def add(a,b):
    print (a+b)
def multi(a,b):
    print(a*b)
def sub(a,b):
    print(a-b)
def div(a,b):
    print (a/b)
def sine(n):
    print(m.sin(n))
def cosine(n):
    print(m.cos(n))
def tangent(n):
    print(m.tan(n))
def Fac(n):
    print(m.factorial(n))
def Power(a,b):
    print(m.pow(a,b))
def Sqrt(n):
    print (m.sqrt(n))
def Log(n):
    print(m.log(n))
print("\t\t\t\tWelcome To The Scientific Calculator")
print("\t Operation are as Follow:")
print(" \t+ for Addition ")
print(" \t- for Subtraction")
print(" \t* for Multiplication ")
print(" \t/ for Division ")
print("\tsin for Sine of any number")
print("\tcos for cosine of any number")
print("\ttan for Tangent of any number")
print("\t! for Factorial of any number")
print("\t^ for Power of any number")
print("\tsqrt for Square Root of any number")
print("\tlog for the log of any no. with Base 10")
res=str(input("Do You Want To Perform Operation "))
res.lower
if(res=="yes"):
    op=str(input("Your Option is :"))
    if (op=="+" or op=="-" or op=='*' or op=='/' or op=='^' ):
        
        a=int(input("Enter The First Number"))
        b=int(input("Enter The Second Number"))
    else:
        n=int(input("Enter The Number"))
else:
    exit()

if (op=="+"):
    add(a,b)
if (op=="-"):
    sub(a,b)
if (op=="*"):
    multi(a,b)
if (op=="/"):
    div(a,b)
if (op=="^"):
    Power(a,b)
if (op=="sin"):
    sine(n)
if (op=="cos"):
    cosine(n)
if (op=="tan"):
    tangent(n)
if (op=="!"):
    Fac(n)
if (op=="log"):
    Log(n)
if(op=="sqrt"):
    Sqrt(n)
