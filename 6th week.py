
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
