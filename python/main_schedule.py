import globals_var
from file_handle import get_data_from_file, write_file
from sample_data import sample_data
from prepare_data import get_all_courses_timeblocks, faculty_time_dic, faculty_course_dic
from domain import get_domain
from solution import get_solution, print_solution
from cost import create_constraints_dic, schedule_cost, get_priority
from genetic_algo import genetic_optimize
import multiple_tests

import copy
import time

#COURSE_FILE_NAME = 'files/schedule.json'
COURSE_FILE_NAME = 'files/schedule_S2021.json'

CONSTRAINT_FILE_NAME = 'files/student_constraint1.json'
# CONSTRAINT_FILE_NAME = 'files/student_constraint_S2021.json'
# CONSTRAINT_FILE_NAME = 'files/student_constraint_S2021_copy.json'

ALL_TIME_BLOCKS_FILE_NAME = 'files/all_time_blocks.json'

OUTPUT_FILE_NAME = 'files/output_solution.json'


def structure_potential_schedule(sol):
    faculty_data_dic = {}

    time_blocks = copy.deepcopy(globals_var.global_all_time_blocks) 
   
    for indx in range(len(sol)):
        time_block_indx = sol[indx]
        time_code = time_blocks[time_block_indx]

        faculty_name = globals_var.global_all_courses[indx][1]
     
        priority = get_priority(time_code, faculty_name)
        
        course_code = globals_var.global_all_courses[indx][0]
      

        course_dic = {'courseCode': course_code, 'timeCode': time_code, 'priority': priority}
        
        if faculty_name not in faculty_data_dic:
            faculty_data_dic[faculty_name] = [course_dic]
        else:
            faculty_data_dic[faculty_name].append(course_dic)

        
        # Remove this block
        del time_blocks[time_block_indx]

    return faculty_data_dic
    


if __name__ == "__main__":

    # store starting time
    begin = time.time()

    # initialize global variables
    globals_var.initialize()

    # for testing with sample data
    #faculty_data = sample_data

    
    # READ THE COURSES FILE
    faculty_data = get_data_from_file(COURSE_FILE_NAME)

    # READ THE CONSTRAINTS FILE
    constraints_data = get_data_from_file(CONSTRAINT_FILE_NAME)

    # READ THE ALL TIME BLOCKS FILE 
    time_blocks_arr = get_data_from_file(ALL_TIME_BLOCKS_FILE_NAME)
    

    globals_var.global_all_time_blocks_arr = time_blocks_arr
    # creating dictionary of constraints
    globals_var.global_constraints_dic = create_constraints_dic(constraints_data)

    # STRUCTURE TIME AND COURSES
    # get all time blocks and faculty courses in a structured way
    # eg. Time blocks: ['A', 'C', 'G_1', 'H_3', 'AA', 'U', 'Y', 'C', 'H_3', 'I_2', 'K_3', 'BB', 'V', 'X', 'Z', 'A', 'C', 'D', 'G_1', 'H_2', 'K_2', 'L']
    # eg. Courses: [('Course 2', 'A'), ('CMPT 100', 'A'), ('Course 3', 'A'), ('Lab 1A', 'A'), ('Lab 2A', 'A'), ('MATH 100', 'B'), ('CHEM 100', 'B'), ('MATH 400', 'B'), ('Lab 3A', 'B'), ('Lab 3B', 'B'), ('BIO 200', 'C'), ('PHYS 100', 'C'), ('Course 25', 'C')]
    all_time_blocks, all_faculty_courses = get_all_courses_timeblocks(faculty_data)
    
    
    globals_var.global_all_data = faculty_data
    globals_var.global_all_courses = all_faculty_courses
    globals_var.global_all_time_blocks = all_time_blocks

    
    # print(faculty_course_dic)
    # print(faculty_time_dic)


    # DEFINE DOMAIN
    domain_lst = get_domain(all_time_blocks, all_faculty_courses, faculty_course_dic, faculty_time_dic)
    # print(domain_lst)
    # print('length of domain: ', len(domain_lst))
    
    # print(all_time_blocks)
    # print(all_faculty_courses)
    # print(domain_lst)

    
    # -----------RUN OPTIMIZATION----------------
    # population size
    #popsize = 2048
    # mutation probability
    #mut_prob = 0.25
    #elite_ratio = 0.1
    # number of generation
    #n = 10  

    '''
    #POP_SIZE = 1024
    POP_SIZE = 1700
    MUT_PROB = 0.03
    ELITE_RATIO = 0.5
    GENERATION = 200
    print("\n-----------Running Genetic algorithm----------")
    sol, sol_cost, n = genetic_optimize(domain_lst, schedule_cost,
                                popsize=POP_SIZE, mut_prob=MUT_PROB,
                                elite_ratio=ELITE_RATIO, n=GENERATION)
   
    print("Total cost after {} generations is:{}\n".format(n, sol_cost))
    print_solution(sol)


    # DECODE SOLUTION
    # will need faculty name, course code, priority, Block Code
    structured_schedule = structure_potential_schedule(sol)
    # print('structured schedule')
    # print(structured_schedule)
    # print('\n')



    # WRITE THE SOLUTION TO THE JSON FILE
    print('writing to file...')
    write_file(OUTPUT_FILE_NAME, structured_schedule)


    time.sleep(1)
    # store end time
    end = time.time()

    # total time taken
    print(f"Total time taken: {end - begin}")
    '''



    # print('\nMultiple Generations Test')
    # multiple_tests.test_with_multiple_generations(domain_lst, schedule_cost)
    
    # print('\nMultiple Population Test')
    # multiple_tests.test_with_multiple_population(domain_lst, schedule_cost)
    
    # print('\nMultiple mutation prob Test')
    # multiple_tests.test_with_multiple_mut_prob(domain_lst, schedule_cost)
    
    # print('\nMultiple elite ratio Test')
    # multiple_tests.test_with_multiple_elite_ratio(domain_lst, schedule_cost)

    # MULTIPLE TESTS
    print('Multiple iterations Test')
    multiple_tests.test_with_multiple_iterations(domain_lst,schedule_cost)