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
    
    
