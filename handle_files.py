import csv

def get_time():
    with open('functional_files/time.txt', 'r') as time_file:
        read_time = time_file.read()
        if read_time == '':
            current_time = 0
        else:
            current_time = int(read_time)
    return current_time

def write_to_time(new_time):
    with open('functional_files/time.txt', 'w') as time_file:
        time_file.write(new_time)
    pass

def format_prices(price):
    return "{:.2f}".format(price)

def get_balance():
    with open('balance.csv', mode='r') as balance:
        balance_per_day = list(csv.DictReader(balance))
    return balance_per_day

def add_day_to_balance(balance_day):
    with open('balance.csv', mode='a', newline = '') as write_balance: 
        fieldnames = ['date', 'cost', 'revenue']
        balance_writer = csv.DictWriter(write_balance, fieldnames=fieldnames)
        balance_writer.writerow(balance_day)
    pass

def overwrite_balance(balance):
    with open('balance.csv', mode='w', newline = '') as write_balance: 
        balance_writer = csv.DictWriter(write_balance, fieldnames=balance[0].keys())
        balance_writer.writeheader()
        balance_writer.writerows(balance)
    pass

def get_stock_items():
    with open('inventory.csv', mode='r') as stock:
        stock_items = list(csv.DictReader(stock))
    return stock_items

def add_record_to_stock(stock_item):
    with open('inventory.csv', mode='a', newline = '') as write_stock:
        fieldnames = ['id', 'date_of_purchase', 'product_name', 'quantity', 'price', 'expiration_date'] 
        stock_writer = csv.DictWriter(write_stock, fieldnames=fieldnames)
        stock_writer.writerow(stock_item)
    pass

def overwrite_stock(stock_items):
    with open('inventory.csv', mode='w', newline = '') as write_stock: 
        stock_writer = csv.DictWriter(write_stock, fieldnames=stock_items[0].keys())
        stock_writer.writeheader()
        stock_writer.writerows(stock_items)
    pass

def get_sale_record():
    with open('sale_record.csv', mode='r') as record:
        sale_record = list(csv.DictReader(record))
    return sale_record

def add_sale_to_record(sale_item):
    with open('sale_record.csv', mode='a', newline = '') as write_sale:
        fieldnames = ['id', 'product_name', 'inventory_id', 'price', 'quantity', 'sale_date'] 
        stock_writer = csv.DictWriter(write_sale, fieldnames=fieldnames)
        stock_writer.writerow(sale_item)
    pass

def overwrite_sale_record(record):
    with open('sale_record.csv', mode='w', newline = '') as write_stock: 
        sale_writer = csv.DictWriter(write_stock, fieldnames=record[0].keys())
        sale_writer.writeheader()
        sale_writer.writerows(record)
    pass

def get_expired_record():
    with open('expired_products.csv', mode='r') as record:
        expired_record = list(csv.DictReader(record))
    return expired_record

def overwrite_expired_record(record):
    with open('expired_products.csv', mode='w', newline = '') as write_expired: 
        expired_writer = csv.DictWriter(write_expired, fieldnames=record[0].keys())
        expired_writer.writeheader()
        expired_writer.writerows(record)
    pass