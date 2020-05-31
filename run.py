import numpy as np
from modules import animate, cross_shaped

size = 32
#A = np.random.randint(high=2, low=0, size=(size,size))

A = cross_shaped(size)


animate(A)
