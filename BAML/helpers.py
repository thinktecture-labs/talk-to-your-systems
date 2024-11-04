def read_employees():
    with open('employees.txt', 'r') as file:
        return file.read().strip()
