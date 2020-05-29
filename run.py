import numpy as np
from modules import animate, make_striped_matrix

size = 32
A = np.random.randint(high=2, low=0, size=(size,size))

#A = make_striped_matrix(size)


animate(A)
