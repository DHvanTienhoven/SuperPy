from check_arguments import check_arguments
from dates import get_valid_date
from handle_files import format_prices, get_record, update_record
from rich.console import Console
from style_print_statements import custom_style

console = Console(theme=custom_style)

def update_inventory_sale(sale_items):
    '''
    Description: this function is called on when a sale is made and will remove the sold products from the inventory
    '''
    items_dict = {}
    for item in sale_items:
        items_dict[item['inventory_id']]= item['quantity']
    stock_items = get_record('inventory')
    for item in stock_items:
        if item['id'] in items_dict:
            item['quantity'] = int(item['quantity']) - int(items_dict[item['id']])
    update_record('inventory', stock_items)
    pass

def add_to_sale_record(sale_items):
    '''
    Description: this function will add the sold items to the sale record
    '''
    sale_record = get_record('sale_record')
    for item in sale_items:
        sale_record.append(item)
    update_record('sale_record', sale_record)
    pass

def add_sale_to_balance(price, quantity, sale_date):
    '''
    Description: this function will add the revenue to the balance when products are sold
    '''
    balance_day ={
        'date': sale_date,
        'cost': 0,
        'revenue': price * quantity
    }
    balance_day['cost'], balance_day['revenue'] = format_prices(balance_day['cost']), format_prices(balance_day['revenue'])
    balance_per_day = get_record('balance')
    for day in balance_per_day:
        if balance_day['date'] == day['date']:
            day['revenue'] = format_prices(float(day['revenue']) + float(balance_day['revenue']))
            update_record('balance', balance_per_day)
            return
    balance_per_day.append(balance_day)
    update_record('balance', balance_per_day)
    pass

def get_possible_products(product_name, date):
    '''
    Description: this function will filter through the inventory and return a list of possible products to sell
    '''
    stock_items = get_record('inventory')
    possible_products = []
    for item in stock_items:
        if item['product_name'] == product_name and int(item['quantity']) > 0 and item['date_of_purchase'] <= date and item['expiration_date'] > date:
            possible_products.append(item)
    return possible_products

def check_quantity(products):
    '''
    Description: this function checks how many of the desired item are currently in stock
    '''
    quantity_in_stock = 0
    for product in products:
        quantity_in_stock += int(product['quantity'])
    return quantity_in_stock

def sort_by_expiration_date(products):
    '''
    Description: this function sorts the items that can be sold by expiration date in order to sell the items that expire first before the others.
    '''
    return sorted(products, key=lambda l: l['expiration_date'])

def create_sale_items(products, quantity, price, date):
    '''
    Description: this function creates a list of one or more dictionaries for the items that will be sold
    '''
    sale_items = []
    sold_quantity = 0
    for product in products:
        if sold_quantity == quantity:
            break
        if int(product['quantity']) > quantity-sold_quantity:
                sale_item ={
                'id': '',
                'product_name': product['product_name'],
                'inventory_id': product['id'],
                'price': format_prices(price),
                'quantity': quantity-sold_quantity,
                'sale_date': date
                }
                sale_items.append(sale_item)
                sold_quantity = quantity
        else:
                sale_item ={
                'id': '',
                'product_name': product['product_name'],
                'inventory_id': product['id'],
                'price': format_prices(price),
                'quantity': product['quantity'],
                'sale_date': date
                }
                sale_items.append(sale_item)
                sold_quantity += int(product['quantity'])
    return sale_items

def add_id_to_items(sale_items):
    '''
    Description: this function will add an id to the sale items
    '''
    sale_record = get_record('sale_record')
    for i, record in enumerate(sale_items):
        record['id'] = len(sale_record) + 1 + i
    return sale_items

def sell_product(product_name, price, quantity, date):
    '''
    Description: this function can be called on from the command line and handles the sale of a product
    '''
    check_arguments(product_name, price)
    sale_date = str(get_valid_date(date))
    possible_products = get_possible_products(product_name, sale_date)
    if len(possible_products)==0:
        console.print (f'[product_name]{product_name}[/] is not in stock, the sale is not possible')
    else:
        quantity_in_stock = check_quantity(possible_products)
        if quantity_in_stock < quantity:
            console.print(f'there\'s not enough [product_name]{product_name}[/] in stock, the maximum amount of[product_name] {product_name}[/] you can sell is [positive]{quantity_in_stock}[/]' )
        else:
            console.print(f'selling [positive]{quantity}[/][product_name] {product_name}[/]')
            sorted_products = sort_by_expiration_date(possible_products)
            sale_items = create_sale_items(sorted_products, quantity, price, sale_date)
            add_id_to_items(sale_items)
            add_to_sale_record(sale_items)
            update_inventory_sale(sale_items)
            add_sale_to_balance(price, quantity, sale_date)
    pass
