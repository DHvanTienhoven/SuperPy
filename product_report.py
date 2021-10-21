from dates import get_formatted_date, get_valid_date
from handle_files import get_record, update_record
from rich.console import Console
from style_print_statements import custom_style

console = Console(theme=custom_style)

def report_on_product(product_name, date):
    '''
    Description: this function can be called on from the command line and will create a report about a given produst on a given date. It will show how many of the product are in store, have been sold and are expired.
    '''
    inventory = get_record('inventory')
    date = str(get_valid_date(date))
    relevant_records = []
    id_list = []
    for item in inventory:
        if product_name == item['product_name'] and item['date_of_purchase'] <= date:
            relevant_records.append(item)
            id_list.append(item['id'])
    if len(relevant_records) == 0:
        console.print(f'no [product_name]{product_name}[/] was found')
    else:
        currently_sold = 0
        currently_in_store = 0
        currently_expired = 0
        sale_record = get_record('sale_record')
        for item in sale_record:
            if item['product_name'] == product_name and item['sale_date'] <= date and item['inventory_id'] in id_list:
                currently_sold += int(item['quantity'])
            if item['product_name'] == product_name and item['sale_date'] > date:
                currently_in_store += int(item['quantity'])
        for item in relevant_records:
            if item['expiration_date'] < date:
                currently_expired += int(item['quantity'])
            else:
                currently_in_store += int(item['quantity'])
        product_report =[{
            'currently_in_store': currently_in_store,
            'currently_sold': currently_sold,
            'currently_expired': currently_expired
        }]
        formatted_date = get_formatted_date(date)
        console.print(f'creating a report for [product_name]{product_name}[/] on {formatted_date}')
        update_record(f'reports/report_of_{product_name}_on_{date}', product_report)
    pass
