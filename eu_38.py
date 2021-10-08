import numpy as np
import math
def digits(n):
    return np.array(list(str(n)),dtype=object)
def from_digits(x):
    return int(''.join(np.array(x,dtype=np.str0)))
def eu_38():
    res=np.array([],dtype=object)
    for n in np.arange(2,10000):
        concatenated=np.array([])
        for i in np.arange(1,n):
            concatenated=np.append(concatenated,digits(i*n))
            if len(np.unique(concatenated))!=len(concatenated):
                break
            if len(concatenated)==9 and 0 not in concatenated:
                res=np.append(res,(n,i,concatenated))
                break
        n=n+1

    return  res.reshape(-1, 3)[:,2]





