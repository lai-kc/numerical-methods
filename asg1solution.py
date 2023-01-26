#########question 1###########
###############################
import scipy.special as sc
import numpy as np
import matplotlib.pyplot as pt

#define rician function
def rician(x,u,s):
    return x/s**2*np.exp(-(x**2+u**2)/2*s**2)*sc.iv(0,(x*u/s**2))

#define 1st derivative of rician function by central difference method
def f(x):
    return (rician(x+h,u,s)-rician(x-h,u,s))/2*h

#initialize all variables
s=1                         #sigma=1, see rician
peak=[]                     #empty array, then append peak found into it
test=np.linspace(0,10,100)  #find peak in ragen of value v=[0,10]

#looping from range [0,10]
for u in test:
    print(u)
    n=0
    a=0.5
    b=15
    err=1
    root=(a+b)/2
    err=abs((a-b)/2)
    h=0.01
#for each test value run bisection method
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
        #print(n,'    ',a,'    ',b,'    ',err)
    print('final=',root)
    peak.append(root)

pt.plot(test,peak,test,test)    #plotting 2 curve
#########question 1 end#############

#######question 2############
#############################
#for 2(a) 1d case, change 'n' value from 0.1,0.5,1,5,10
import scipy.special as sc
x=np.linspace(-6,6,1000)
n=0.1
a=2**0.5*(x+n**0.5)
b=2**0.5*(x-n**0.5)
s1,c1=sc.fresnel(a)
s2,c2=sc.fresnel(b)
s,c=s1-s2,c1-c2
f=0.5*(s**2+c**2)
pt.plot(x,f)


#for 2(b) 2d case
nx=10
ny=10
x=np.linspace(-6,6,1000)
y=np.linspace(-6,6,1000)
X,Y=np.meshgrid(x,y)
xs=sc.fresnel(2**0.5*(X+nx**0.5))[1]*1j+sc.fresnel(2**0.5*(X+nx**0.5))[0]-sc.fresnel(2**0.5*(X-nx**0.5))[1]*1j-sc.fresnel(2**0.5*(X-nx**0.5))[0]
ys=sc.fresnel(2**0.5*(Y+ny**0.5))[1]*1j+sc.fresnel(2**0.5*(Y+ny**0.5))[0]-sc.fresnel(2**0.5*(Y-ny**0.5))[1]*1j-sc.fresnel(2**0.5*(Y-ny**0.5))[0]
z=abs(xs*ys)**2
pt.imshow(0.25*abs(z)**2)

########question 2 end###########

########question 3###############
#################################
import numpy as np

m=np.array([[2,-1],[-1,2]])
print(np.linalg.eig(m))

