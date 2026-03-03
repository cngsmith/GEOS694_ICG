'''
This is a script that opens and reads SEG-Y format files downloaded from 
NOAA NCEI. It plots the traces in the segy files and combines them with
the gps coordinates in associated .txt files.

inputs: seg-y file, associated .txt file containing gps coordinates of pings
outputs: plot of twt.

'''

import numpy as np
import matplotlib.pyplot as plt
from obspy.io.segy.segy import _read_segy
from obspy.core.util import get_example_file
import sys


segy = _read_segy("/Users/celinesmith/Desktop/GEOS694/assignments/GEOS694_lab7byoc_smith/HE0703/Digital/he0703_2007_229_1847_LF_000.sgy")

print(segy)



# def segy_to_numpy():
#     '''turns binary data into a 2D numpy array for plotting'''