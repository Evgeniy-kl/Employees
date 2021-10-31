import datetime

from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.views import View
from django.views.generic import DetailView, TemplateView

from .models import *
from .forms import *


class BaseView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self, request):
        return render(request, 'base.html', {})


class PositionView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self, request):
        context = {
            'positions': Position.objects.all()
        }
        return render(request, 'positions.html', context)

    def post(self, request):
        form = PositionForm(request.POST or None)
        if form.is_valid():
            position_name = form.cleaned_data['position_name']
            Position.objects.create(
                position_name=position_name
            )

        context = {
            'positions': Position.objects.all()
        }
        return render(request, 'positions.html', context)


class SubdivisionView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self, request):
        context = {
            'subdivisions': Subdivision.objects.all()
        }
        return render(request, 'subdivision.html', context)

    def post(self, request):
        form = SubdivisionForm(request.POST or None)
        if form.is_valid():
            subdivision_name = form.cleaned_data['subdivision_name']
            Subdivision.objects.create(
                subdivision_name=subdivision_name
            )

        context = {
            'subdivisions': Subdivision.objects.all()
        }
        return render(request, 'subdivision.html', context)


def delete_subdivision(request):
    if request.method == 'POST':
        form = SubdivisionFormDelete(request.POST or None)
        if form.is_valid():
            subdivision_name = form.cleaned_data['subdivision_name']
            Subdivision.objects.filter(
                subdivision_name=subdivision_name
            ).delete()

        context = {
            'subdivisions': Subdivision.objects.all()
        }
        return render(request, 'subdivision.html', context)


class EmployeesView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self, request, *args, **kwargs):
        form = EmployeeForm(request.POST or None)
        context = {
            'form': form,
            'employees': Employee.objects.all(),
        }
        return render(request, 'employees.html', context)

    def post(self, request):
        form = EmployeeForm(request.POST or None)
        if form.is_valid():
            full_name = form.cleaned_data['full_name']
            subdivision = form.cleaned_data['subdivision']
            position = form.cleaned_data['position']
            started_work_date = form.cleaned_data['started_work_date']
            experience = datetime.date.today().year-started_work_date.year
            Employee.objects.create(
                full_name=full_name,
                subdivision=subdivision,
                position=position,
                started_work_date=started_work_date,
                experience=experience,
            )

        return redirect('/employees/')


class EmployeeDeleteView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'login'

    def post(self, request):
        form = EmployeeDeleteForm(request.POST or None)
        if form.is_valid():
            id = form.cleaned_data['id']
            Employee.objects.filter(
                id=id
            ).delete()

        return redirect('/employees/')


class EmployeeDetailView(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'
    template_name = 'employee_detail.html'

    def get_context_data(self, **kwargs):
        id_ = self.kwargs['id']
        context = super().get_context_data(**kwargs)
        context['employee'] = get_object_or_404(Employee, id=id_)
        context['form'] = EmployeeUpdateSubdivisionForm()
        context['form2'] = EmployeeUpdatePositionForm()
        return context

    def post(self, request, **kwargs):
        id_ = self.kwargs['id']
        form_sub = EmployeeUpdateSubdivisionForm(request.POST or None)
        form_pos = EmployeeUpdatePositionForm(request.POST or None)
        if form_sub.is_valid():
            subdivision = form_sub.cleaned_data['subdivision']

            Employee.objects.filter(id=id_).update(
                subdivision=subdivision,
            )

        if form_pos.is_valid():
            position = form_pos.cleaned_data['position']

            Employee.objects.filter(id=id_).update(
                position=position,
            )

        return redirect('/employees/')


class LoginView(View):
    def get(self, request):
        form = LoginForm(request.POST or None)
        context = {
            'form': form,
        }
        return render(request, 'login.html', context)

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(
                username=username, password=password
            )
            if user:
                login(request, user)
                return HttpResponseRedirect('/')

        return render(request, 'base.html')








