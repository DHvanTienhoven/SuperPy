from dates import get_formatted_date, get_valid_date_report
from handle_files import format_prices, get_balance
from rich.console import Console
from style_print_statements import custom_style

console = Console(theme=custom_style)


def report_revenue(date):
    balance = get_balance()
    date = get_valid_date_report(date)
    formatted_date = get_formatted_date(date)
    relevant_days = []
    for day in balance:
        if date in day['date']:
            relevant_days.append(day)
    if len(relevant_days) == 0:
        console.print(f'there\'s no revenue for {formatted_date}')
    else:
        revenue = 0
        for day in relevant_days:
            revenue += float(day['revenue'])
        revenue = format_prices(revenue)
        console.print(f'the revenue for {formatted_date} is [positive]€ {revenue}[/positive]')
    pass

def report_profit(date):
    balance = get_balance()
    date = get_valid_date_report(date)
    formatted_date = get_formatted_date(date)
    relevant_days = []
    for day in balance:
        if date in day['date']:
            relevant_days.append(day)
    if len(relevant_days) == 0:
        print(f'there\'s no profit for {formatted_date}')
    else:
        profit = 0
        for day in relevant_days:
            profit += float(day['revenue'])
            profit -= float(day['cost'])
        profit = format_prices(profit)
        if float(profit) > 0:
            console.print(f'the profit for {formatted_date} is [positive]€ {profit}[/positive]')
        else:
            console.print(f'the profit for {formatted_date} is [negative]€ {profit}[/negative]')
    pass
