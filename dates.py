from datetime import date, datetime, timedelta
from handle_files import get_time, write_to_time
from rich.console import Console

console = Console()

advance_days_by = get_time()

today = date.today() + timedelta(days=advance_days_by)

days = {
    'today': today,
    'yesterday': today - timedelta(days= 1),
    'day_before_yesterday': today - timedelta(days =2),
    'one_week_ago': today - timedelta(days =7),
    'two_weeks_ago': today - timedelta(days =14),
    'tomorrow': today + timedelta(days = 1),
    'day_after_tomorrow': today + timedelta(days = 2),
    'next_week': today + timedelta(days = 7),
    'two_weeks_ahead': today + timedelta(days = 14)}

def advance_time(number_of_days):
    if number_of_days == 0:
        print('resetting date to today')
        new_date = date.today()
        new_time = str(0)
    else:
        if number_of_days > 0:
            print(f'advancing time by {number_of_days} days')
        if number_of_days < 0:
            print(f'going back in time by {abs(number_of_days)} days')
        new_time = str(int(get_time()) + number_of_days)
        new_date = today + timedelta(days=number_of_days)
    console.print(f'the date is now {new_date}')
    write_to_time(new_time)
    pass

def get_valid_date(date_string):
    if date_string.lower() in days:
        return days[date_string.lower()]
    try:
        datetime.strptime(date_string, '%Y-%m-%d')
        return date_string
    except:
        raise ValueError('the date is not provided in a valid format, please provide date as YYYY-MM-DD')

def get_valid_date_report(date_string):
    if date_string.lower() in days:
        return str(days[date_string.lower()])
    try:
        datetime.strptime(date_string, '%Y-%m-%d')
        return date_string
    except:
        try:
            datetime.strptime(date_string, '%Y-%m')
            return date_string
        except:
            try:
                datetime.strptime(date_string, '%Y')
                return date_string
            except:    
                raise ValueError('the date is not provided in a valid format, please provide date as YYYY-MM-DD or YYYY-MM or YYYY')

def get_formatted_date(date):
    if len(date) == 10:
        formatted_date = datetime.strptime(date, '%Y-%m-%d').strftime('%d-%m-%Y')
    if len(date) == 7:
        formatted_date = datetime.strptime(date, '%Y-%m').strftime('%B of %Y')
    if len(date) == 4:
        formatted_date = f'the year {date}'
    return formatted_date

