# TODO: Implement field equations of different approximation elements: Electric monopole, magnetic monopole, electric
#   dipole, magnetic dipole. Monopole elements change charge over time?

# Meeting with Bojana 04-14-21:
# - Do we need our own forward solver or can we use QuickWave?
# - Three possibilities:
#       - Forward solution with pseudo inversion:
#           Good because we can have any geometry. Maybe extract matrix directly from QWED?
#       - Precalculate different inhomogeneities?
#       - Signal processing from measured signals
#
# Transmission line matrix method?
#
# Just implement predefined positions of e.g. current elements - Biot-Savart Law
# Most likely phase less since field is evanescent (ring circumference is much small than free space wavelength.
