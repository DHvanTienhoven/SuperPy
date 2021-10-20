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

def get_balance():
    '''
    Description: this function will get the information stored in the balance and return it as a list of dictionaries, where each dictionary represents a day
    '''
    with open('functional_files/balance.csv', mode='r') as balance:
        balance_per_day = list(csv.DictReader(balance))
    return balance_per_day

def update_balance(balance):
    '''
    Description: this function will update the balance and is called on when a purchase or a sale is made
    '''
    with open('functional_files/balance.csv', mode='w', newline = '') as write_balance: 
        balance_writer = csv.DictWriter(write_balance, fieldnames=balance[0].keys())
        balance_writer.writeheader()
        balance_writer.writerows(balance)
    pass

def get_stock_items():
    '''
    Description: this function will get the information in the inventory of the supermarket and return it as a list of dictionaries. Where each dictionairy represents a product with the same name, purchase date, purchase price and expiration date.
    '''
    with open('functional_files/inventory.csv', mode='r') as stock:
        stock_items = list(csv.DictReader(stock))
    return stock_items

def update_stock(stock_items):
    '''
    Description: this function will update the inventory when a purchase or a sale is made
    '''
    with open('functional_files/inventory.csv', mode='w', newline = '') as write_stock: 
        stock_writer = csv.DictWriter(write_stock, fieldnames=stock_items[0].keys())
        stock_writer.writeheader()
        stock_writer.writerows(stock_items)
    pass

def get_sale_record():
    '''
    Description: this function will read the information from the sale record and return it as a list of dictionaries, where each dictionary represents a product sold
    '''
    with open('functional_files/sale_record.csv', mode='r') as record:
        sale_record = list(csv.DictReader(record))
    return sale_record

def update_sale_record(record):
    '''
    Description: this function will update the sale record and is called on when a sale is made
    '''
    with open('functional_files/sale_record.csv', mode='w', newline = '') as write_stock: 
        sale_writer = csv.DictWriter(write_stock, fieldnames=record[0].keys())
        sale_writer.writeheader()
        sale_writer.writerows(record)
    pass

''''def get_expired_record():
    with open('expired_products.csv', mode='r') as record:
        expired_record = list(csv.DictReader(record))
    return expired_record

def overwrite_expired_record(record):
    with open('expired_products.csv', mode='w', newline = '') as write_expired: 
        expired_writer = csv.DictWriter(write_expired, fieldnames=record[0].keys())
        expired_writer.writeheader()
        expired_writer.writerows(record)
    pass
'''