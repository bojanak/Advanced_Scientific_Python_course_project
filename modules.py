import numpy as np
import matplotlib.pyplot as plt
from itertools import product
from celluloid import Camera


### Functions that generate matrices

def make_random_matrix(size=32):

    """Returns a random matrix.
    
    Parameters:
        size (int): The matrix dimensions (size*size)
    
    Returns:
        matrix (numpy.ndarray): The random matrix
        
    """

    matrix = np.random.randint(high=2, low=0, size=(size,size))    

    return matrix



def make_cross_shaped_matrix(size = 32, thickness = 5):

    """Generates a cross-shaped matrix. Default stripe thickness = 5.
    
    Paramters:
        size (int): The matrix dimensions (size*size)
        thickness (int): The thickness of the stripes - default value is 5
        
    Returns:
        matrix (numpy.ndarray): The cross-shaped matrix
    
    """

    matrix = np.zeros((size,size))
    matrix[int(size/2-thickness/2):int(size/2+thickness/2), :] = 1
    matrix[:, int(size/2-thickness/2):int(size/2+thickness/2)] = 1


    return matrix


##########
    

def evolve(A):

    """Function which takes in a matrix and evolves it over one timestep, according to the rules.
    
    Paramters:
        A (numpy.ndarray): The matrix with which one timestep begins
        
    Returns:
        B (numpy.ndarray): The outcome of evolving the matrix
    
    """

    ### Functions:

    def get_neighbors_index_list(elem_indices):

        """Returns a generator with  that outputs the neighbors' indices in the matrix.
        
        Paramters:
            elem_indices (tuple): Tuple of indices of one matrix element
        
        Returns:
            c (list): List of tuples with indices of that element's neighbors
        
        """

        for c in product(*(range(n-1, n+2) for n in elem_indices)):
            if c != elem_indices and all(0 <= n < size for n in c):
                yield c


    # this function will be run on each matrix element
    def check_neighbors(elem_indices):


        """The function evaluates the neighbours' statuses and changes their respective statuses according to the rules.
        
        Parameters:
            elem_indices (tuple): Tuple of indices of one matrix element
            
        """
        
        
        # generates the neighbor indices list
        neighbor_list= list(get_neighbors_index_list(elem_indices))


        # creates a list of neighbor values
        neighbor_values = []

        for neighbor_indices in neighbor_list:
            k,l = neighbor_indices[0], neighbor_indices[1]

            neighbor_values.append(A[k,l])


        # counts the number of alive neighbors
        alive_neighbors = np.count_nonzero(neighbor_values)

        # Kills the alive cells if necessary
        if A[elem_indices[0],elem_indices[1]] == 1 and alive_neighbors not in [2,3]:

            B[elem_indices[0],elem_indices[1]] = 0

        # revives the dead cells if necessary
        elif A[elem_indices[0],elem_indices[1]] == 0 and alive_neighbors == 3:

            B[elem_indices[0],elem_indices[1]] = 1

    ##################

    # this will be the output matrix
    B = np.copy(A)
    size = A.shape[0]

    # generating a list of tuples with matrix indices of all elements
    ind_matrix = np.empty((size,size), dtype=object)
    for p in np.arange(size):
        for q in np.arange(size):

            ind_matrix[p,q] = (p,q)

    ind_matrix =ind_matrix.flatten()

    # run the function on all matrix index combinations
    run=np.vectorize(check_neighbors)

    run(ind_matrix)

    return B


def animate(type = 'random', size = 32, thickness=None, animate = True, n_steps = 500):

    """Function that runs the simulation and animates it.
    
    Parameters:
        type (str): Defines the type of matrix to be used as seed. The default values is "random"
        size (int): Specifies the size of the seed matrix. The default value is 32.
        thickness(int or NoneType): Specifies the thickness of the cross-shaped matrix if that is the type the user specified under "type". The default value is None.
        animate (bool): Turns the animation on/off. The default values is True
        n_steps (int): Specifies the number of evolution steps to be performed
        
    Returns:
        outcome (numpy.ndarray): The matrix representing the final state after the seed matrix has been propagated n_steps times.
    
    """
    
    # generating the seed matrix
    if type == 'random':
        matrix = make_random_matrix(size) 
    if type == 'cross_shaped':
        if thickness is not None:
            matrix = make_cross_shaped_matrix(size, thickness)
        else: 
            matrix = make_cross_shaped_matrix(size)

    
    fig = plt.figure()
    camera = Camera(fig)

    # animation will run for n_steps times
    for i in range(n_steps):

        try:
            state = evolve(state)
 
        except NameError:
            state = matrix
        
        # settings for plotting each state
        plt.xticks([],[])
        plt.yticks([],[])
        plt.imshow(state, cmap = 'Reds')
        camera.snap()
        old_state = state
 
    if animate == True:
        animation = camera.animate(repeat=False) #generates the animation out of all n_steps states
        plt.show()
                   
    return state

