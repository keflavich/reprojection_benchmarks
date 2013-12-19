from python_reprojection import reproject
from FITS_tools.hcongrid import hcongrid_hdu, wcsalign

import headers
import data

from astrop.io import fits

def test_simple():
    hdu_in = fits.PrimaryHDU(data=data.simple_3by3(),header=headers.header_radec)
    hdr_out = header.header_radec2

    hcr = hcongrid_hdu(hdu_in, hdr_out)
    ast = wcsalign(hdu_in, hdr_out)
    rep = reproject(hdu_in, hdr_out)
