import numpy as np
import math
def digits(n):
    return np.array(list(str(n)),dtype=object)
def from_digits(x):
    return int(''.join(np.array(x,dtype=np.str0)))

def list_lengths(p):
    res=np.array([])
    for x in np.arange(1, int(p / 2)):
        for y in np.arange(x, int(p / 2)):
            if math.sqrt(x ** 2 + y ** 2) == p - (x + y):
                res=np.append(res,(x,y,p-(x+y)))
    return res


def eu_39(limit=1000):
    counter=np.array([])
    for p in np.arange(limit):
        counter=np.append(counter,(len(list_lengths(p))))
        np.argmax(counter)
    return ('p:',np.argmax(counter),list_lengths(np.argmax(counter)).reshape(-1,3))

# print(eu_39(1000))
def champernowne(base=10,iter=100):
        return ''.join(np.concatenate((np.array(['0.']),np.array([np.base_repr(i,base=base) for i in np.arange(iter)]))))
print(champernowne(base=7,iter=15))





