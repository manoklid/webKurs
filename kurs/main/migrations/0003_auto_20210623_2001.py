# Generated by Django 3.2.2 on 2021-06-23 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210623_1955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group_2342',
            name='classroom',
            field=models.CharField(blank=True, default='', max_length=10, verbose_name='Аудитория'),
        ),
        migrations.AlterField(
            model_name='group_2342',
            name='teacher',
            field=models.CharField(blank=True, default='', max_length=70, verbose_name='Преподаватель'),
        ),
    ]
