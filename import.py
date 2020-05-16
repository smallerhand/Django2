#have to run below in shell.
#python manage.py shell < import.py


import csv
from empapp.models import employee

with open('data/employees.csv', encoding = 'utf-8-sig') as f:
    reader = csv.DictReader(f)
    for row in reader:
        emp_num         =	row['従業員番号']
        emp_name        =	row['氏名']
        emp_ename       =	row['氏名（ローマ字）']
        sex             =	row['性別']
        birth           =	row['生年月日']
        age             =	row['年齢']
        bloodtype       =	row['血液型']
        dep             =	row['所属組織']
        job             =	row['役職']
        employee.objects.create(emp_num	=	emp_num	,
                                emp_name	=	emp_name	,
                                emp_ename	=	emp_ename	,
                                sex	=	sex	,
                                birth	=	birth	,
                                age	=	age	,
                                bloodtype	=	bloodtype	,
                                dep	=	dep	,
                                job	=	job
                                )
