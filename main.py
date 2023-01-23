import datetime
from application.salary import calculate_salary
from application.db.people import get_employees

if __name__ == '__main__':
    current_time = datetime.datetime.now()
    print(f'Current date: {current_time}')
    calculate_salary()
    get_employees()
