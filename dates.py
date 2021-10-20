from datetime import date, datetime, timedelta
from handle_files import get_time, write_to_time
from rich.console import Console

console = Console()

advance_days_by = get_time()

# today is the variable with the date that the program percieves as today

today = date.today() + timedelta(days=advance_days_by)

# the dictionary days contains some relative dates that are dependant on today. This makes the program more user-friendly 
# as a user can add a sale from for example yesterday without looking up the date. 

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
    '''
    Description: this function can be called from the command-line and will shift the date that the program percieves as today by the number of days specified
    '''
    if number_of_days == 0:
        print('resetting date to today')
        new_date = get_formatted_date(str(date.today()))
        new_time = str(0)
    else:
        if number_of_days > 0:
            print(f'advancing time by {number_of_days} days')
        if number_of_days < 0:
            print(f'going back in time by {abs(number_of_days)} days')
        new_time = str(int(get_time()) + number_of_days)
        new_date = get_formatted_date(str(today + timedelta(days=number_of_days)))
    console.print(f'the date is now {new_date}')
    write_to_time(new_time)
    pass

def get_valid_date(date_string):
    '''
    Description: this function will check if the date a user has given in a valid format. If that's not the case it will raise a Value error.
    If the user is using one of the relative days it will return a valid date-string to work with.
    '''
    if date_string.lower() in days:
        return days[date_string.lower()]
    try:
        datetime.strptime(date_string, '%Y-%m-%d')
        return date_string
    except:
        raise ValueError('the date is not provided in a valid format, please provide date as YYYY-MM-DD')

def get_valid_date_report(date_string):
    '''
    Description: this function will check if the date a user has given in a valid format. If that's not the case it will raise a Value error.
    It's broader than the get_valid_date function as it will also accept entire months or years as valid dates
    '''
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
    '''
    this function will convert YYYY-MM-DD date-strings into DD-MM-YYYY date-strings and is used in print statements, to make the program more user-friendly
    '''
    if len(date) == 10:
        formatted_date = datetime.strptime(date, '%Y-%m-%d').strftime('%d-%m-%Y')
    if len(date) == 7:
        formatted_date = datetime.strptime(date, '%Y-%m').strftime('%B of %Y')
    if len(date) == 4:
        formatted_date = f'the year {date}'
    return formatted_date

