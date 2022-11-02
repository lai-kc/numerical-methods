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
