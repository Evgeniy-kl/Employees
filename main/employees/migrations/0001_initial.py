# Generated by Django 3.2.8 on 2021-10-29 14:56

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subdivision',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Название подразделения')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=256, verbose_name='ФИО сотрудника')),
                ('position', models.CharField(choices=[('Главный бухгалтер', 'Chief Accountant'), ('Главный диспетчер', 'Chief Dispatcher'), ('Главный инженер', 'Chief Engineer'), ('Главный конструктор', 'Chief Designer'), ('Финансовый директор', 'Cfo'), ('Директор предприятия', 'Director Of The Enterprise')], max_length=256, verbose_name='Должность')),
                ('started_work_date', models.DateField(default=django.utils.timezone.now, verbose_name='Дата начала работы')),
                ('experience', models.IntegerField(verbose_name='Стаж')),
                ('subdivision', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees.subdivision', verbose_name='Подразделение')),
            ],
        ),
    ]
