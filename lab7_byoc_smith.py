'''
This is a script that opens and reads SEG-Y format files downloaded from 
NOAA NCEI. It converts seg-y traces to a 2-D numpy array and plots them.

Not yet completed (##): combining traces with gps coordinates. Reading in 
multiple files and concatenating them to view larger areas of trackline.

inputs: seg-y file, associated .txt file containing gps coordinates of pings
outputs: plot of traces

'''

import numpy as np
import matplotlib.pyplot as plt
from obspy.io.segy.segy import _read_segy
import sys

# import parameters

filepath = sys.argv [1]
##textfile = sys.argv [2]

# read in segy file

segy = _read_segy(filepath, headonly = True)

# creating 2-D numpy array from traces held in segy object
# .T transposes so that twt is y-axis and trace number is x-axis

data = np.stack([t.data for t in segy.traces]).T

# printing rows and columns

print(f"array shape is: {data.shape}")


# plotting stacked data. TO UPDATE: find a better cmap for visualization

plt.imshow(data, cmap='gray_r', aspect='auto')

plt.title("Healy 0703_2007_229_1847 Subbottom")
plt.xlabel("trace number")
plt.ylabel("two way travel time")
plt.colorbar(label="amplitude")
plt.show()
