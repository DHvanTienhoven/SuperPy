## User's manual for SuperPy
  


SuperPy is a program designed to keep track of the inventory and sales of a Supermarket. It is operated through the command line. In SuperPy there's six possible actions:  

 *buy  
 *sell  
 *report inventory  
 *report revenue  
 *balance report    
 *advance time  
 *report on product  
 *expiration report  

In this manual I will discuss each of the actions.

### Buy

To buy a product for your Supermarket you will need to use the command

> python main.py buy

and you need to provide the name and the price of the product. You can do this using the --name/-n and the --price/-p flag respectively. The price must be a float. For example:

> python main.py buy --name apple --price 0.42

or:

> python main.py buy -n apple -p 0.42

There are some other optional arguments:  
**date of purchase** The date of purchase can be added with the --date/-d flag. If no date is given the default date is today. The date must be provided in the YYYY-MM-DD format or can one of the following: two_weeks_ago, one_week_ago, day_before_yesterday, yesterday, today, tomorrow, day_after_tomorrow, next_week, two_weeks_ahead.  
**expiration date** The expiration date for the product can be added with the --expiration/-e flag. If no expiration date is provided the default is set to two weeks from today. The date must be provided in the YYYY-MM-DD format or can one of the following: two_weeks_ago, one_week_ago, day_before_yesterday, yesterday, today, tomorrow, day_after_tomorrow, next_week, two_weeks_ahead.  
**quantity** The quantity of the product you'd like to buy with the --q/-q flag. If no quantity is given the default is set to 1. The quantity must be an integer.  
  
so you could also buy a product like this:

> python main.py buy --name apple --price 0.42 --quantity 135 --date yesterday --expiration 2021-11-04

or:

> python main.py buy -n apple -p 0.42 -q 135 -d yesterday -e 2021-11-04

When you buy a product the inventory as well as the balance of your supermarket will be updated. 

### Sell

To sell a product from your Supermarket you will need to use the command

> python main.py sell

and you need to provide the name and the price of the product. You can do this using the --name/-n and the --price/-p flag respectively. The price must be a float. For example:

> python main.py sell --name oatmeal --price 1.12

or:

> python main.py sell -n oatmeal -p 1.12

There are some other optional arguments:  
**date of sale** The date of sale can be added with the --date/-d flag. If no date is given the default date is today. The date must be provided in the YYYY-MM-DD format or can one of the following: two_weeks_ago, one_week_ago, day_before_yesterday, yesterday, today, tomorrow, day_after_tomorrow, next_week, two_weeks_ahead.  
**quantity** The quantity of the product you'd like to sell with the --q/-q flag. If no quantity is given the default is set to 1. The quantity must be an integer.  
  
so you could also sell a product like this:

> python main.py sell --name oatmeal --price 1.12 --quantity 3 --date tomorrow

or:

> python main.py sell -n oatmeal -p 1.12 -q 3 -d tomorrow

If you try to sell a product that's not in store or if there's not enough of the product in store, you will receive a message like *oatmeal is not in stock, the sale is not possible* or *there's not enough oatmeal in stock, the maximum amount of oatmeal you can sell is 2*. If there is enough of the product in store to make the sale your inventory and balance will be updated.

### Report Inventory

If you want to see the inventory of the supermarket on a given day you can use the command

> python main.py report_inventory

to specify the date for which you would like to see the inventory you can use the --date/-d flag. If no date is given the default is today. The date must be provided in the YYYY-MM-DD format or can one of the following: two_weeks_ago, one_week_ago, day_before_yesterday, yesterday, today, tomorrow, day_after_tomorrow, next_week, two_weeks_ahead. For example:

> python main.py report_inventory --date day_before_yesterday

or:

> python main.py report_inventory --d 2022-09-13

The program will print a table with the names of all the products in store, the count of that product, the price that it was bought for and the expiration date. It will show the inventory of the store at the end of the given day.  

### Report on balance

If you want to see the revenue or the profit of the supermarket for a given period you can use the command

> python main.py balance_report

You'll have to specify what type of report you'd like to receive with the --report or -r flag. The options are: 'revenue' or 'profit'.  

You can see the revenue or profit for either a given day or a calendar month or a calendar year. You can specify the period of the report with the --date/-d flag. If no date is given the default is today. If you would like to see the revenue or profit for a given calendar year provide the date as YYYY, if you'd like to see a calendar month, provide the date as YYYY-MM and if you'd like to see the revenue or profit for one day provide the date as YYYY-MM-DD or it can be one of the following: two_weeks_ago, one_week_ago, day_before_yesterday, yesterday, today, tomorrow, day_after_tomorrow, next_week, two_weeks_ahead.  

For example:

> python main.py balance_report --report revenue --date tomorrow

or:

> python main.py balance_report -r profit --date 2019-08

or:

> python main.py balance_report -r revenue -d 2021

The program will print the revenue or profit. for the given time period.  

### Report on product.  

If you would like to receive a report on a given product on a given date you can use the command:  

> python main.py report_on_product

you'll have to specify the product name with the --name or -n flag. You can also provide a date with the --date or -d flag. The date must be provided in the YYYY-MM-DD format or can one of the following: two_weeks_ago, one_week_ago, day_before_yesterday, yesterday, today, tomorrow, day_after_tomorrow, next_week, two_weeks_ahead. If no date is given the default is set to today. for example:  

> python main.py report_on_product --name chocolate  

or:  

> python main.py report_on_product --n chocolate -d tomorrow  
  
  or:  
    
> python main.py report_on_product --n chocolate -d 2020-08-17  

The program will then generate a csv-file which will show you how many items of that product were in store, how many were sold and how many were expired on the given date, and will store it in the reports directory.  
  

### Report Expired  
  
If you would like to recieve a report on the expired products on a given date you can use:  

> python main.py report_expired
  
You can also provide a date with the --date or -d flag. The date must be provided in the YYYY-MM-DD format or can one of the following: two_weeks_ago, one_week_ago, day_before_yesterday, yesterday, today, tomorrow, day_after_tomorrow, next_week, two_weeks_ahead. If no date is given the default is set to today. for example:  
  
> python main.py report_expired --date two_weeks_ahead
  
> python main.py report_expired -d 2021-11-01

The program will then generate a csv-file which will show you how many items were in store on the given date that were expired on the given date, it will also show the 'lost cost': the price payed for the product that will not be earned back, and will store it in the reports directory.  

### Advance Time 

It's possible to jump back and forth in time in this program. If you use this functionality, the date of 'today' as well as other relative dates such as 'day_before_yesterday' or 'two_weeks_ahead' for the programm will change. You can do this with the following command:

> python main.py advance_time

additionally provide the number of days with the --time/-t flag. This must be an integer. If no number of days is specified or if the number of days is specified as 0, 'today' will reset to the actual current date. If a negative number is provided the program will go back in time, if a positive number is provided it will jump ahead.  
for example:

> python main.py advance_time --time 90

will make the program go ahead in time 90 days.

> python main.py advance_time -t -5

will make the program go back in time by 5 days.  
Both:

> python main.py advance_time

and:

> python main.py advance_time -t 0

will reset the current date of the program to the actual date. 

