#python manage.py shell < del.py

from empapp.models import employee
employee.objects.all().delete()
employee.objects.values()
