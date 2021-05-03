from file_handle import get_data_from_file
from sample_data import sample_data
from prepare_data import get_all_courses_timeblocks, faculty_time_dic, faculty_course_dic
from domain import get_domain
from solution import get_solution
import globals_var

import random
import copy

def schedule_cost(sol):
    # print('constraints')
    # print(globals_var.global_constraints_dic)

    cost = 0

    # eg. {'CMPT 100': 'C'}
    course_time_dic = {}

    time_blocks = copy.deepcopy(globals_var.global_all_time_blocks) 
    for indx in range(len(sol)):
        time_block_indx = sol[indx]

        # eg. C
        time_code = time_blocks[time_block_indx]
        
        # eg. CMPT 100
        course_code = globals_var.global_all_courses[indx][0]

        course_time_dic[course_code] = time_code

        # Remove this block
        del time_blocks[time_block_indx]

    # print(course_time_dic)
    # print('\n')

    time_blocks = copy.deepcopy(globals_var.global_all_time_blocks) 
    
    for indx in range(len(sol)):
        time_block_indx = sol[indx]
        time_code = time_blocks[time_block_indx]
        # print('time code')
        # print(time_code)
        # print('\n')

        # faculty name
        name = globals_var.global_all_courses[indx][1]
        priority = get_priority(time_code, name)

        if priority == 1:
            # first preference
            cost += 0
        elif priority == 2:
            # second preference
            cost += 1
        else:
            # third preference
            # priority = 3
            cost += 2


        if (indx != (len(sol) - 1)):
            # not the last index
            # check each ith course vs all other course starting at i + 1
            for another_indx in range(indx+1, len(sol)):
                value = check_constraint(indx, another_indx, course_time_dic)
                if value == -1:
                    # meaning it's a hard constraint.
                    # two courses cannot overlap but they overlap
                    # so assign maximum number
                    # no need to check other indexes. Can return
                    return globals_var.global_max_int
                
                if value == 2:
                    # meaning it's a soft constraint.
                    # two courses are not preferred to be overlapped but they overlap
                    # so add penalty (2 points)
                    cost += 2
                
                else:
                    # no penalty for constraints
                    cost += 0
   
        # Remove this block
        del time_blocks[time_block_indx]

    return cost


def check_constraint(first_indx, second_indx, course_time_dic):
    first_course = globals_var.global_all_courses[first_indx][0]
    second_course = globals_var.global_all_courses[second_indx][0]

    dic_key = None
    if first_course < second_course:
        dic_key = (first_course, second_course)
    else:
        dic_key = (second_course, first_course)

    # if (first_course, second_course) in dictionary of constraints
    if dic_key in globals_var.global_constraints_dic:
        first_course_time_code = course_time_dic[first_course]
        second_course_time_code = course_time_dic[second_course]

        # print(first_course_time_code, second_course_time_code)
        
        first_time_obj = get_time_obj(first_course_time_code)
        second_time_obj = get_time_obj(second_course_time_code)
        
        # check overlap
        is_overlapped = check_overlap(first_time_obj, second_time_obj)

        if is_overlapped and globals_var.global_constraints_dic[dic_key] == -1:
            # this is hard constraint
            # this means that two courses cannot overlap but they overlap
            
            return -1

        elif is_overlapped and globals_var.global_constraints_dic[dic_key] == 2:
            # this is soft constraint
            # this means that two courses are not preferred to be overlapped but they overlap
            
            return 2
    
    return 0


def get_time_obj(code):
    for time_obj in globals_var.global_all_time_blocks_arr:
        if time_obj['code'] == code:
            return time_obj

def check_overlap(first_time_obj, second_time_obj):
    # print(first_time_obj)
    # print('\n')
    # print(second_time_obj)
    # print('---end---')

    first_day_lst = first_time_obj['dayArr']
    second_day_lst = second_time_obj['dayArr']

    if check_at_least_one_element_same(first_day_lst, second_day_lst):
        # at least one day is common
        # check for common num

        first_time_lst = first_time_obj['numArr']
        second_time_lst = second_time_obj['numArr']
       
        if check_at_least_one_element_same(first_time_lst, second_time_lst):
            # two time blocks overlap
            return True

    return False



def check_at_least_one_element_same(lst1, lst2):
    check =  any(item in lst1 for item in lst2)
    return check
    



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
            

def create_constraints_dic(constraints_data):
    new_constraints_data = {}
    for course_constraint in constraints_data:
        course_1 = course_constraint['course_1']
        course_2 = course_constraint['course_2']
        constraint_type = course_constraint['type']
        
        constraint_val = None
        if constraint_type == 'hard':
            constraint_val = -1
        else:
            constraint_val = 2
        
        new_constraints_data[(course_1, course_2)] = constraint_val

    return new_constraints_data

'''
if __name__ == "__main__":
    print('running cost.py')

    obj = get_data_from_file('schedule.json')

    constraints_data = get_data_from_file('student_constraint.json')

    # creating dictionary of constraints
    global global_constraints_dic 
    global_constraints_dic = create_constraints_dic(constraints_data)
        
    print(global_constraints_dic)
    print('-----------')

    global global_all_data
    global_all_data = sample_data
    

    all_time_blocks, all_faculty_courses = get_all_courses_timeblocks(sample_data)
   
    # global global_all_courses
    # global_all_courses = all_faculty_courses

    global global_all_time_blocks
    global_all_time_blocks = all_time_blocks

    global global_all_courses
    global_all_courses = all_faculty_courses

    domain_lst = get_domain(all_time_blocks, all_faculty_courses, faculty_course_dic, faculty_time_dic)
    # print(domain_lst)

    sol = get_solution(domain_lst)
    print(sol)

    
    schedule_cost(sol)
'''
