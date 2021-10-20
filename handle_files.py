import csv

def get_time():
    '''
    Description: this function will tell the program how many days to advance time by from the current date
    '''
    with open('functional_files/time.txt', 'r') as time_file:
        read_time = time_file.read()
        if read_time == '':
            current_time = 0
        else:
            current_time = int(read_time)
    return current_time

def write_to_time(new_time):
    '''
    Description: this function will change the number of days the program is advanced by
    '''
    with open('functional_files/time.txt', 'w') as time_file:
        time_file.write(new_time)
    pass

def format_prices(price):
    '''
    Description: this function will format all prices as a float with two decimals
    '''
    return "{:.2f}".format(price)

def get_record(file_name):
    '''
    Description: this function will read date from a csv file
    '''
    with open(f'functional_files/{file_name}.csv', mode='r') as file:
        record = list(csv.DictReader(file))
    return record

def update_record(file_name, new_list):
    '''
    Description: this function will update a record in a csv file or create one if none is present
    '''
    with open(f'functional_files/{file_name}.csv', mode='w', newline = '') as file: 
        file_writer = csv.DictWriter(file, fieldnames=new_list[0].keys())
        file_writer.writeheader()
        file_writer.writerows(new_list)
    pass