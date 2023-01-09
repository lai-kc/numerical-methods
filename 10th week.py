import numpy as np

###Gauss newton lsq
def function(a,x):              
    return np.exp((-(x[0]-a[0])**2-(x[1]-a[1])**2)/2)

def J(f,a,x):                  
    d=0.000001                        
    b=[]
    for i in range (len(a)):
        ap1=a.copy()
        ap2=a.copy()
        ap1[i]=ap1[i]+d
        ap2[i]=ap2[i]-d
        b.append((f(ap1,x)-f(ap2,x))/2/d)
    return np.column_stack(b)

def Gauss(f,a0,x,y,err):        
    a=a0.copy()                      
    e=1   
    r=0                             
    while e>err:                     
        a1=a
        r=f(a1,x)-y
        j=J(f,a1,x)
        a1=a1-(np.linalg.inv(j.T@j)@j.T@r)
        e=np.linalg.norm(a1-a)
        a=a1
    return a


f=function
a0=[]
final=Gauss(f,a0,x,y,err)




###multivariate newton method
def multinewt():
    global zs,xs
    x0=np.array(list(start),float)
    xs=[]
    errs=[]
    zs=[]
    err=1
    xi=x0.copy()
    i=0
    xs.append(xi)
    errs.append(err)
    zs.append(f(xi))
    while err>0.0001:
        i=i+1
        p=(-np.linalg.inv(hessian(f,xi))@jacobian(f,xi).T).reshape(2)
        err=abs(f(xi)-f(xi+p))
        xi=xi+p
        xs.append(xi)
        errs.append(err)
        zs.append(f(xi))
    zs=np.array(zs)
    xs=np.array(xs).reshape(len(xs),2)  

    
###steepest descent    
from scipy.optimize import rosen
f=rosen
def jacobian(x):
    d=0.0001
    b=[]
    for i in range (len(x)):
        xp1=x.copy()
        xp2=x.copy()
        xp1[i]=xp1[i]+d
        xp2[i]=xp2[i]-d
        b.append((f(xp1)-f(xp2))/2/d)
    return np.column_stack(b)


x0=np.array([0.5,-0.5],float)
xs=[]
errs=[]
zs=[]
err=1
xi=x0.copy()
i=0
xs.append(xi)
errs.append(err)
zs.append(f(xi))
while err>0.00125:
    i=i+1
    p=-jacobian(xi).reshape(2)
    a=line_search(f,jacobian,xi,p)[0]
    err=abs(f(xi)-f(xi+a*p))
    xi=xi+a*p
    xs.append(xi)
    errs.append(err)
    zs.append(f(xi))
    print(i,'   ',p,'   ',a,'   ',xi,'   ',err)
zs=np.array(zs)
xs=np.array(xs).reshape(len(xs),2)  
