import numpy as np

def simple_3by3():
    z = np.zeros([3,3])
    z[0,0] = 1.0
    return z


def centered_gaussian():
    x,y = np.mgrid[:9,:9]
    sigma = 1.0
    g = np.exp(-((x-4)**2+(y-4)**2)/(2*sigma**2))
    return g
