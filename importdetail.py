#have to run below in shell.
#python manage.py shell < importdetail.py

import csv
from empapp.models import employeeDetail

with open('data/employeeDetails.csv', encoding = 'utf-8-sig') as f:
    reader = csv.DictReader(f)
    for row in reader:
        employeeDetail.objects.create(num	    =	row['従業員番号']		,
                                        lname	=	row['姓（漢字）']		,
                                        fname	=	row['名（漢字）']		,
                                        elname	=	row['姓（ローマ字）']		,
                                        efname	=	row['名（ローマ字）']		,
                                        sex	    =	row['性別']		,
                                        email	=	row['メールアドレス']		,
                                        birth	=	row['生年月日']		,
                                        age	    =	row['年齢'	]	,
                                        bloodtype	=	row['血液型']		,
                                        dep	    =	row['所属組織']		,
                                        job     =	row['役職']			,
                                        pw      =	row['パスワード']
                                    )
