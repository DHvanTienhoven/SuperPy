import argparse
import csv

"""parser = argparse.ArgumentParser()

def write():
    with open('practice.csv', mode='a', newline='') as practice_file:
        employee_writer = csv.writer(practice_file, delimiter=',')
        employee_writer.writerow(['test', 'hoi', 'bla'])
        employee_writer.writerow(['wes', 'fyn', 'lot'])

parser.add_argument("language")
parser.add_argument("name")
parser.add_argument("name")

args = parser.parse_args()

if args.language == 'Python':
    print("I love Python too")
else:
    print("Learn Python, you will like it")

print(f'Hello {args.name}, this was a simple introduction to argparse module')"""


def take_last(element):
    return element[-1]
    pass


collection = [[2,5,10,14], [1,2,3,4]]

collection.sort(key=take_last)

print(collection)

