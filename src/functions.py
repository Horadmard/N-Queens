

import random
from copy import deepcopy


def conclusion(p1, p2):

    if abs((p1[1] - p2[1])/(p1[0] - p2[0])) == 1 or (p1[1] - p2[1]) == 0:
        return True

    return False



def fitness(solution, n):

    cost = 0

    for i in range(0, n-1):
        for j in range(i+1, n):
            if conclusion(solution[i], solution[j]):
                cost += 1

    return cost



def generate_new_solution(cur_solution, n):

    new_solution = deepcopy(cur_solution)

    i = random.randint(0, n-1)
    new_solution[i][1] = random.randint(0, n-1)

    return new_solution