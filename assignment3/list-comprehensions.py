#Task 3: List Comprehensions Practice
import csv

# Step 1: read ../csv/employees.csv into a list of lists
with open(r"C:\Users\joanp\OneDrive\Desktop\CTD Python\python_class\python_homework\csv\employees.csv", newline="") as f:
    reader = csv.reader(f)
    rows = [row for row in reader]

# Step 2: full names (first_name + space + last_name), skipping the heading row
# Assumes first_name is column 1 and last_name is column 2 (employee_id is column 0).
header = rows[0]
first_idx = header.index("first_name")
last_idx = header.index("last_name")

names = [row[first_idx] + " " + row[last_idx] for row in rows[1:]]
print(names)

# Step 3: only the names that contain the letter "e"
names_with_e = [name for name in names if "e" in name]
print(names_with_e)