import numpy as np
from astropy.io import fits
import headers

def simple_3by3():
    z = np.zeros([3,3])
    z[1,1] = 1.0
    return z

def simple_3by3_hdu():
    return fits.PrimaryHDU(data=simple_3by3(),
                           header=headers.generate_nxn_header(3))


def centered_gaussian():
    x,y = np.mgrid[:9,:9]
    sigma = 1.0
    g = np.exp(-((x-4)**2+(y-4)**2)/(2*sigma**2))
    return g

def centered_gaussian_hdu():
    return fits.PrimaryHDU(data=centered_gaussian(),
                           header=headers.generate_nxn_header(9))


def empty_nbyn(n):
    z = np.zeros([n,n])
    return z

def simple_nbyn_hdu(n):
    return fits.PrimaryHDU(data=empty_nbyn(n),
                           header=headers.generate_nxn_header(n))
