# Generated by Django 3.2.9 on 2021-11-02 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='visit',
            name='coordinates',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='Координаты'),
        ),
    ]