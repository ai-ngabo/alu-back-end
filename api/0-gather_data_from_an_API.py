#!/usr/bin/python3
import requests
import sys

if len(sys.argv) != 2:
    print("Usage: python3 script.py EMPLOYEE_ID")
    sys.exit(1)

employee_id = int(sys.argv[1])
base_url = "https://jsonplaceholder.typicode.com/"

# Fetch employee details
employee = requests.get(base_url + f"users/{employee_id}").json()
employee_name = employee.get('name')

# Fetch employee's TODO list
todos = requests.get(base_url + f"todos?userId={employee_id}").json()

# Filter and count completed tasks
completed_tasks = [todo['title'] for todo in todos if todo['completed']]
number_of_done_tasks = len(completed_tasks)
total_number_of_tasks = len(todos)

# Display TODO list progress
print(
   f"Employee {employee_name} is done with tasks("
   f"{number_of_done_tasks}/{total_number_of_tasks}):"
)
for task in completed_tasks:
    print(f"\t {task}")
