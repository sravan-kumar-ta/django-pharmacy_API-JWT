# Generated by Django 3.2.10 on 2022-01-24 07:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicines', '0011_alter_medicine_stock'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='medicine',
            name='slug',
        ),
    ]
