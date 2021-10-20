from rich.table import Table
from rich.theme import Theme

def create_inventory_table(inventory):
    '''
    description: this function is called on when a report of the inventory is asked and it creates a table of the inventory, using Rich
    '''
    inventory_table = Table()
    inventory_table.add_column('Product Name', style="blue")
    inventory_table.add_column('Count', style="green", justify="center")
    inventory_table.add_column('Buy Price', justify="right")
    inventory_table.add_column('Expiration Date', justify="right", style="cyan")
    for item in inventory:
        inventory_table.add_row(item['product_name'], str(item['quantity']), '€ {price}'.format(**item), item['expiration_date'])
    return inventory_table

# The custom style is created to emphasize certain words and numbers in print statements, to improve the user-friendliness of the program

custom_style = Theme({
    'negative': 'bold red',
    'positive': 'bold green',
    'product_name': 'bold blue'
})