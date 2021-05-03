from file_handle import get_data_from_file
from sample_data import sample_data

ALL_LAB_BLOCKS = ["S","T","U","X","Y","Z","V","AA","BB","W","CC"]

# eg. {'A': [4, 3, 4, 3], 'B': [7, 0, 7, 0]}
# first element in list -> num of lecture time block
# second element in list -> num of lab time block
# third element in list -> num of lecture time block that will not changed
# fourth element in list -> num of lab time block that will not changed
faculty_time_dic = {}

# eg. {'A': [3, 1, 3, 1], 'B': [3, 0, 3, 0]}
# first element in list -> num of lecture course
# second element in list -> num of lab course
# third element in list -> num of lecture course that will not change
# fourth element in list -> num of lab course that will not change
faculty_course_dic = {}


# time blocks for a professor
def get_time_blocks(faculty_name, avail_time_blocks):
    lecture_blocks = []
    lab_blocks = []

    for key in avail_time_blocks:
        if key in ALL_LAB_BLOCKS:
            # this is a lab time block so put it in lab_blocks
            lab_blocks.append(key)
        else:
            # this is a lecture time block so put it in lecture_blocks
            lecture_blocks.append(key)

    sorted_lecture_blocks = sorted(lecture_blocks)
    sorted_lab_blocks = sorted(lab_blocks)

    # adding to global dic: how many lecture time blocks and lab time blocks
    faculty_time_dic[faculty_name] = [len(sorted_lecture_blocks), len(sorted_lab_blocks), len(sorted_lecture_blocks), len(sorted_lab_blocks)]

    # concatenate two lists into one so that all the lecture blocks come before lab blocks
    combination = sorted_lecture_blocks + sorted_lab_blocks

    return combination

# courses for a professor
def get_courses(faculty_name, courses):
    lecture_courses = []
    lab_courses = []

    for course_dic in courses:
        if course_dic['isLab']:
            # a course is a lab course so put it into lab_courses
            lab_courses.append((course_dic['courseCode'], faculty_name))
        else:
            # a course is a lecture course so put it into lecture_courses
            lecture_courses.append((course_dic['courseCode'], faculty_name))
    
    # adding to global dic : how many lecture course and lab course
    faculty_course_dic[faculty_name] = [len(lecture_courses), len(lab_courses), len(lecture_courses), len(lab_courses)]

    # concatenate two lists into one so that all the lecture courses come before lab courses
    combined = lecture_courses + lab_courses

    return combined


def get_all_courses_timeblocks(all_data):
    faculty_names = []
    data_dic = {}
    for faculty_data_dic in all_data:
        # assuming all faculty names are unique
        data_dic[faculty_data_dic['facultyName']] = {"courses": faculty_data_dic['courses'], "availableTime": faculty_data_dic["availableTime"]}
        faculty_names.append(faculty_data_dic['facultyName'])
    
    # sort by faculty name
    sorted_faculty_names = sorted(faculty_names)

    all_faculties_time_blocks = []
    all_faculties_courses = []
    
    for name in sorted_faculty_names:
        faculty_time_blocks = data_dic[name]['availableTime']
        faculty_courses = data_dic[name]['courses']

        # print(name)
        # print(faculty_time_blocks)
        # print(faculty_courses)
        # print('-------------------')

        # get time block and append to all time blocks
        all_faculties_time_blocks += get_time_blocks(name, faculty_time_blocks)

        # get courses and append to all courses
        all_faculties_courses += get_courses(name, faculty_courses)


    return all_faculties_time_blocks, all_faculties_courses



if __name__ == "__main__":
    #obj = get_data_from_file('schedule.json')
    # print(obj)


    # lst = ['A', 'B', 'C', 'D', 'E', 'G_1', 'G_2','G_3',"H_1","H_2","H_3","I_1","I_2","I_3","J_1","J_2","J_3","JJ", "K_1","K_2","K_3","L","M","N","O","P","Q","R","S","T","U","X","Y","Z","V","AA","BB","W","CC"]
    # print(sorted(lst))


    

    all_time_blocks, all_courses = get_all_courses_timeblocks(sample_data)
    print('combined')
    print(all_time_blocks)
    print('\n')
    print(all_courses)

    print('\n')
    print(faculty_time_dic)
    print(faculty_course_dic)


    # all_time_blocks, all_courses = get_all_courses_timeblocks(obj)
    # print('combined')
    # print(all_time_blocks)
    # print('\n')
    # print(all_courses)

