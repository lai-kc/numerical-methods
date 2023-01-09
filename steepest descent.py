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
