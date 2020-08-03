from modules import animate


parameters = {'type': 'cross_shaped', # or 'random'   
              'size': 32,
              'thickness': 5, # if type = 'random', set to None or delete
              'animate': True,
              'n_steps': 500}

outcome = animate(**parameters)
