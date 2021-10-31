from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', BaseView.as_view(), name='base'),
    path('positions/', PositionView.as_view(), name='positions'),
    path('subdivisions/', SubdivisionView.as_view(), name='subdivisions'),
    path('subdivisions_delete/', delete_subdivision, name='subdivisions_delete'),
    path('employees/', EmployeesView.as_view(), name='employees'),
    path('employees_delete/', EmployeeDeleteView.as_view(), name='employees_delete'),
    path('employees/<int:id>/', EmployeeDetailView.as_view(), name='employees_detail'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page="/"), name='logout'),
]