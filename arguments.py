import argparse

parser = argparse.ArgumentParser()

parser.add_argument("action", nargs="?", type=str, help="specify which action you want to take: options are 'buy', 'sell', 'report_inventory', 'balance_report', 'report_expired', 'report_on_profit' or 'advance_time'")
parser.add_argument("--name", "-n", type=str, help="specify the name of the product you want to buy or sell")
parser.add_argument("--date", "-d", action="store", default="today", type= str, help="provide the date of transaction or the report, the default is set to today")
parser.add_argument("--expiration", "-e", action="store", default="two_weeks_ahead", type= str, help="provide the expiration date of the product, the default is set to two weeks from today")
parser.add_argument("--price", "-p", type=float, help = "specify the price of the product bought or sold")
parser.add_argument("--quantity", "-q", action="store", default=1, type=int, help = "specify the quantity of the product bought or sold, if none is provided, the default is set to 1")
parser.add_argument("--time", "-t", type=int, default=0, help="specify the number of days you would like to advance the program by")
parser.add_argument("--report", "-r", type=str, default='',help="specify the type of report you'd like to recieve: options are 'revenue' or 'profit'")

args = parser.parse_args()
