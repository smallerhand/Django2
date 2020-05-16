from django.urls import path

from . import views

urlpatterns = [
    path('list/', views.list, name='list'),
    path('details/<int:empdetail_id>/', views.detail, name='detail'),
]
