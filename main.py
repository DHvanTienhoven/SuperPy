# Imports
from dates import advance_time
from arguments import args
from buy_product import buy_product
from report_inventory import report_inventory
from report_on_balance import report_on_balance
from sell_product import sell_product


# Do not change these lines.
__winc_id__ = 'a2bc36ea784242e4989deb157d527ba0'
__human_name__ = 'superpy'


# Your code below this line.
def main():
    pass

if args.action == "buy":
    buy_product(product_name=args.name, price=args.price, exp_date=args.expiration, quantity=args.quantity, purch_date=args.date)
if args.action == "sell":
    sell_product(product_name=args.name, price=args.price, quantity=args.quantity, date=args.date)
if args.action == "advance_time":
    advance_time(args.time)
if args.action == "report_inventory":
    report_inventory(args.date)
if args.action == "balance_report":
    report_on_balance(report_type=args.report, date=args.date)
    
if __name__ == '__main__':
    main()
