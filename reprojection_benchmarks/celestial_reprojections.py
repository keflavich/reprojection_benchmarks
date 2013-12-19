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

def test_centered_gaussian():
    hdu_in = data.centered_gaussian_hdu()
    hdr_out = headers.header_radec2

    hcr = hcongrid_hdu(hdu_in, hdr_out)
    ast = wcsalign(hdu_in, hdr_out)
    rep = reproject(hdu_in, hdr_out)

    return hcr,ast,rep

def aplpy_centered_gaussian():
    import aplpy
    import pylab as pl

    fig = pl.figure(1)
    fig.clf()

    F = aplpy.FITSFigure(data.centered_gaussian_hdu(), subplot=(2,2,1), figure=fig)
    F.show_grayscale()
    F._ax1.set_title("Input")

    hcr,ast,rep = test_centered_gaussian()

    titles = ['hcongrid','wcsalign/starlink','reproject']

    figs = []
    for ii,im in enumerate((hcr,ast,rep)):
        figs.append(aplpy.FITSFigure(im,subplot=(2,2,ii+2), figure=fig))
        figs[-1].show_grayscale()
        figs[-1].show_contour(data.centered_gaussian_hdu())
        figs[-1]._ax1.set_title(titles[ii])

    F.save('centered_gaussian_test.png')

