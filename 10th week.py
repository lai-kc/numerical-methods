import numpy as np

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
        print('a','   ',a)
        #print(r)
        r=f(a1,x)-y
        j=J(f,a1,x)
        print('hess','   ',j.T@j)
        print('eig','   ',np.linalg.eigvals(j.T@j))
        print('error','   ',e)
        print('')
        print('')
        a1=a1-(np.linalg.inv(j.T@j)@j.T@r)
        e=np.linalg.norm(a1-a)
        a=a1
    return a


f=function
a0=[]
final=Gauss(f,a0,x,y,err)
