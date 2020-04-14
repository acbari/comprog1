import sys, readtxt

namafile = sys.argv[1]
filter = sys.argv[2]
data = readtxt.bacafile(namafile, int(filter))
