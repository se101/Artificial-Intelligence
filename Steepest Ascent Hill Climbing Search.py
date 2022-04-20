#QUESTION 2: 2019A7PS1207H 2019A7PS0003H

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

array=np.array([[8,10,3],[12,6,2],[5,1,7],[11,4,9]])
original_array=np.array([[8,10,3],[12,6,2],[5,1,7],[11,4,9]])
array1=np.array([[9,5,1],[10,6,2],[11,7,3],[12,8,4]])
count=0
h=0

#jump function
def jump(array,i,j):
    if (j!=2):
        temp=array[i,j]
        array[i,j]=array[i,j+1]
        array[i,j+1]=temp
    if (j==2):
        temp=array[i,j]
        array[i,j]=array[i,j-1]
        array[i,j-1]=temp
    return array

#clockwise rotate function
def c_rotate(array,i,j):
    temp1=array[0,j]
    temp2=array[1,j]
    temp3=array[2,j]
    temp4=array[3,j]
    array[0,j]=temp4
    array[1,j]=temp1
    array[2,j]=temp2
    array[3,j]=temp3
    return array

#anti-clockwise rotate function
def a_rotate(array,i,j):
    temp1=array[0,j]
    temp2=array[1,j]
    temp3=array[2,j]
    temp4=array[3,j]
    array[0,j]=temp2
    array[1,j]=temp3
    array[2,j]=temp4
    array[3,j]=temp1
    return array

#optimal heuristic function: number of misplaced tiles
def heuristic(array1,array2):
    count=0
    for i in range(4):
        for j in range(3):
            #print(array1[i,j],array2[i,j],"\n")
            if array1[i,j]==array2[i,j]:
                count+=1
    return (12-count)

#function to find all neighbours of a state 
def neighbours(array):
    neighbors = []
    statements = []
    for i in range(4):
        for j in range(3):
            array_copy1=np.copy(array)
            jump(array_copy1,i,j)
            neighbors.append(array_copy1)
            statements.append(f"Jump({array_copy1[i,j]}):\n{array_copy1}")
            array_copy2=np.copy(array)
            c_rotate(array_copy2,i,j)
            neighbors.append(array_copy2)
            statements.append(f"C_Rotate({array_copy2[i,j]}):\n{array_copy2}")
            array_copy3=np.copy(array)
            a_rotate(array_copy3,i,j)
            neighbors.append(array_copy3)    
            statements.append(f"A_Rotate({array_copy3[i,j]}):\n{array_copy3}")
    return neighbors,statements

def Steepest_Ascent_Hill_Climbing(array, initial_array, current_heuristic, current_neighbors, iterations = 100 ):
    initial_state = original_array  
    distance = current_heuristic(initial_state,array) 
    
    for i in range(iterations): 
        # Generate all neighbors
        neighbors,statements_n = current_neighbors(initial_state)
        heuristics_neighbors = []
        # Loop over each neighbor and calculate the heuristic
        for n in neighbors:
            d = current_heuristic(n,array)
            heuristics_neighbors.append(d)
        # Get the index of the smallest heuristic 
        min_distance_index = heuristics_neighbors.index(min(heuristics_neighbors))
        # Get the relative neighbor 
        #if ((initial_state==neighbors[min_distance_index]).all()):
        #    del heuristics_neighbors[min_distance_index]
        #    min_distance_index = heuristics_neighbors.index(min(heuristics_neighbors))
        initial_state = neighbors[min_distance_index]
        global h
        global count
        if(h==current_heuristic(initial_state,array)):
            count+=1
        h=current_heuristic(initial_state,array)
        #print(initial_state)
        print(statements_n[min_distance_index])
    # Return the final state, and its heuristic 
    return initial_state, current_heuristic(initial_state,array)

# jump(array,3,1)
# print("Jump(", array[3,1], "): \n", array)
# print(heuristic(array,array1))
# c_rotate(array,3,1)
# print("C_Rotate(", array[3,1], "): \n", array)
# a_rotate(array,3,1)
# print("A_Rotate(", array[3,1], "): \n", array)
# print("Neighbours:\n", neighbours(array))

# Steepest Ascent Hill Climbing algorithm with 100 iterations
iterations = 100
final_state, heuristic_n = Steepest_Ascent_Hill_Climbing(array1, array, heuristic, neighbours, iterations = iterations )
# # The best state found is
print(f'Best state found is with {heuristic_n} heuristic value with {iterations} iterations:\n {final_state}')
if(count>10):
    print(f'Number of times heuristic {h} has occurred is: {count} times')
    print('Therefore, it is a PLATEAU condition')

