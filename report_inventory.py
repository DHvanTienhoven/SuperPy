from dates import get_formatted_date, get_valid_date
from handle_files import get_sale_record, get_stock_items
from rich.console import Console
from style_print_statements import create_inventory_table

console = Console()

def report_inventory(date):
    '''
    description: This function can be called directly from the commandline and will print a table of the current inventory. 
    Products that are expired or have been sold on the day of the report are excluded from the report
    '''
    date = str(get_valid_date(date))
    inventory = get_stock_items()
    sale_record = get_sale_record()
    current_inventory = []
    sold_items = {}
    for item in sale_record:
        if item['sale_date'] > date:
            if item['inventory_id'] in sold_items:
                sold_items[item['inventory_id']] += int(item[ 'quantity'])
            else:
                sold_items[item['inventory_id']]= int(item['quantity'])
    for item in inventory:
        if item['id'] in sold_items:
            item['quantity'] = int(item['quantity']) + int(sold_items[item['id']])
    for item in inventory:
        if int(item[ 'quantity']) > 0 and item['expiration_date'] > date and item['date_of_purchase'] <= date:
            current_inventory.append(item)
    inventory_table = create_inventory_table(current_inventory)
    formatted_date = get_formatted_date(date)
    console.print(f'The inventory on {formatted_date} is:', style="bold underline")
    console.print(inventory_table)
    pass
