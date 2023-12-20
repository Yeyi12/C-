import random
import copy
import matplotlib.pyplot as plt
import numpy as np
N = 20
P = 100
G = 200
MUTRATE =0.008
MUTSTEP =1.0
MAX = 10
MIN = -10

class solution:
    variable = [0]*N
    utility = 0
individual = solution()

for j in range (N):
    individual.variable[j] = random.randint(0,100)
individual.utility = 0

def test_function( ind ):
    b=0
    for i in range (1,N):   
        b = b + (i*(2*ind.variable[i])**2 - (ind.variable[i-1]))**2
    a = (ind.variable[0]-1)**2
    utility = a + b
    return utility

newind = solution()
for x in range (P):
    for i in range(N):
        newind.variable[i] = individual.variable[i]
    change_point = random.randint(0, N-1)
    newind.variable[change_point] = random.randint(0,100)
    newind.utility = test_function( newind )
    if individual.utility <= newind.utility:
        individual.variable[change_point] = newind.variable[change_point]
        individual.utility = newind.utility

plt.plot(newind)