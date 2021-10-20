from dates import get_formatted_date, get_valid_date_report
from handle_files import format_prices, get_balance
from rich.console import Console
from style_print_statements import custom_style

console = Console(theme=custom_style)

def report_on_balance(report_type, date):
    '''
    Description: this function can be called on from the command_line and will report the profit or the revenue on a given day, depending on the report_type
    '''
    balance = get_balance()
    date = str(get_valid_date_report(date))
    formatted_date = get_formatted_date(date)
    relevant_days = []
    for day in balance:
        if date == day['date']:
            relevant_days.append(day)
    if report_type == 'revenue':
        if len(relevant_days) == 0:
            console.print(f'there\'s no revenue for {formatted_date}')
        else:
            revenue = 0
            for day in relevant_days:
                revenue += float(day['revenue'])
            revenue = format_prices(revenue)
            console.print(f'the revenue for {formatted_date} is [positive]€ {revenue}[/]')
    elif report_type == 'profit':
        if len(relevant_days) == 0:
            console.print(f'there\'s no profit for {formatted_date}')
        else:
            profit = 0
            for day in relevant_days:
                profit += float(day['revenue'])
                profit -= float(day['cost'])
            profit = format_prices(profit)
            if float(profit) > 0:
                console.print(f'the profit for {formatted_date} is [positive]€ {profit}[/]')
            else:
                console.print(f'the profit for {formatted_date} is [negative]€ {profit}[/]')
    else:
        console.print('Please specify what kind of report you\'d like to see: [product_name]revenue[/] or [product_name]profit[/] with the --report or -r flag')
    pass
