
import random
import copy
import matplotlib.pyplot as plt
import numpy as np
import math

#random. randint(0, 1)
#number of genes
N= 20
#population size
P= 500
G = 200
MUTRATE = 0.009
MUTSTEP = 2.00
#first worksheet, xi ranges from -5.12 to 5.12, in this one x ranges -10 to 10, how does
#this apply in the code, max and min is used in mutation, mutation step?
MIN = -10
MAX = 10



class individual:
    def __init__(self):
        self.gene = [0]*N
        self.fitness=0
 
#edit this part        
def test_function( ind ):
    a = 0
    b=0
    
    #said the loop can only start from 0, ask if it can start from 1, does d represent number of genes
    #ask if i can use a while loop, while i=2, the count of i increases, stops at 20
    #for i in range (d):
    #b = b + (2*(ind.gene[i+1])**2 - i*(ind.gene[(i+1)-1])**2)
       
    #a = (ind.gene[i]-1)^2
    #utility = a + b
    #utility=0
    #for i in range (N):
    #utility = utility + ind.gene[i]
    #while i == 2:
    for i in range (1,N):    
        b = b + (i*(2*ind.gene[i])**2 - (ind.gene[i-1]))**2
       
    a = a + ((ind.gene[0]-1)**2)
    utility = a + b
    return utility



population = []
#initializing population


#list of total fitness
def fits():
    for x in range(0, P):
        total_fit=[]
        for y in range(0,N):
            total_fit.append(random.uniform(MIN, MAX))
        newind = individual()
        newind.gene=total_fit.copy()
    
            # calculate the fitness using the test function
        # newind.fitness = sum(total_fit)
        newind.fitness = test_function(newind)
        population.append(newind)
    return total_fit
    
#for x in population:
    #print(x.gene)
    #print(x.fitness)
    #print("*************")
    
#append total fitness to plot  

#call the fitness function
fits()
#make functions
#selection func
offspring = []
def selection():
    #print(len(population))
    for i in range (0,P):
        parent1= random.randint(0, P-1)
        off1 = copy.deepcopy(population[parent1])
        parent2 = random.randint(0, P-1)
        off2 = copy.deepcopy(population[parent2])
        if off1.fitness < off2.fitness:
            offspring.append(off1)
        else:
            offspring.append(off2)
    return offspring

#crossover function
def crossover():
    toff1 = individual()
    toff2 = individual()
    temp = individual()
    for i in range (0, P, 2):
        toff1 = copy.deepcopy(offspring[i])
        toff2 = copy.deepcopy(offspring[i+1])
        temp = copy.deepcopy(offspring[i])
        crosspoint= random.randint(1,N)
        crosspoint2 = random.randint(crosspoint, N)
        for j in range(crosspoint, crosspoint2):
            toff1.gene[j] = toff2.gene[j]
            toff2.gene[j] = temp.gene[j]
        offspring[i] = copy.deepcopy(toff1)
        offspring[i+1]= copy.deepcopy(toff2)
    return offspring
        
#mutation func
#mutation function is edited too, we work with floats now do random.uniform
def mutation():
    for i in range (0, P):
        newind = individual()
        newind.gene=[]
        for j in range (0, N):
            gene = offspring[i].gene[j]
            mutprob = random.random()
            #print(mutprob)
            if mutprob < MUTRATE:
                alter = random.uniform(-MUTSTEP,MUTSTEP)
                gene = gene + alter
                if gene > MAX:
                    gene = MAX
                if gene < MIN:
                    gene = MIN
                #if(gene==1):
                    #gene = 0
                #else:
                    #gene = 1
            newind.gene.append(gene)
        newind.fitness = test_function(newind)
         #you must now append the new individual or overwite offspring       
        offspring[i]=copy.deepcopy(newind)
    return newind
    
#generation loop
#for each time the mutation loops runs and creates new mutations, the generation increases, so count?

Gen = [] #a list of the generation, to plot against the fitness of the generation
avrgen= []

for x in range(0, G):
    offspring = [] #added
    selection() #withing the loop, select new parents and create offsprings
    crossover()
    mutation()
    #fits()#fitness to calculate the fitness of each generation made within the loop
    bestfit = population[0].fitness
    for i in range(0, P):
        fitnessi = copy.deepcopy(population[i].fitness)
        #print(fitnessi)
        if fitnessi < bestfit:
            bestfit = fitnessi 
    #print(bestfit)     
    
    total = 0
    for i in range(P):
       total = (total + population[i].fitness)
    #print(f"avg: {total/P}")
    
    avrgen.append(total/ P)  
    Gen.append(bestfit)#append into the list
    population= offspring


    
print(f"Minimum bestfitness in the generations: {min(Gen)}")
print(f"Lowest average in the generations: {min(avrgen)}")
plt.plot(avrgen, label = "Average fitness")
plt.plot(Gen, label = "Bestfitness")
plt.xlabel('Generation')
plt.ylabel('Fitness')
plt.legend()
plt.show()
#print(len(Gen))   
#gen_fit=0
#for x in Gen:
    #gen_fit= gen_fit + x.fits
#print(y.fitness)   
#avg_total_fit = 0 
#for i in Gen:
    #avg_total_fit= avg_total_fit + i
    
#print(avg_total_fit/G)
#plot
#xpoints = np.Gen([])
#ypoints= np.total_fit[()]
#plt.plot(fitness(),x)
#plt.show()
      
#calc total fit 
#plot
#overwrite total fitness of pop


#generation loop: fitness against generation, should i create a limited generation? maybe
#ok so x is generation, for x in range(generation) run functions
#for each generations fitness plot against generation