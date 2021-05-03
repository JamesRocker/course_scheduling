import json

# Import writer class from csv module
from csv import writer

import os.path

#column_names = ['popsize', 'mut_prob', 'elite_ratio', 'generation', 'cost', 'time']


def get_data_from_file(filename):

    try:
        # read file
        with open(filename, 'r') as f:
            data = f.read()
        
        # parse json file
        obj = json.loads(data)

        return obj
    
    except IOError:
        raise Exception("Cannot read the file")


def write_file(filename, obj):
    try:
        with open(filename, "w") as outfile:
            json.dump(obj, outfile)
    except IOError:
        raise Exception("Writing to file not successful")
    else:
        print ("Successfully written to the file\n")


def write_csv_file(filename, lst, column_names):
    file_path = 'files/' + filename

  
    if not os.path.isfile(file_path):
        with open(file_path, 'a', newline='') as csv_file:
            # Create a writer object from csv module
            csv_writer = writer(csv_file)

            # Add contents of list as last row in the csv file
            csv_writer.writerow(column_names)
            csv_writer.writerow(lst)
    
    else:
        # Open file in append mode
        with open(file_path, 'a', newline='') as csv_file:
            # Create a writer object from csv module
            csv_writer = writer(csv_file)

            # Add contents of list as last row in the csv file
            csv_writer.writerow(lst)


# write_csv_file('testing.csv', ['1', '2', '3', '4', '5'])