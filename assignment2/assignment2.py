#Task 2: Read a CSV File
import csv
import traceback
import custom_module
from datetime import datetime

def read_employees():
    employees_dict = {}
    rows = []

    try:
        with open("C:\\Users\\joanp\\OneDrive\\Desktop\\CTD Python\\python_class\\python_homework\\csv\\employees.csv", newline="") as f:
            reader = csv.reader(f)
            for index, row in enumerate(reader):
                if index == 0:
                    employees_dict["fields"] = row
                else:
                    rows.append(row)
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        print("An exception occurred.")
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")
        exit(1)

    employees_dict["rows"] = rows
    return employees_dict

employees = read_employees()

#Task 3: Find the Column Index
def column_index(column_name):
    return employees["fields"].index(column_name)
 
employee_id_column = column_index("employee_id")

#Task 4: Find the Employee First Name
def first_name(row_number):
    first_name_column = column_index("first_name")
    row = employees["rows"][row_number]
    return row[first_name_column]

#Task 5: Find the Employee: a Function in a Function
def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
 
    matches = list(filter(employee_match, employees["rows"]))
    return matches

#Task 6: Find the Employee with a Lambda
def employee_find_2(employee_id):
    matches = list(filter(lambda row : int(row[employee_id_column]) == employee_id , employees["rows"]))
    return matches

#Task 7: Sort the Rows by last_name Using a Lambda
def sort_by_last_name():
    last_name_column = column_index("last_name")
    employees["rows"].sort(key=lambda row: row[last_name_column])
    return employees["rows"]
sort_by_last_name()

#Task 8: Create a dict for an Employee
def employee_dict(row):
    result = {}
    for index, field in enumerate(employees["fields"]):
        if index == employee_id_column:
            continue
        result[field] = row[index]
    return result
#print(employee_dict(employees["rows"][0])) (to test above function)

#Task 9: A dict of dicts, for All Employees
def all_employees_dict():
    result = {}
    for row in employees["rows"]:
        result[row[employee_id_column]] = employee_dict(row)
    return result
#print(all_employees_dict())

#Task 10: Use the os Module
import os
def get_this_value():
    return os.getenv("THISVALUE")
#print(get_this_value())

#Task 11: Creating Your Own Module
def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)

set_that_secret("ModelMakeYear")
#print(custom_module.secret)

#Task 12: Read minutes1.csv and minutes2.csv
def read_csv_file(path):
    result = {}
    rows = []

    try:
        with open(path, newline="") as f:
            reader = csv.reader(f)
            for index, row in enumerate(reader):
                if index == 0:
                    result["fields"] = row
                else:
                    rows.append(tuple(row))
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        print("An exception occurred.")
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")
        exit(1)

    result["rows"] = rows
    return result


def read_minutes():
    minutes1 = read_csv_file("C:\\Users\\joanp\\OneDrive\\Desktop\\CTD Python\\python_class\\python_homework\\csv\\minutes1.csv")
    minutes2 = read_csv_file("C:\\Users\\joanp\\OneDrive\\Desktop\\CTD Python\\python_class\\python_homework\\csv\\minutes2.csv")
    return minutes1, minutes2


minutes1, minutes2 = read_minutes()
#print(minutes1)
#print(minutes2)

#Task 13: Create minutes_set
def create_minutes_set():
    set1 = set(minutes1["rows"])
    set2 = set(minutes2["rows"])
    return set1.union(set2)

minutes_set = create_minutes_set()
#print(minutes_set)

#Task 14: Convert to datetime
def create_minutes_list():
    minutes_list = list(minutes_set)
    return list(map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), minutes_list))


minutes_list = create_minutes_list()
print(minutes_list)

#Task 15: Write Out Sorted List
def write_sorted_list():
    minutes_list.sort(key=lambda x: x[1])
    converted_list = list(map(lambda x: (x[0], datetime.strftime(x[1], "%B %d, %Y")), minutes_list))

    with open("./minutes.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(minutes1["fields"])
        writer.writerows(converted_list)

    return converted_list
#print(write_sorted_list())