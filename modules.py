import numpy as np
import matplotlib.pyplot as plt
from itertools import product
from celluloid import Camera

def make_random_matrix(size=32):

    """Returns a random matrix. """

    matrix = np.random.randint(high=2, low=0, size=(size,size))    

    return matrix



def make_cross_shaped_matrix(size = 32, thickness = 5):

    """Generates a striped matrix. Default stripe thickness = 5. """

    matrix = np.zeros((size,size))

    matrix[int(size/2-thickness/2):int(size/2+thickness/2), :] = 1
    matrix[:, int(size/2-thickness/2):int(size/2+thickness/2)] = 1


    return matrix


def evolve(A):

    """Function which takes in a matrix and evolves it according to the rules"""

    ### Functions:

    def get_neighbors_index_list(elem_indices):

        """Returns a generator with  that outputs the neighbors' indices in the matrix"""

        for c in product(*(range(n-1, n+2) for n in elem_indices)):
            if c != elem_indices and all(0 <= n < size for n in c):
                yield c


    # this function will be run on each matrix element
    def check_neighbors(elem_indices):


        """ Takes in a tuple of matrix element's indices, evaluates the neighbours' statuses and sets its value accordingly

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

    # generating the matrix
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

        plt.xticks([],[])
        plt.yticks([],[])
        plt.imshow(state, cmap = 'Reds')
        camera.snap()
        old_state = state
 
    if animate == True:
        animation = camera.animate(repeat=False)
        plt.show()
                   
    return state

