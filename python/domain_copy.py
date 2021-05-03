from sample_data import sample_data
from prepare_data import get_all_courses_timeblocks, faculty_time_dic, faculty_course_dic


def get_domain(comb_time_blocks, comb_courses, course_dic, time_dic):
    domain = []

    # start and end keep track of indexes in time blocks
    start = 0 
    end = 0
    for indx in range(len(comb_courses)):
        course = comb_courses[indx]
        
        # faculty name
        name = course[1]

        # number of lecture courses
        num_lecture = course_dic[name][0]
        # number of lab courses
        num_lab = course_dic[name][1]

        if indx == 0:
            if time_dic[name][0] > 0:
                # get index of the last lecture time block
                end = time_dic[name][0] - 1
            else:
                # get index of the last lab time block
                end = time_dic[name][1] - 1

       
        if num_lecture == 0:
            # start of lab course
            if num_lab == course_dic[name][3]:
                # if current number == original number
                # start of lab 

                # if time_dic[name][2] == 0:
                #     # no lecture blocks before the lab time blocks
                #     start = 0
                #     end = time_dic[name][1] - 1
                # else:
                
                start = end + 1
                end = (time_dic[name][1] + end)
                
                

                domain.append((start, end))
            else:
                # continuation of lab 
                domain.append((start, end))

            course_dic[name][1] -= 1
            
        else:
            # lecture course
            domain.append((start, end))
            

            course_dic[name][0] -= 1

        
            # print(indx)

        if course_dic[name][0] == 0 and course_dic[name][1] == 0 and indx != (len(comb_courses) - 1):
            # both the number of lecture courses and num of lab courses goes to 0 and this is not the last element
            # prepare for next faculty

            next_course = comb_courses[indx+1]
        
            # next faculty name
            next_name = next_course[1]

            if course_dic[next_name][2] == 0:
                # no lecture course before the lab course but there are lecture labs
                start = end + time_dic[next_name][2]
            else:
                start = end

            end = (time_dic[next_name][1] + end)
            # if course_dic[next_name][2] == 0:
                
            # else:
            #     end = (time_dic[next_name][0] + end)

            


        end -= 1

    return domain


    


if __name__ == "__main__":
    all_time_blocks, all_courses = get_all_courses_timeblocks(sample_data)
    
    print(all_time_blocks)
    print(all_courses)
    print(faculty_time_dic)
    print(faculty_course_dic)

    domain_lst = get_domain(all_time_blocks, all_courses, faculty_course_dic, faculty_time_dic)
    print(domain_lst)