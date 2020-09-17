import random
 
def get_fitness(guess, target):
    return sum(1 for expected, actual in zip(target, guess) if expected == actual)
 
def gen_individual(length):
    genes = []
    while len(genes) < length:
        sampleSize = min(length - len(genes), len(geneSet))
        genes.extend(random.sample(geneSet, sampleSize))
 
    return ''.join(genes)
 
def display(guess, target):
    fitness = get_fitness(guess, target)
    print('{}\t{} '.format(guess, fitness))
 
def mutate(parent):
    index = random.randrange(0, len(parent))
    childGenes = list(parent)
    newGene, alternate = random.sample(geneSet, 2)
    childGenes[index] = alternate if newGene == childGenes[index] else newGene
 
    return ''.join(childGenes)
 
def reproduce(x,y):
    n = len(x)
    c = random.randint(1,n-2)
    indi = x[:c] + y[c:]
    return indi

def roulette(population):
    #select 2 from population
    a = []
    for i in range(len(population)):
        pofi=population[i]

#fitness list
def random_selection_index(fitness):
    sum_fitness = 0
    acc_fitness = []
    for i in fitness:
        sum_fitness += i
        acc_fitness.append(sum_fitness)

    rou = random.randint(1,sum_fitness)
    i= 0
    while rou > acc_fitness[i]:
        i+=1
    return i

def GA(population, fitness_values, target,max_iteration):
    
    maxfit = 0
    maxind = 0
    for i in range(max_iteration):
        new_population = []
        new_fitness = []
        
        for i in range(len(population)):
            x = random_selection_index(fitness_values)
            y = random_selection_index(fitness_values)
            child = reproduce(population[x],population[y])
            if random.randint(1,10) < 2:
                child = mutate(child)
            new_population.append(child)
            new_fitness.append(get_fitness(child, target))
        
        population = new_population
        fitness = new_fitness
        best_fitness = max(new_fitness)
    
        #display(new_population[fitness.index(best_fitness)],target, i)
        if best_fitness >= len(child):
            break
    print(new_population[fitness.index(best_fitness)],' ',
              fitness[best_fitness],' ',target,' ',i, 'th')
    individual = new_population[fitness.index(best_fitness)]
    return individual
    
geneSet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!.'
target='Python.is.fun'
popu = []
fitness_values = []
num_population = 200
max_iteration = 5000
for i in range(num_population):
    ind = gen_individual(len(target))
    popu.append(ind)
    fitness_values.append(get_fitness(ind,target))
GA(popu, fitness_values, target, max_iteration)
