# Generated by Django 4.1.4 on 2023-04-22 17:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_employee_company'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='company',
            new_name='companies',
        ),
    ]