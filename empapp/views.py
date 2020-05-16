from django.shortcuts import render, get_object_or_404
from .models import employeeDetail

def list(request):
    emp = employeeDetail.objects.all()
    return render(request, 'list.html', {'emplist' : emp})

def detail(request, empdetail_id):
    empdetail = get_object_or_404(employeeDetail, pk=empdetail_id)
    return render(request, 'details.html', {'empdetail' : empdetail})
