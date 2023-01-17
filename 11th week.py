

import numpy as np
import matplotlib.pyplot as pt
from mpl_toolkits import mplot3d
f=lambda x,a:np.exp(-(x[0]-a[0])**2-(x[1]-a[1])**2)

a=[1,2]
x1=np.random.uniform(-3,5,400)
x2=np.random.uniform(-3,5,400)
y=f([x1,x2],a)+np.random.normal(0,0.1,400)
x=[x1,x2]

pt.figure()
ax=pt.axes(projection='3d')
ax.scatter3D(x[0],x[1],y)

r=np.linspace(-3,5,20)
u1,u2=np.meshgrid(r,r)
z=f([u1,u2],a)
ax.plot_surface(u1,u2,z,color='green',alpha=0.4)
