from check_arguments import check_arguments
from dates import get_valid_date
from handle_files import add_day_to_balance, add_sale_to_record, format_prices, get_balance, get_sale_record, get_stock_items, overwrite_balance, overwrite_sale_record, overwrite_stock
from rich.console import Console
from style_print_statements import custom_style

console = Console(theme=custom_style)

def update_inventory_sale(sale_items):
    items_dict = {}
    for item in sale_items:
        items_dict[item['inventory_id']]= item['quantity']
    stock_items = get_stock_items()
    for item in stock_items:
        if item['id'] in items_dict:
            item['quantity'] = int(item['quantity']) - int(items_dict[item['id']])
    overwrite_stock(stock_items)
    pass

def update_sale_record(sale_items):
    sale_record = get_sale_record()
    if len(sale_record) == 0:
        overwrite_sale_record(sale_items)
    else:
        for item in sale_items:
            add_sale_to_record(item)
    pass

def update_balance_sale(price, quantity, sale_date):
    balance_day ={
        'date': sale_date,
        'cost': 0,
        'revenue': price * quantity
    }
    balance_day['cost'], balance_day['revenue'] = format_prices(balance_day['cost']), format_prices(balance_day['revenue'])
    balance_per_day = get_balance()
    for day in balance_per_day:
        if balance_day['date'] == day['date']:
            day['revenue'] = format_prices(float(day['revenue']) + float(balance_day['revenue']))
            overwrite_balance(balance_per_day)
            return None
    if len(balance_per_day) == 0:
        balance_per_day.append(balance_day)
        overwrite_balance(balance_per_day)
    else:
        add_day_to_balance(balance_day)
    pass

def get_possible_products(product_name, date):
    stock_items = get_stock_items()
    possible_products = []
    for item in stock_items:
        if item['product_name'] == product_name and int(item['quantity']) > 0 and item['date_of_purchase'] <= date and item['expiration_date'] > date:
            possible_products.append(item)
    return possible_products

def check_quantity(products):
    quantity_in_stock = 0
    for product in products:
        quantity_in_stock += int(product['quantity'])
    return quantity_in_stock

def sort_by_expiration_date(products):
    return sorted(products, key=lambda l: l['expiration_date'])

def create_sale_items(products, quantity, price, date):
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
    sale_record = get_sale_record()
    for i, record in enumerate(sale_items):
        record['id'] = len(sale_record) + 1 + i
    return sale_items

def sell_product(product_name, price, quantity, date):
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
            update_sale_record(sale_items)
            update_inventory_sale(sale_items)
            update_balance_sale(price, quantity, sale_date)
    pass
