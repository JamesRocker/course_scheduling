import sys

def initialize():
    # eg. {('CHEM 303', 'CHEM 303 Lab'): -1, ('CHEM 303', 'CHEM 306'): -1, ('CHEM 303', 'CMPT 250'): -1, ('CHEM 303', 'CMPT 355'): -1, ('CHEM 303', 'CMPT 243'): 2}
    # -1 = hard constraint, 2 = soft constraint
    global global_constraints_dic

    # data we get from schedule json file
    global global_all_data

    # eg. [('CHEM 303', 'DRM'), ('CHEM 306', 'DRM'), ('CHEM 303 Lab', 'DRM'), ('CMPT 243', 'MB'), ('CMPT 250', 'SH')]
    global global_all_courses

    # eg. ['B', 'C', 'D', 'G_1', 'J_1', 'L', 'M', 'N', 'CC', 'S', 'U', 'X']
    global global_all_time_blocks

    # eg. [{'numArr': [1, 2], 'timeFrom': '09:00', 'timeTo': '10:00', 'dayArr': ['M', 'W', 'F'], 'code': 'A'}, {'numArr': [3, 4], 'timeFrom': '10:00', 'timeTo': '11:00', 'dayArr': ['M', 'W', 'F'], 'code': 'B'}]
    # data we get from all_time_blocks json file
    global global_all_time_blocks_arr

    # maximum int for solution where two or more courses overlap and are hard constraint
    global global_max_int 

    

    global_constraints_dic = {}
    global_all_data = []
    global_all_courses = []
    global_all_time_blocks = []
    global_all_time_blocks_arr = []
    global_max_int = sys.maxsize