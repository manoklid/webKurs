# Generated by Django 3.2.2 on 2021-06-24 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_group_2321_group_2322'),
    ]

    operations = [
        migrations.CreateModel(
            name='group_2361',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week', models.IntegerField(choices=[(0, 'Обе недели'), (1, 'Верхняя неделя'), (2, 'Нижняя неделя')], verbose_name='Вехрняя или нижняя неделя')),
                ('day', models.IntegerField(choices=[(0, 'Понедельник'), (1, 'Вторник'), (2, 'Среда'), (3, 'Четверг'), (4, 'Пятница'), (5, 'Суббота')], verbose_name='День недели')),
                ('time', models.IntegerField(choices=[(0, '08.30-10.00'), (1, '10.10-11.40'), (2, '12.10-13.40'), (3, '14.10-15.40'), (4, '15.50-17.20'), (5, '17.30-19.00'), (6, '19.10-20.40')], verbose_name='Время')),
                ('teacher', models.CharField(blank=True, default='', max_length=70, verbose_name='Преподаватель')),
                ('classroom', models.CharField(blank=True, default='', max_length=10, verbose_name='Аудитория')),
                ('name', models.CharField(max_length=100, verbose_name='Название пары')),
            ],
            options={
                'verbose_name': 'Пара группы 2361',
                'verbose_name_plural': 'Расписание группы 2361',
            },
        ),
        migrations.CreateModel(
            name='group_2371',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week', models.IntegerField(choices=[(0, 'Обе недели'), (1, 'Верхняя неделя'), (2, 'Нижняя неделя')], verbose_name='Вехрняя или нижняя неделя')),
                ('day', models.IntegerField(choices=[(0, 'Понедельник'), (1, 'Вторник'), (2, 'Среда'), (3, 'Четверг'), (4, 'Пятница'), (5, 'Суббота')], verbose_name='День недели')),
                ('time', models.IntegerField(choices=[(0, '08.30-10.00'), (1, '10.10-11.40'), (2, '12.10-13.40'), (3, '14.10-15.40'), (4, '15.50-17.20'), (5, '17.30-19.00'), (6, '19.10-20.40')], verbose_name='Время')),
                ('teacher', models.CharField(blank=True, default='', max_length=70, verbose_name='Преподаватель')),
                ('classroom', models.CharField(blank=True, default='', max_length=10, verbose_name='Аудитория')),
                ('name', models.CharField(max_length=100, verbose_name='Название пары')),
            ],
            options={
                'verbose_name': 'Пара группы 2371',
                'verbose_name_plural': 'Расписание группы 2371',
            },
        ),
    ]