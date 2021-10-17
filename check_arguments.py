def check_arguments(product_name, price):
    if (product_name == None and price==None):
        raise AttributeError("please provide the product name with the --name or -n flag and the price with the --price or -p flag")
    if product_name == None:
        raise AttributeError("please provide the product name with the --name or -n flag")
    if price == None:
        raise AttributeError("please provide the price with the --price or -p flag")
    return 