from django.shortcuts import render
from .models import employee

def list(request):
    emp = employee.objects.all()
    return render(request, 'list.html', {'emplist' : emp})
