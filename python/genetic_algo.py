import random
import math
import time

def genetic_optimize (domain, fitness_function,
                    popsize=100, step=1,
                    mut_prob=0.2, elite_ratio=0.2, n=100):
    # Mutation Operation
    def mutate(sol):
        # choose random index in the solution
        i=random.randint(0,len(domain)-1)

        # Roll the dice and with equal probability
        # either increase or decrease value at i by step
        if random.random()<0.5 and (sol[i] - step) >= domain[i][0]:
            return sol[0:i]+[sol[i]-step]+sol[i+1:]
        elif (sol[i]+step) <= domain[i][1]:
            return sol[0:i]+[sol[i]+step]+sol[i+1:]
        return sol

    # Crossover Operation
    def crossover(sol_1, sol_2):
        # choose random index in the solution
        indx = random.randint(0,len(sol_1)-1)

        return sol_1[0:indx] + sol_2[indx:]

    # Build the initial population of random solutions
    pop=[]
    for i in range(popsize):
        vec = [random.randint(domain[i][0],domain[i][1])
               for i in range(len(domain))]
        pop.append(vec)

    # How many winners from each generation?
    topelite=int(elite_ratio*popsize)

    # Main loop
    generations = 0

    # begin = time.time()

    # print('start of genetic algo...')  
    for i in range(n):
        # This is the list of all solutions in the population together with their fitness scores
        scores = [(fitness_function(sol_vect), sol_vect) for sol_vect in pop]
        
        # We sort this list by score
        scores.sort()

        # print(scores)

        # See what is current top best score
        if scores[0][0] == 0:
            break
        
        generations += 1
        
        # this is a list of just the solutions extracted from the sorted by score
        ranked_solutions = [sol_vect for (cost, sol_vect) in scores]

        # Build next gen population
        # Start with the pure winners
        pop = ranked_solutions[0:topelite]

        # Add mutated and bred forms of the winners
        while len(pop) < popsize:
            if random.random() < mut_prob:
                # Mutation. Select random individual from elite group and mutate
                c = random.randint(0,topelite-1)
                pop.append(mutate(ranked_solutions[c]))
            else:
                # Crossover. Select 2 random individuals from elite group and cross
                c1 = random.randint(0, topelite-1)
                c2 = random.randint(0, topelite-1)
                pop.append(crossover(ranked_solutions[c1],ranked_solutions[c2]))


        
        # store end time
        # end = time.time()

        # print every 50 generations
        # if (generations % 50 == 0):
        #     print(f'{generations},          {scores[0][0]},          {end-begin}')


        

    # print('\n')          
    # After n generations return the top scored solution from the sorted list of scores
    return (scores[0][1], scores[0][0], generations)