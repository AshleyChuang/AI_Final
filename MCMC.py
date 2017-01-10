#          A  B  C  D  E  F
initial = [1, 0, x, x, x, x]
Num_of_nodes = 5;

CPT = [[ 0 ,  0 , 0.1, 0.9,  0 ,  0 ],
       [ 0 ,  0 , 0.2, 0.8,  0 ,  0 ],
       [ 0 ,  0 ,  0 ,  0 , 0.3, 0.7],
       [ 0 ,  0 ,  0 ,  0 , 0.4, 0.6],
       [0.5, 0.5,  0 ,  0 ,  0 ,  0 ],
       [0.6, 0.4,  0 ,  0 ,  0 ,  0 ]]


counter = [100, 150, 200, 110, 230, 300]

import random

def probability(p):
    if random.randint(0, 99) < p * 100:
        return 1 # can be changed
