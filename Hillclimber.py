import random
import math

MIN=-10
MAX=10
N=20
LOOPS =500*200
class solution:
    variable = [0]*N
    utility = 0
individual = solution()

for j in range (N):
    individual.variable[j] = random.uniform(MIN,MAX)
individual.utility = 0

def test_function( ind ):
    utility = 0
    b=0
    for i in range (N):
       b = b + ( ind.variable[i]**2 - (10* math.cos((2*math.pi)*ind.variable[i])))   
    a = 10*N
    utility = a + b
    return utility


individual.utility= test_function(individual)
newind = solution()
for x in range (LOOPS):
    for i in range(N):
        newind.variable[i] = individual.variable[i]
    change_point = random.randint(0, N-1)
    newind.variable[change_point] = random.uniform(MIN,MAX)
    newind.utility = test_function( newind )
    if individual.utility >= newind.utility:
        individual.variable[change_point] = newind.variable[change_point]
        individual.utility = newind.utility
    print(individual.utility)
    
