# Generated by Django 3.2.9 on 2021-11-02 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Имя')),
                ('phone', models.CharField(max_length=50, verbose_name='# Телефона')),
            ],
            options={
                'verbose_name': 'Работник',
                'verbose_name_plural': 'Работники',
            },
        ),
        migrations.CreateModel(
            name='RetailPoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.employee', verbose_name='Работник')),
            ],
            options={
                'verbose_name': 'Торговая точка',
                'verbose_name_plural': 'Торговые точки',
            },
        ),
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visit_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата')),
                ('retail_point', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.retailpoint', verbose_name='Торговая точка')),
            ],
            options={
                'verbose_name': 'Посещение',
                'verbose_name_plural': 'Посещения',
            },
        ),
    ]