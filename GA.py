import time
from fitness import fitness
import random

def GA(N):
    def fitval(tup):
        return tup[1]


    def sort():
        global qspace
        qspace = sorted(qspace, key=fitval)


    def initialize(total):
        queens = [0] * n
        qpop.clear()
        while total > 0:
            for i in range(0, n):
                queens[i] = random.randint(0, n-1)
                qpop.add(tuple(queens))
            total = total - 1
        for config in qpop:
            # print(config)
            qspace.append((config, fitness(config, start_time)))


    def genetic():
        global qspace, generations
        curgen = 0
        while generations > curgen:
            print("Generation ", curgen)
            sort()
            # print(qspace)
            qspace = qspace[:top_best]        # criterion for parent selection top 20
            qpop.clear()
            for i in range(0, top_best):
                qpop.add(qspace[i][0])
            # print("Parents: ", qspace)
            print("Best in gen: ", qspace[0])
            if curgen % random_offspring_lim == random_offspring_lim - 1:   # random offspring generation
                print("random offspring generation")
                initialize(pop_limit - top_best)
            else:
                for i in range(0, pop_limit - top_best):
                    # select random parents and cross over
                    child = [0] * n
                    parent1 = qspace[random.randint(0, top_best - 1)][0]
                    parent2 = qspace[random.randint(0, top_best - 1)][0]
                    bias = random.randrange(1, biasing_value)
                    for j in range(0, n):
                        if j % bias != 0:
                            child[j] = parent1[j]
                        else:
                            child[j] = parent2[j]
                    chance = random.randrange(0, 1)
                    if chance < mutation_probability:                             # mutation on low probability
                        child[random.randint(0, n-1)] = random.randint(0, n-1)    # change one random value by random amount
                    child = tuple(child)
                    if child not in qpop:
                        qspace.append((child, fitness(child, start_time)))
                        qpop.add(child)
            curgen = curgen + 1
            generations = generations + 1

    n = N
    initialize(pop_limit)
    genetic()
    print("---Total Time is %s seconds --" % (time.time() - start_time))


pop_limit = 100
generations = 500
top_best = 50
mutation_probability = 0.2
random_offspring_lim = 20
biasing_value = 10
qpop = set()
qspace = []
start_time = time.time()



