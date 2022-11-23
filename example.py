# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 11:13:59 2022

@author: User
"""
#to define factorial
def fact(n):
    a=1
    for i in range (2,n+1):
       a=a*i 
    return a
#define term n for arcsin
def t(x,n):
    return (fact(2*n))/(2**(2*n))/(fact(n)**2)/(2*n+1)*(x**(2*n+1))
#calculate pi using arcsin for for 30 terms
x=0.5
a=0
for n in range (0,30):
    a=a+t(x,n)
    print(6*a)
#calc pi with precision 0.001
a=0 
x=0.5  
dif=1  
n=0  
while dif > 0.001:
    b=a+t(x,n)
    dif=6*abs(b-a)
    print(n,'    ',6*b,'    ', dif)
    n=n+1
    a=b
 
    
#define term for arctan
def t(x,n):
    return ((-1)**n)*(x**(2*n+1))/(2*n+1)
a=0 
x=1  
dif=1  
n=0  
while dif > 0.001:
    b=a+t(x,n)
    dif=4*abs(b-a)
    print(n,'    ',4*b,'    ', dif)
    n=n+1
    a=b    
    
    
    
    
#demo looping#   
x=list(range(1,11))
for i in x:
    if i>7:
        print(i,'is larger than 7')

x=list(range(1,11))
for i in x:
    if i>7:
        break
    print(i)

x=list(range(1,11))
for i in x:
    if i>7:
        print(i,'is larger than 7')
    else:
        print(i,'is <= 7')
        
x=list(range(1,11))
for i in x:
    if i>7:
        break
        print(i,'is larger than 7')
    else:
        print(i,'is <= 7')



x=list(range(10,21))
for i in x:
    if i%2==0:
        print('2 is divider of',i)
    if i%3==0:
        print('3 is divider of',i)
    else:
        print('2 & 3 is not divider of',i)

     
x=list(range(10,21))
for i in x:
    if i%2==0:
        print('2 is divider of',i)
    elif i%3==0:
        print('3 is divider of',i)
    else:
        print('2 & 3 is not divider of',i)
##



def fact(n):
    a=1
    for i in range (1,n+1):
        a=a*i
    return a

def t(x,n):
    return ((-1)**n)*x**(2*n+1)/fact(2*n+1)


#we want to find sin(x),x=1,first 4 therm
x=1
a=0
for i in range (4):
    a=a+t(x,i)
return a

#find sin(x) to precision of  0.00001
x=10
a=0
dif=1
n=0
while dif>0.00001:
    b=a
    a=a+t(x,n)
    print(n,'    ',a)
    n=n+1
    dif=abs(b-a)

#def sin(x) for first 4 term
def sin(x):
    a=0
    for i in range (4):
        a=a+t(x,i)
    return a


#bisection method of f(x)=2-e^x interval [0,1]
def f(x,h):
    return (rician(x+h)-rician(x-h))/2*h

n=0
a=0.5
b=2
err=1
root=(a+b)/2
err=abs((a-b)/2)
while err>0.001:
    c=(a+b)/2
    testb=f(c)*f(b)
    testa=f(c)*f(a)
    if testb<0:
        a=c
        root=(a+b)/2
        err=abs((a-b)/2)
    elif testa<0:
        b=c
        root=(a+b)/2
        err=abs((a-b)/2)
    else:
        print('error')
        break
    n=n+1
    print(n,'    ',a,'    ',b,'    ',err)
print('final=',root)   

#newton method
def f(x):
    return x-0.9*np.sin(x)-np.pi/2
def f1(x):
    return 1-0.9*np.cos(x)

n=0
x=2
dif=1
while dif>0.001:
    print(n,'   ',x)
    a=x-f(x)/f1(x)
    dif=abs(a-x)
    x=a
    n=n+1

#secant method
def f(x):
    return 2-np.exp(x)

n=0
x0=0.5
x1=1
dif=1
while dif>0.00000001:
    a=x1-f(x1)*(x1-x0)/(f(x1)-f(x0))
    n=n+1
    print(n,'    ',a)
    x0=x1
    x1=a
    dif=abs(x1-x0)
    

######DK method for polynomial#######
def p(x):
    return x**6-x-1

def t(x):
    for i in range (len(x)):
        x[i]=x[i]-p(x[i])/(np.prod(x[i]-np.delete(x,i)))
    return x

x=np.array([1,-1,1j,-1j])
t(x)

###householder transform, Qx=-|x|e1,w=x+|x|e1###
x=np.array([1,2,3]).reshape(3,1)
def ht(x):
    g=1/((x.T@x)+(x.T@x)**0.5*x[0])
    return np.identity(x.shape[0])-g*(x+np.linalg.norm(x)*np.array([1,0,0]).reshape(x.shape[0],1))@(x+np.linalg.norm(x)*np.array([1,0,0]).reshape(x.shape[0],1)).T


####Rayleigh quotient eigenvalue######
for i in range (10):
    y=m@z
    l=(z.T@y)/np.sqrt(z.T@z)
    z=y/np.sqrt(y.T@y)
    print(i,l)

###QR method###
m=np.array([4,1,0,1,4,1,0,1,4]).reshape((3,3))
for i in range (100):
    q,r=np.linalg.qr(m)
    m=r@q
    print(m)
import numpy as np

l,v=np.linalg.eig(m)
np.linalg.



###rician curve###
import scipy.special as sc
def rician(x,u,s):
    return x/s**2*np.exp(-(x**2+u**2)/2*s**2)*sc.iv(0,(x*u/s**2))

def f(x):
    return (rician(x+h,u,s)-rician(x-h,u,s))/2*h

s=1
peak=[]
test=np.linspace(0,10,100)

for u in test:
    print(u)
    n=0
    a=0.5
    b=15
    err=1
    root=(a+b)/2
    err=abs((a-b)/2)
    h=0.1
    while err>0.0001:
        c=(a+b)/2
        testb=f(c)*f(b)
        testa=f(c)*f(a)
        if testb<0:
            a=c
            root=(a+b)/2
            err=abs((a-b)/2)
        elif testa<0:
            b=c
            root=(a+b)/2
            err=abs((a-b)/2)
        else:
            print('error')
            break
        n=n+1
        h=h/2
        print(n,'    ',a,'    ',b,'    ',err)
    print('final=',root)
    peak.append(root)












