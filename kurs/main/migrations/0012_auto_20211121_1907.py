# Generated by Django 3.2.2 on 2021-11-21 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20210703_1322'),
    ]

    operations = [
        migrations.CreateModel(
            name='news_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher', models.CharField(blank=True, default='', max_length=40, verbose_name='Заголовок')),
                ('classroom', models.CharField(blank=True, default='', max_length=500, verbose_name='Текст статьи')),
            ],
        ),
        migrations.AlterField(
            model_name='group_2121m',
            name='week',
            field=models.IntegerField(choices=[(0, 'Обе недели'), (1, 'Верхняя неделя'), (2, 'Нижняя неделя')], verbose_name='Верхняя или нижняя неделя'),
        ),
        migrations.AlterField(
            model_name='group_2122m',
            name='week',
            field=models.IntegerField(choices=[(0, 'Обе недели'), (1, 'Верхняя неделя'), (2, 'Нижняя неделя')], verbose_name='Верхняя или нижняя неделя'),
        ),
        migrations.AlterField(
            model_name='group_2161m',
            name='week',
            field=models.IntegerField(choices=[(0, 'Обе недели'), (1, 'Верхняя неделя'), (2, 'Нижняя неделя')], verbose_name='Верхняя или нижняя неделя'),
        ),
        migrations.AlterField(
            model_name='group_2171m',
            name='week',
            field=models.IntegerField(choices=[(0, 'Обе недели'), (1, 'Верхняя неделя'), (2, 'Нижняя неделя')], verbose_name='Верхняя или нижняя неделя'),
        ),
        migrations.AlterField(
            model_name='group_2261m',
            name='week',
            field=models.IntegerField(choices=[(0, 'Обе недели'), (1, 'Верхняя неделя'), (2, 'Нижняя неделя')], verbose_name='Верхняя или нижняя неделя'),
        ),
        migrations.AlterField(
            model_name='group_2321',
            name='week',
            field=models.IntegerField(choices=[(0, 'Обе недели'), (1, 'Верхняя неделя'), (2, 'Нижняя неделя')], verbose_name='Верхняя или нижняя неделя'),
        ),
        migrations.AlterField(
            model_name='group_2322',
            name='week',
            field=models.IntegerField(choices=[(0, 'Обе недели'), (1, 'Верхняя неделя'), (2, 'Нижняя неделя')], verbose_name='Верхняя или нижняя неделя'),
        ),
        migrations.AlterField(
            model_name='group_2341',
            name='week',
            field=models.IntegerField(choices=[(0, 'Обе недели'), (1, 'Верхняя неделя'), (2, 'Нижняя неделя')], verbose_name='Верхняя или нижняя неделя'),
        ),
        migrations.AlterField(
            model_name='group_2342',
            name='week',
            field=models.IntegerField(choices=[(0, 'Обе недели'), (1, 'Верхняя неделя'), (2, 'Нижняя неделя')], verbose_name='Верхняя или нижняя неделя'),
        ),
        migrations.AlterField(
            model_name='group_2361',
            name='week',
            field=models.IntegerField(choices=[(0, 'Обе недели'), (1, 'Верхняя неделя'), (2, 'Нижняя неделя')], verbose_name='Верхняя или нижняя неделя'),
        ),
        migrations.AlterField(
            model_name='group_2371',
            name='week',
            field=models.IntegerField(choices=[(0, 'Обе недели'), (1, 'Верхняя неделя'), (2, 'Нижняя неделя')], verbose_name='Верхняя или нижняя неделя'),
        ),
    ]