import random
import math

MIN=-10
MAX=10
N=20
LOOPS =500*500
class solution:
    variable = [0]*N
    utility = 0
individual = solution()

for j in range (N):
    individual.variable[j] = random.uniform(MIN,MAX)
individual.utility = 0

def test_function( ind ):
    utility = 0
    a=0
    b=0
    c=0
    for i in range (0,N):
        a = a + ind.variable[i]**2
        b = b + (0.5*(i+1)*ind.variable[i])
        c = c + (0.5*(i+1)*ind.variable[i])
       
    utility= a + b**2 + c**4
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
    