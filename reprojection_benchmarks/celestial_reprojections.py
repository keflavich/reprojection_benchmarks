from reproject.reproject import reproject
from FITS_tools.hcongrid import hcongrid_hdu, wcsalign

import headers
import data

from astropy.io import fits

def test_simple():
    hdu_in = data.simple_3by3_hdu()
    hdr_out = headers.header_radec2

    hcr = hcongrid_hdu(hdu_in, hdr_out)
    ast = wcsalign(hdu_in, hdr_out)
    rep = reproject(hdu_in, hdr_out)

    return hcr,ast,rep

def aplpy_simple():
    import aplpy

    F = aplpy.FITSFigure(data.simple_3by3_hdu())
    F.show_grayscale()

    hcr,ast,rep = test_simple()

    F.show_contour(hcr,colors=[(1,0,0,0.5)],filled=True)
    F.show_contour(ast,colors=[(0,1,0,0.5)],filled=True)
    F.show_contour(rep,colors=[(0,0,1,0.5)],filled=True)
