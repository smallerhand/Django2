#python manage.py shell < import.py

import csv
from empapp.models import employee
hand = open('data/employees.csv', encoding = 'utf-8-sig')
reader = csv.reader(hand)
bulk_list = []
for row in reader:
    bulk_list.append(employee(
    emp_num = row[0],
    emp_name = row[1],
    emp_ename = row[2],
    sex = row[3],
    birth = row[4],
    age = row[5],
    bloodtype = row[6],
    dep = row[7],
    job = row[8]))

employee.objects.bulk_create(bulk_list)
employee.objects.values()
