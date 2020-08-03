import numpy as np
from modules import animate



parameters = {'type': 'cross_shaped',
              'size': 32,
              'thickness': 3,
              'animate': False,
              'n_steps': 1000}

outcome = animate(**parameters)

def test_modules():
    assert (outcome == np.zeros(shape = outcome.shape)).all()


