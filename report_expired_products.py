from dates import get_formatted_date, get_valid_date
from handle_files import format_prices, get_record, update_record
from rich.console import Console
from style_print_statements import custom_style

console = Console(theme=custom_style)

def report_expired(date):
    '''
        Description: this function can be called on from the command line and will create a report about the expired product on a given date. 
    '''
    inventory = get_record('inventory')
    expired_products = []
    date = str(get_valid_date(date))
    id = 0
    for item in inventory:
        
        if item['date_of_purchase'] <= date and item['expiration_date'] < date and int(item['quantity']) > 0:
            id += 1
            expired_item = {
                'id': id,
                'product_name': item['product_name'],
                'inventory_id': item['id'],
                'quantity': item['quantity'],
                'lost_cost': format_prices(int(item['quantity']) * float(item['price']))
            }
            expired_products.append(expired_item)
    formatted_date = get_formatted_date(date)
    if len(expired_products) == 0:
        console.print(f'there\'s no expired products in store on {formatted_date}! :thumbs_up:')
    else:
        console.print(f'there\'s expired products on {formatted_date}, a report will be created')
        update_record(f'reports/expired_products_on_{date}', expired_products)
    pass
