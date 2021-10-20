from check_arguments import check_arguments
from dates import get_valid_date
from handle_files import format_prices, get_balance, get_stock_items, update_stock, update_balance
from rich.console import Console
from style_print_statements import custom_style

console = Console(theme=custom_style)

def add_to_balance(balance_day):
    '''
    Description: this function will add the total cost for a purchased product to the balance
    '''
    balance_day['cost'], balance_day['revenue'] = format_prices(balance_day['cost']), format_prices(balance_day['revenue'])
    balance_per_day = get_balance()
    for day in balance_per_day:
        if balance_day['date'] == day['date']:
            day['cost'] = format_prices(float(day['cost']) + float(balance_day['cost']))
            update_balance(balance_per_day)
            return
    balance_per_day.append(balance_day)
    update_balance(balance_per_day)
    pass


def add_to_inventory(product_item):
    '''
    Description: this function will add a bought product to the inventory of the supermarket
    '''
    product_item['price'] = format_prices(product_item['price'])
    stock_items = get_stock_items()
    for stock_item in stock_items:
        if (str(product_item['date_of_purchase']) == stock_item['date_of_purchase']
        and product_item['price'] == stock_item['price']
        and product_item['product_name'] == stock_item['product_name']
        and str(product_item['expiration_date']) == stock_item['expiration_date']):
            console.print('[product_name]{product_name}[/] with expiration date {expiration_date} is already in stock, adding [positive]{quantity}[/] to quantity'.format(**product_item))
            stock_item['quantity'] = int(stock_item['quantity']) + product_item['quantity']
            update_stock(stock_items)
            return 
    console.print('buying [product_name]{product_name}[/]'.format(**product_item))
    num_stock_items = len(stock_items)
    product_item['id'] = num_stock_items + 1
    stock_items.append(product_item)
    update_stock(stock_items)
    pass


def buy_product(product_name, price, exp_date, quantity, purch_date):
    '''
    Description: this function can be called directly from the commandline and will create dictionaries for the item bought and add them to the inventory and the balance of the supermarket
    '''
    check_arguments(product_name, price)
    expiration_date, purchase_date = get_valid_date(exp_date), get_valid_date(purch_date)
    product_item ={
        'id': '',
        'date_of_purchase': purchase_date,
        'product_name': product_name,
        'quantity': quantity,
        'price': price,
        'expiration_date': expiration_date
    }
    add_to_inventory(product_item)
    balance_day ={
        'date': str(purchase_date),
        'cost': quantity * price,
        'revenue': 0
    }
    add_to_balance(balance_day)
    pass
