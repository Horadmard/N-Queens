

import random

from functions import *


def hill_climbing(n):

    cur_solution = []

    for i in range(0, n):
        cur_solution.append([i, random.randint(0, n-1)])

    fit_cur = fitness(cur_solution, n)

    print('Initial Solution: ',cur_solution)
    print('Fitness: ',fit_cur)


    while(fit_cur > 0):

        new_solution = generate_new_solution(cur_solution, n)
        fit_new = fitness(new_solution, n)

        if fit_new <= fit_cur:
            cur_solution = new_solution
            fit_cur = fit_new


    print('Final Solution: ',cur_solution)
    print('Fitness: ',fit_cur)



if __name__ == '__main__':
    n = int(input('n :> '))
    hill_climbing(n)