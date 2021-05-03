from sample_data import sample_data
from prepare_data import get_all_courses_timeblocks, faculty_time_dic, faculty_course_dic
from domain import get_domain
from solution import get_solution

import random

# def mutate(sol):

#     # choose random index in the solution
#     indx = random.randint(0,len(sol)-1)
#     print(indx)

#     random_range = globals_var.global_domain[indx]
    
#     random_val = random.randint(random_range[0], random_range[1])
#     while random_val == sol[indx]:
#         random_val = random.randint(random_range[0], random_range[1])

#     sol[indx] = random_val

#     return sol

def crossover(sol_1, sol_2):
    # choose random index in the solution
    indx = random.randint(0,len(sol_1)-1)

    return sol_1[0:indx] + sol_2[indx:]


if __name__ == "__main__":
    
    # initialize global variables
    globals_var.initialize()
    
    all_time_blocks, all_courses = get_all_courses_timeblocks(sample_data)
    

    domain_lst = get_domain(all_time_blocks, all_courses, faculty_course_dic, faculty_time_dic)
    print(domain_lst)

    sol_1 = get_solution(domain_lst)
    print('sol 1')
    print(sol_1)

    sol_2 = get_solution(domain_lst)
    print('\nsol_2')
    print(sol_2)

    # modified_sol = mutate(sol_1)
    # print('\nafter crossover')
    # print(modified_sol)

    # modified_sol = crossover(sol_1, sol_2)
    # print('\nafter crossover')
    # print(modified_sol)


