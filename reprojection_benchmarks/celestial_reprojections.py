from __future__ import print_function
from reproject.reproject import reproject as pyreproject
from FITS_tools.hcongrid import hcongrid_hdu, wcsalign
from montage_wrapper import reproject_hdu as montage

import warnings
warnings.filterwarnings('ignore')

# should be relative imports, but I want to use this with %run...
import headers
import data
import tempfile

from astropy.io import fits
from astropy import log
log.setLevel("WARN")
#log.disable_warnings_logging()
#log.disable_exception_logging()

import numpy as np

import timeit

reproject_cmds = ('pyreproject','montage_hdu','hcongrid_hdu','wcsalign')

def montage_hdu(hdu_in, hdr_out):
    hdr = tempfile.NamedTemporaryFile()
    hdr_out.totextfile(hdr.name)
    mon = montage(hdu_in, header=hdr.name, silence=True)
    hdr.close()

    return mon

def all_tools(hdu_in, hdr_out):

    hcr = hcongrid_hdu(hdu_in, hdr_out)
    ast = wcsalign(hdu_in, hdr_out)
    rep = pyreproject(hdu_in, hdr_out)
    mon = montage_hdu(hdu_in, hdr_out)

    return hcr,ast,rep,mon

def test_simple():
    hdu_in = data.simple_3by3_hdu()
    hdr_out = headers.header_radec2

    return all_tools(hdu_in,hdr_out)


def aplpy_simple():
    import aplpy

    F = aplpy.FITSFigure(data.simple_3by3_hdu())
    F.show_grayscale()

    hcr,ast,rep,mon = test_simple()

    F.show_contour(hcr,colors=[(1,0,0,0.5)],filled=True)
    F.show_contour(ast,colors=[(0,1,0,0.5)],filled=True)
    F.show_contour(rep,colors=[(0,0,1,0.5)],filled=True)

def test_centered_gaussian():
    hdu_in = data.centered_gaussian_hdu()
    hdr_out = headers.header_radec2

    return all_tools(hdu_in,hdr_out)


def aplpy_centered_gaussian():
    import aplpy
    import pylab as pl

    fig = pl.figure(1)
    fig.clf()

    F = aplpy.FITSFigure(data.centered_gaussian_hdu(), subplot=(2,3,1), figure=fig)
    F.show_grayscale()
    F._ax1.set_title("Input")

    hcr,ast,rep,mon = test_centered_gaussian()

    titles = ['hcongrid','wcsalign/starlink','pyreproject','montage']

    figs = []
    for ii,im in enumerate((hcr,ast,rep,mon)):
        figs.append(aplpy.FITSFigure(im,subplot=(2,3,ii+2), figure=fig))
        figs[-1].show_grayscale()
        figs[-1].show_contour(data.centered_gaussian_hdu())
        figs[-1]._ax1.set_title(titles[ii])

    F.save('centered_gaussian_test.png')


def timing_shrink():
    times = {}
    sizes = (8,16,32,64,128)
    for n in sizes:
        times[n] = {}

        for reproject_cmd in reproject_cmds:
            setup = ("import data,headers\n"
                     "from celestial_reprojections import {reproject_cmd}\n"
                     "hdu_in = data.simple_nbyn_hdu({n})\n"
                     "hdr_out = headers.generate_nxn_header(int({n}/2.))\n"
                     ).format(reproject_cmd=reproject_cmd, n=n)
            T = timeit.Timer(setup=setup,
                         stmt="{0}(hdu_in,hdr_out)".format(reproject_cmd))

            times[n][reproject_cmd] = np.median(T.repeat(3,10))


    print(" ".join(["%15s" % x for x in (['reproject_cmd']+[n for n in sizes])]))
    for reproject_cmd in reproject_cmds:
        line = " ".join(["%15s" % x for x in ([reproject_cmd]+[times[n][reproject_cmd] for n in sizes])])

        print(line)


