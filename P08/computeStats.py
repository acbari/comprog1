import numpy as np
import readtxt

data = readtxt.bacafile("rand.txt", 0)
npdata = np.array(data)
print( "Mean value   :",np.mean(npdata) )
print( "Max value    :",np.max(npdata) )
print( "Min value    :",np.min(npdata) )
print( "Std deviation:",np.std(npdata) )



