from sample_data import sample_data
from prepare_data import get_all_courses_timeblocks, faculty_time_dic, faculty_course_dic
from domain import get_domain
import globals_var
# from cost import get_priority

import random
import copy

def get_solution(domain):
    sol = []

    for d in domain:
        start = d[0]
        stop = d[1]

        rand_indx = random.randint(start, stop)
        sol.append(rand_indx)

    return sol


def print_solution(sol):
    time_blocks = copy.deepcopy(globals_var.global_all_time_blocks) 
    
    dash = '-' * 70

    print('\n')
    print(dash)
    print('{:<20s}{:^20s}{:>20s}'.format('Name', 'Course Code', 'Block Code'))
    print(dash)

    for indx in range(len(sol)):
        time_block_indx = sol[indx]
        time_code = time_blocks[time_block_indx]

     
        # faculty name
        name = globals_var.global_all_courses[indx][1]
        priority = get_priority(time_code, name)
        
        course_code = globals_var.global_all_courses[indx][0]
        faculty_name = globals_var.global_all_courses[indx][1]

        #print('{:<20s}{:^20s}{:>20s}{:>20s}'.format(faculty_name, course_code, time_code, priority))
        print('{}, {}, {}, {}'.format(faculty_name, course_code, time_code, priority))
        
        # Remove this block
        del time_blocks[time_block_indx]
    
    print('\n')

def get_priority(code, faculty_name):
    # print(code, faculty_name)
    for faculty in globals_var.global_all_data:
        if faculty_name == faculty['facultyName']:
            # found the right faculty 
            
            # print('\n')
            # print(faculty_name)
            # print(code)
            # print('\n')

            time_data = faculty['availableTime'][code]

            # get the priority
            priority = time_data['priority']

            return priority
   



if __name__ == "__main__":
    all_time_blocks, all_courses = get_all_courses_timeblocks(sample_data)
    

    domain_lst = get_domain(all_time_blocks, all_courses, faculty_course_dic, faculty_time_dic)
    print(domain_lst)

    sol = get_solution(domain_lst)
    print(sol)
    