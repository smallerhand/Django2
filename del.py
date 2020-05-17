#python manage.py shell < del.py

from empapp.models import employeeDetail
employeeDetail.objects.all().delete()
employeeDetail.objects.values()
