# Generated by Django 3.2.2 on 2021-07-03 05:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20210703_1320'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='group_2341',
            options={'ordering': ['time', 'day'], 'verbose_name': 'Пара группы 02341-ДБ', 'verbose_name_plural': 'Расписание группы 02341-ДБ'},
        ),
        migrations.AlterModelOptions(
            name='group_2342',
            options={'ordering': ['time', 'day'], 'verbose_name': 'Пара группы 02342-ДБ', 'verbose_name_plural': 'Расписание группы 02342-ДБ'},
        ),
        migrations.AlterModelTable(
            name='group_2121m',
            table='Расписание группы 02121-ДМ',
        ),
        migrations.AlterModelTable(
            name='group_2122m',
            table='Расписание группы 02122-ДМ',
        ),
        migrations.AlterModelTable(
            name='group_2161m',
            table='Расписание группы 02161-ДМ',
        ),
        migrations.AlterModelTable(
            name='group_2171m',
            table='Расписание группы 02171-ДМ',
        ),
        migrations.AlterModelTable(
            name='group_2261m',
            table='Расписание группы 02261-ДМ',
        ),
        migrations.AlterModelTable(
            name='group_2321',
            table='Расписание группы 02321-ДБ',
        ),
        migrations.AlterModelTable(
            name='group_2322',
            table='Расписание группы 02322-ДБ',
        ),
        migrations.AlterModelTable(
            name='group_2361',
            table='Расписание группы 02361-ДБ',
        ),
        migrations.AlterModelTable(
            name='group_2371',
            table='Расписание группы 02371-ДБ',
        ),
    ]
