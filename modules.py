import numpy as np
import matplotlib.pyplot as plt


def find_neighbors(i, j, matrix):
    
    """Creates a list of neighbor statuses."""
    
    neighbors = []
    
    
    ### distinguish the edge cases
    if i == 0:
        i_eval = [0,1]
    elif i == matrix.shape[0]-1:
        i_eval = [-1,0]
    else:
        i_eval = [-1,0,1]
        
    if j == 0:
        j_eval = [0,1]
    elif j == matrix.shape[0]-1:
        j_eval = [-1,0]
    else:
        j_eval = [-1,0,1]
        
    
    for i_inc in i_eval:
        for j_inc in j_eval:
            
            # the same element - skip
            if i_inc == 0 and j_inc ==0:
                continue
            
            # append neighbor element statuses
            else:
                
                neighbors.append(matrix[i+i_inc,j+j_inc])
                

                
    return neighbors


def evolve(matrix):
    
    """Function that evolves the matrix according to the stated rules."""
    
    new_state = np.copy(matrix)
    
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):

            neighbor_elements = find_neighbors(i,j, matrix)
            
            alive_neighbors = np.count_nonzero(neighbor_elements)
            
            if matrix[i,j] == 1:
                
                if alive_neighbors not in [2,3]:

                    new_state[i,j] = 0

            elif matrix[i,j] == 0:

                if alive_neighbors > 3:
                    new_state[i,j] = 1
                    
    return new_state


def animate():

    plt.ion()
    for i in range(1000):
        
        # special case for the start of the animation
        # displays the starting matrix
        if i == 0:
            updated = np.random.randint(low=0, high=2, size=(32,32)) 


        else:
            updated = evolve(updated)
        plt.imshow(updated)
        plt.pause(1)
        plt.clf()
