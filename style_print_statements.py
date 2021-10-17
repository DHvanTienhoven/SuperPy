from rich.table import Table
from rich.theme import Theme

def create_inventory_table(inventory):
    inventory_table = Table()
    inventory_table.add_column('Product Name', style="blue")
    inventory_table.add_column('Count', style="green", justify="center")
    inventory_table.add_column('Buy Price', justify="right")
    inventory_table.add_column('Expiration Date', justify="right", style="cyan")
    for item in inventory:
        inventory_table.add_row(item['product_name'], str(item['quantity']), '€ {price}'.format(**item), item['expiration_date'])
    return inventory_table

custom_style = Theme({
    'negative': 'bold red',
    'positive': 'bold green',
    'product_name': 'bold blue'
})