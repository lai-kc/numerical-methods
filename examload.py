#load examdata.npy
#change your working directory, then run
import numpy as np
with open('examdata.npy','rb') as f:
    x1=np.load(f)
    x2=np.load(f)
    y=np.load(f)
