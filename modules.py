import numpy as np

def find_neighbors(i, j):
    neighbors = []
    for i_inc in [-1,0,1]:
        for j_inc in [-1,0,1]:
            if i_inc == 0 and j_inc ==0:
                continue
            else:
                if i+i_inc >-1 and j+j_inc >-1:
                    
                    neighbors.append(matrix[i+i_inc,j+j_inc])
                    print('added')
                    print(i+i_inc,j+j_inc)

                
    return neighbors


def evolve(matrix):
    
    new_state = np.copy(matrix)
    
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):

            neighbor_elements = find_neighbors(i,j)
            alive_neighbors = np.count_nonzero(neighbor_elements)

            if matrix[i,j] == 1:

                if alive_neighbors < 2 and alive_neighbors > 3:
                    new_state[i,j] == 0

            if matrix[i,j] == 0:

                if alive_neighbors > 3:
                    new_state[i,j] == 1
    
    return new_state