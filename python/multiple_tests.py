from genetic_algo import genetic_optimize
from graph import plot_graph
import time
from file_handle import write_csv_file

# This tells the number of times the algorithm will run
total_no_of_iter = 10

# POP_SIZE = 2048
# MUT_PROB = 0.25
# ELITE_RATIO = 0.1
# GENERATION = 96

# final parameter
POP_SIZE = 2500
MUT_PROB = 0.11
ELITE_RATIO = 0.5
GENERATION = 50


# POP_SIZE = 1700
# MUT_PROB = 0.03
# ELITE_RATIO = 0.5
# GENERATION = 200


CSV_FILE_PATH = 'multiple_mutations.csv'

def get_average(nested_lst):
    result_list = [sum(i)/len(nested_lst) for i in zip(*nested_lst)]
    
    return result_list

def test_with_multiple_generations(domain, schedule_cost):
    # This is for seeing the costs with different generation for Genetic Algorithm
    
    # all_gen_cost_lst = []
    # all_gen_time_lst = []
    
    for num in range(1, total_no_of_iter + 1):
        print(f'\n Iteration {num} / {total_no_of_iter}: \n')
        print(f' gen,     cost,       time')

        sol, sol_cost, n = genetic_optimize(domain, schedule_cost,
                                        popsize=POP_SIZE, mut_prob=MUT_PROB,
                                        elite_ratio=ELITE_RATIO, n=250)

        print('--------------------')
        

'''
def test_with_multiple_generations(domain, schedule_cost):
    # This is for seeing the costs with different generation for Genetic Algorithm
    
    all_gen_cost_lst = []
    all_gen_time_lst = []
    
    for num in range(1, total_no_of_iter + 1):
        print(f'\n Iteration {num} / {total_no_of_iter}: \n')
        print(f' gen,     cost,       time')

        gen_cost_lst = []
        gen_time_lst = []
        gen_lst = []

        gen_counter = 50
        while gen_counter <= 250:
            # store starting time
            begin = time.time()

            sol, sol_cost, n = genetic_optimize(domain, schedule_cost,
                                        popsize=POP_SIZE, mut_prob=MUT_PROB,
                                        elite_ratio=ELITE_RATIO, n=gen_counter)
            
            time.sleep(1)
            # store end time
            end = time.time()

            time_diff = end - begin


            print(f'    {gen_counter},      {sol_cost},     {time_diff}')

            # write to csv file
            #write_csv_file(CSV_FILE_PATH, [POP_SIZE, MUT_PROB, ELITE_RATIO, gen_counter, sol_cost, time_diff])


            gen_lst.append(gen_counter)
            gen_cost_lst.append(sol_cost)
            gen_time_lst.append(time_diff)
            
            #gen_counter += 100
            gen_counter += 50
        
        all_gen_cost_lst.append(gen_cost_lst)
        all_gen_time_lst.append(gen_time_lst)

        print('---------------------')
    
    print('\n -------- Average costs and time --------- \n')
    average_costs = get_average(all_gen_cost_lst)
    average_time = get_average(all_gen_time_lst)


    column_names = ['Generation', 'Average Cost', 'Average time(in seconds)']
    print(f'Gen,     Avg Cost,      Avg time(s)')
    for indx in range(len(average_costs)):
        # write to csv file
        rounded_average_cost = round(average_costs[indx], 3)
        rounded_average_time = round(average_time[indx], 3)
        write_csv_file(CSV_FILE_PATH, [gen_lst[indx], rounded_average_cost, rounded_average_time], column_names)
        
        print(f'{gen_lst[indx]},      {rounded_average_cost},        {rounded_average_time}')


    # plot graph and save
    plot_graph(x_lst=gen_lst, y_lst=average_costs, title="Genetic Algorithm: Generation vs Costs", x_label="Generation", y_label="costs depending on generation", filename='multiple_generations')
'''


# Average of 10 iteration: 8.8
# Popsize = 3000, MUT_PROB = 0.25, ELITE_RATIO = 0.1, GENERATION = 50
def test_with_multiple_population(domain, schedule_cost):
    # This is for seeing the costs with different population size for Genetic Algorithm

    all_popsize_cost_lst = []
    all_popsize_time_lst = []

    for num in range(1, total_no_of_iter + 1):
        print(f'\n Iteration {num} / {total_no_of_iter}: \n')
        print(f' pop,     cost,       time')

        popsize_cost_lst = []
        popsize_lst = []
        popsize_time_lst = []

        popsize_counter = 500
        while popsize_counter <= 2500:
            # store starting time
            begin = time.time()

            sol, sol_cost, n = genetic_optimize(domain, schedule_cost,
                                        popsize=popsize_counter, mut_prob=MUT_PROB,
                                        elite_ratio=ELITE_RATIO, n=GENERATION)


            time.sleep(1)
            # store end time
            end = time.time()

            time_diff = end - begin

            print(f'    {popsize_counter},      {sol_cost},     {time_diff}')

            # write to csv file
            #write_csv_file(CSV_FILE_PATH, [popsize_counter, MUT_PROB, ELITE_RATIO, GENERATION, sol_cost, time_diff])

            popsize_lst.append(popsize_counter)
            popsize_cost_lst.append(sol_cost)
            popsize_time_lst.append(time_diff)
            
            popsize_counter += 500

        all_popsize_cost_lst.append(popsize_cost_lst)
        all_popsize_time_lst.append(popsize_time_lst)

        print('---------------------')
    

    print('\n -------- Average costs and time --------- \n')
    average_costs = get_average(all_popsize_cost_lst)
    average_time = get_average(all_popsize_time_lst)


    column_names = ['Population', 'Average Cost', 'Average time(in seconds)']
    print(f'Pop,     Avg Cost,      Avg time(s)')
    for indx in range(len(average_costs)):
        # write to csv file
        rounded_average_cost = round(average_costs[indx], 3)
        rounded_average_time = round(average_time[indx], 3)
        
        write_csv_file(CSV_FILE_PATH, [popsize_lst[indx], rounded_average_cost, rounded_average_time], column_names)
        
        print(f'{popsize_lst[indx]},      {rounded_average_cost},        {rounded_average_time}')


    # plot graph and save
    plot_graph(x_lst=popsize_lst, y_lst=average_costs, title="Genetic Algorithm: Population Size vs Costs", x_label="Population Size", y_label="costs depending on population size", filename='multiple_populations')
    



def test_with_multiple_mut_prob(domain, schedule_cost):
    # This is for seeing the costs with different mutation probability for Genetic Algorithm

    all_mut_cost_lst = []
    all_mut_time_lst = []
    
    for num in range(1, total_no_of_iter + 1):
        print(f'\n Iteration {num} / {total_no_of_iter}: \n')
        print(f' mut_prob,     cost,       time')

        mut_cost_lst = []
        mut_lst = []
        mut_time_lst = []

        mut_counter = 0.01
        while mut_counter <= 0.26: 
            # store starting time
            begin = time.time()

            sol, sol_cost, n = genetic_optimize(domain, schedule_cost,
                                        popsize=POP_SIZE, mut_prob=mut_counter,
                                        elite_ratio=ELITE_RATIO, n=GENERATION)
            
            time.sleep(1)
            # store end time
            end = time.time()

            time_diff = end - begin

            print(f'    {mut_counter},      {sol_cost},     {time_diff}')

            # write to csv file
            #write_csv_file(CSV_FILE_PATH, [POP_SIZE, mut_counter, ELITE_RATIO, GENERATION, sol_cost, time_diff])

            mut_lst.append(mut_counter)
            mut_cost_lst.append(sol_cost)
            mut_time_lst.append(time_diff)
            
            mut_counter += 0.05
        
        all_mut_cost_lst.append(mut_cost_lst)
        all_mut_time_lst.append(mut_time_lst)

        print('---------------------')

    print('\n -------- Average costs and time --------- \n')
    average_costs = get_average(all_mut_cost_lst)
    average_time = get_average(all_mut_time_lst)

    column_names = ['Mutation Probability', 'Average Cost', 'Average time(in seconds)']
    print(f'Mut,     Avg Cost,      Avg time(s)')
    for indx in range(len(average_costs)):
        # write to csv file
        rounded_average_cost = round(average_costs[indx], 3)
        rounded_average_time = round(average_time[indx], 3)
        
        write_csv_file(CSV_FILE_PATH, [mut_lst[indx], rounded_average_cost, rounded_average_time], column_names)
        
        print(f'{mut_lst[indx]},      {rounded_average_cost},        {rounded_average_time}')

    
    # plot graph and save
    title = "Genetic Algorithm: Mutation Probability vs Costs"
    x_label = "Mutation Probability"
    y_label = "costs depending on mutation probability"
    plot_graph(x_lst=mut_lst, y_lst=average_costs, title=title, x_label=x_label, y_label=y_label, filename='multiple_mut_prob')
    


def test_with_multiple_elite_ratio(domain, schedule_cost):
    all_elite_cost_lst = []
    all_elite_time_lst = []
    
    for num in range(1, total_no_of_iter + 1):
        print(f'\n Iteration {num} / {total_no_of_iter}: \n')
        print(f' elite,     cost,       time')


        elite_cost_lst = []
        elite_lst = []
        elite_time_lst = []

        elite_counter = 0.1
        while elite_counter <= 0.9:

            # store starting time
            begin = time.time()

            sol, sol_cost, n = genetic_optimize(domain, schedule_cost,
                                        popsize=POP_SIZE, mut_prob=MUT_PROB,
                                        elite_ratio=elite_counter, n=GENERATION)
            
            time.sleep(1)
            # store end time
            end = time.time()

            time_diff = end - begin

            print(f'    {round(elite_counter, 3)},      {sol_cost},     {time_diff}')

            # write to csv file
            # write_csv_file(CSV_FILE_PATH, [POP_SIZE, MUT_PROB, elite_counter, GENERATION, sol_cost, time_diff])


            elite_lst.append(elite_counter)
            elite_cost_lst.append(sol_cost)
            elite_time_lst.append(time_diff)
            
            elite_counter += 0.2
        
        all_elite_cost_lst.append(elite_cost_lst)
        all_elite_time_lst.append(elite_time_lst)

        print('---------------------')

    print('\n -------- Average costs and time --------- \n')
    average_costs = get_average(all_elite_cost_lst)
    average_time = get_average(all_elite_time_lst)

    column_names = ['Elite Ratio', 'Average Cost', 'Average time(in seconds)']
    print(f'Elite,     Avg Cost,      Avg time(s)')
    for indx in range(len(average_costs)):
        # write to csv file
        rounded_average_cost = round(average_costs[indx], 3)
        rounded_average_time = round(average_time[indx], 3)
        
        write_csv_file(CSV_FILE_PATH, [elite_lst[indx], rounded_average_cost, rounded_average_time], column_names)
        
        print(f'{elite_lst[indx]},      {rounded_average_cost},        {rounded_average_time}')


    # plot graph and save
    title = "Genetic Algorithm: Elite Ratio vs Costs"
    x_label = "Elite Ratio"
    y_label = "costs depending on elite ratio"
    plot_graph(x_lst=elite_lst, y_lst=average_costs, title=title, x_label=x_label, y_label=y_label, filename='multiple_elite_ratio')
    

    


# Average of 10 iteration: 8.6; Min cost:  8
def test_with_multiple_iterations(domain, schedule_cost):
    genetic_optimize_costs_lst = []
    iteration_num_lst = []

    for num in range(1, total_no_of_iter + 1):
        print(f'\nIteration {num} / {total_no_of_iter}: \n')
        
        sol, sol_cost, n = genetic_optimize(domain, schedule_cost,
                                    popsize=POP_SIZE, mut_prob=MUT_PROB,
                                    elite_ratio=ELITE_RATIO, n=GENERATION)
        
        print('cost: ', sol_cost)

        iteration_num_lst.append(num)
        genetic_optimize_costs_lst.append(sol_cost)

    # getting average and min costs
    genetic_avg = sum(genetic_optimize_costs_lst)/len(genetic_optimize_costs_lst)
    print("Average of {} iteration: {}".format(total_no_of_iter, genetic_avg))

    min_cost_from_iter = min(genetic_optimize_costs_lst)
    print("Min cost: ", min_cost_from_iter)

    # plot graph and save
    plot_graph(x_lst=iteration_num_lst, y_lst=genetic_optimize_costs_lst, title="Genetic Algorithm", x_label="no of iterations", y_label="costs", filename='multiple_iterations')


if __name__ == '__main__':
    # mulitple generation result
    # with population size 1700
    # mutation probability = 0.25
    # elite raio = 0.1

    # costs = [
    #     [10, 10, 10, 10, 10],
    #     [8, 8, 8, 8, 8],
    #     [10, 10, 10, 10, 10],
    #     [10, 10, 10, 10, 10],
    #     [8, 8, 8, 8, 8],
    #     [8, 8, 8, 8, 8],
    #     [8, 8, 8, 8, 8],
    #     [12, 12, 12, 12, 12],
    #     [8, 8, 8, 8, 8],
    #     [8, 8, 8, 8, 8],
    # ]

    # time = [
    #     [80.8660638332367, 161.4291741847992, 242.2736370563507, 324.7921440601349, 405.6109471321106],
    #     [86.08917498588562, 168.00921416282654, 250.22483706474304, 333.23261618614197, 414.80256938934326],
    #     [78.69724416732788, 161.3247241973877, 246.343092918396, 327.0176639556885, 408.06141996383667],
    #     [79.21017980575562, 160.41059398651123, 240.20571184158325, 321.06329703330994, 400.7412610054016],
    #     [80.64266920089722, 160.82655692100525, 241.96409010887146, 324.5357620716095, 405.4657301902771],
    #     [80.64799213409424, 162.8949110507965, 243.98874020576477, 325.65296506881714, 408.25901103019714],
    #     [83.83998894691467, 166.2589988708496, 250.05240178108215, 335.41282773017883, 421.65538001060486],
    #     [85.26930403709412, 171.09963083267212, 255.6997320652008, 336.31591510772705, 419.6387388706207],
    #     [83.02753710746765, 174.97867894172668, 266.77037525177, 356.705628156662, 450.05363297462463],
    #     [87.46368622779846, 175.32150506973267, 260.44370317459106, 346.2401821613312, 430.62544894218445],
    # ]

    # avg costs:  [9.0, 9.0, 9.0, 9.0, 9.0]
    # avg time:  [82.57538404464722, 166.25539882183074, 249.79663214683532, 333.0969001531601, 416.4914139509201]




    # with population size 1024
    # mutation probability = 0.25
    # elite raio = 0.1
    costs = [
        [10, 10, 10, 10, 10],
        [10, 10, 10, 10, 10],
        [10, 10, 10, 10, 10],
        [10, 10, 10, 10, 10],
        [10, 10, 10, 10, 10],
        [10, 10, 10, 10, 10],
        [12, 10, 10, 10, 10],
        [10, 10, 10, 10, 10],
        [8, 8, 8, 8, 8],
        [12, 12, 12, 12, 12]
    ]

    time = [
        [53.067546129226685,105.32186698913574,156.91716027259827,209.58383417129517,260.500773191452],
        [48.841296911239624,99.85183882713318,150.71128606796265,201.90972805023193,253.55273699760437],
        [50.60228490829468,104.56625986099243,155.5186219215393,206.90059900283813,258.82944989204407],
        [51.72835612297058, 105.23974990844727,160.7707781791687,212.56723308563232,265.2596092224121],
        [52.62678289413452,105.75621199607849,157.723130941391,210.21576976776123,262.2023718357086],
        [54.331494092941284,111.49562120437622,162.81883001327515,213.05765914916992, 264.4934070110321],
        [50.97555708885193,108.77151417732239,162.28308701515198,219.71455717086792,278.35750818252563],
        [51.85524606704712,105.30560207366943,158.21073627471924,210.90447211265564,268.5050492286682],
        [57.558557987213135,113.31611609458923,167.27976512908936,222.54182887077332,275.3733699321747],
        [52.750272035598755,105.70203495025635, 158.6443190574646,211.31386280059814,265.3457248210907]
    ]

    # lst = get_average([[2,5,7,9], [3,3,5,6], [2,2,9,3]])
    # print(lst)
    average_costs = get_average(costs)
    average_time = get_average(time)
    print('avg costs: ', average_costs)
    print('avg time: ', average_time)

    #avg costs:  [10.2, 10.0, 10.0, 10.0, 10.0]
    #avg time:  [52.43373942375183, 106.53268160820008, 159.087771487236, 211.87095441818238, 265.24200003147126]
   


    gen_lst = [50, 100, 150, 200, 250]
    plot_graph(x_lst=gen_lst, y_lst=average_costs, title="Genetic Algorithm: Generation vs Costs", x_label="Generation", y_label="costs depending on generation", filename='multiple_generations')
