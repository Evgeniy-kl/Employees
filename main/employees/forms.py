from django import forms
from .models import *


class PositionForm(forms.ModelForm):
    class Meta:
        model = Position
        fields = ['position_name']

    position_name = forms.CharField()

    def clean(self):
        position_name = self.cleaned_data['position_name']
        if Position.objects.filter(position_name=position_name).exists():
            raise forms.ValidationError(f'Должность "{position_name} уже существует')
        return self.cleaned_data


class SubdivisionForm(forms.ModelForm):

    class Meta:
        model = Subdivision
        fields = ['subdivision_name']

    subdivision_name = forms.CharField()

    def clean(self):
        subdivision_name = self.cleaned_data['subdivision_name']
        if Subdivision.objects.filter(subdivision_name=subdivision_name).exists():
            raise forms.ValidationError(f'Подразделение "{subdivision_name} уже существует')
        return self.cleaned_data


class SubdivisionFormDelete(forms.ModelForm):

    class Meta:
        model = Subdivision
        fields = ['subdivision_name']

    subdivision_name = forms.CharField()

    def clean(self):
        subdivision_name = self.cleaned_data['subdivision_name']
        if not Subdivision.objects.filter(subdivision_name=subdivision_name).exists():
            raise forms.ValidationError(f'Подразделение "{subdivision_name} не существует')
        return self.cleaned_data


class EmployeeForm(forms.ModelForm):

    started_work_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))

    class Meta:
        model = Employee
        fields = ['full_name', 'subdivision', 'position', 'started_work_date']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['started_work_date'].label = 'Дата начала работы'

    def clean(self):
        full_name = self.cleaned_data['full_name']
        subdivision = self.cleaned_data['subdivision']
        position = self.cleaned_data['position']
        started_work_date = self.cleaned_data['started_work_date']
        if Employee.objects.filter(full_name=full_name, subdivision=subdivision, position=position).exists():
            raise forms.ValidationError(f'Такой сотрудник уже работает ')
        return self.cleaned_data


class EmployeeDeleteForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ['id']

    id = forms.CharField()

    def clean(self):
        id = self.cleaned_data['id']
        if not Employee.objects.filter(id=id).exists():
            raise forms.ValidationError(f'Сотрудник с ID: {id} не найден')
        return self.cleaned_data


class EmployeeUpdateSubdivisionForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ['subdivision']


class EmployeeUpdatePositionForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ['position']


class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Логин'
        self.fields['password'].label = 'Пароль'

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        if not User.objects.filter(username=username).exists():
            raise forms.ValidationError(f'Пользователь с логином "{username} не найден в системе')
        user = User.objects.filter(username=username).first()
        if user:
            if not user.check_password(password):
                raise forms.ValidationError("Неверный пароль")
        return self.cleaned_data