from astropy.io import fits

header_gal_txt = """
SIMPLE  =                    T / conforms to FITS standard
BITPIX  =                  -64 / array data type
NAXIS   =                    2 / number of array dimensions
NAXIS1  =                   12
NAXIS2  =                   12
CRVAL1  =                  0.0 / Value at ref. pixel on axis 1
CRVAL2  =                  0.0 / Value at ref. pixel on axis 2
CTYPE1  = 'GLON-CAR'           / Type of co-ordinate on axis 1
CTYPE2  = 'GLAT-CAR'           / Type of co-ordinate on axis 2
CRPIX1  =                  7.0 / Reference pixel on axis 1
CRPIX2  =                  7.0 / Reference pixel on axis 2
CDELT1  =      -0.005555555556 / Pixel size on axis 1
CDELT2  =       0.005555555556 / Pixel size on axis 2
END
""".strip().lstrip()

header_radec_txt = """
SIMPLE  =                    T / conforms to FITS standard
BITPIX  =                  -64 / array data type
NAXIS   =                    2 / number of array dimensions
NAXIS1  =                   12
NAXIS2  =                   12
CRVAL1  =        266.416816625 / Value at ref. pixel on axis 1
CRVAL2  =        -29.007824972 / Value at ref. pixel on axis 2
CTYPE1  = 'RA---TAN'           / Type of co-ordinate on axis 1
CTYPE2  = 'DEC--TAN'           / Type of co-ordinate on axis 2
CRPIX1  =                  7.0 / Reference pixel on axis 1
CRPIX2  =                  7.0 / Reference pixel on axis 2
CDELT1  =      -0.005555555556 / Pixel size on axis 1
CDELT2  =       0.005555555556 / Pixel size on axis 2
EQUINOX =               2000.0
END
""".strip().lstrip()

header_radec2_txt = """
SIMPLE  =                    T / conforms to FITS standard
BITPIX  =                  -64 / array data type
NAXIS   =                    2 / number of array dimensions
NAXIS1  =                   24
NAXIS2  =                   24
CRVAL1  =        266.416816625 / Value at ref. pixel on axis 1
CRVAL2  =        -29.007824972 / Value at ref. pixel on axis 2
CTYPE1  = 'RA---TAN'           / Type of co-ordinate on axis 1
CTYPE2  = 'DEC--TAN'           / Type of co-ordinate on axis 2
CRPIX1  =                 13.0 / Reference pixel on axis 1
CRPIX2  =                 13.0 / Reference pixel on axis 2
CDELT1  =             -0.00225 / Pixel size on axis 1
CDELT2  =              0.00225 / Pixel size on axis 2
EQUINOX =               2000.0
END
""".strip().lstrip()

header_gal = fits.Header().fromstring(header_gal_txt,'\n')
header_radec = fits.Header().fromstring(header_radec_txt,'\n')
header_radec2 = fits.Header().fromstring(header_radec2_txt,'\n')
