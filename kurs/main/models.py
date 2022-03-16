from django.db import models

class news_model(models.Model):
    header = models.CharField('Заголовок', max_length=100)
    text = models.CharField('Текст статьи', max_length=7000)

    def __str__(self):
        return self.header

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        db_table = "Новости"

class abstract_group_model(models.Model):
    weekChoise = [
        (0, 'Обе недели'),
        (1, 'Верхняя неделя'),
        (2, 'Нижняя неделя'),
    ]
    dayChoise = [
        (0, 'Понедельник'),
        (1, 'Вторник'),
        (2, 'Среда'),
        (3, 'Четверг'),
        (4, 'Пятница'),
        (5, 'Суббота'),
    ]
    timeChoise = [
        (0, '08.30-10.00'),
        (1, '10.10-11.40'),
        (2, '12.10-13.40'),
        (3, '14.10-15.40'),
        (4, '15.50-17.20'),
        (5, '17.30-19.00'),
        (6, '19.10-20.40'),
    ]
    week = models.IntegerField('Верхняя или нижняя неделя', choices=weekChoise)
    day = models.IntegerField('День недели', choices=dayChoise)
    time = models.IntegerField('Время', choices=timeChoise)
    teacher = models.CharField('Преподаватель', max_length=70, blank=True, default='')
    classroom = models.CharField('Аудитория', max_length=30, blank=True, default='')
    name = models.CharField('Предмет', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True
        ordering = ['time', 'day']

class group_2342(abstract_group_model):
    class Meta:
        verbose_name = 'Пара группы 02342-ДБ'
        verbose_name_plural = 'Расписание группы 02342-ДБ'
        db_table = "Расписание группы 02342-ДБ"



class group_2341(abstract_group_model):
    class Meta:
        verbose_name = 'Пара группы 02341-ДБ'
        verbose_name_plural = 'Расписание группы 02341-ДБ'
        db_table = "Расписание группы 02341-ДБ"


class group_2321(abstract_group_model):
    class Meta:
        verbose_name = 'Пара группы 02321-ДБ'
        verbose_name_plural = 'Расписание группы 02321-ДБ'
        db_table = "Расписание группы 02321-ДБ"

class group_2322(abstract_group_model):
    class Meta:
        verbose_name = 'Пара группы 02322-ДБ'
        verbose_name_plural = 'Расписание группы 02322-ДБ'
        db_table = "Расписание группы 02322-ДБ"


class group_2361(abstract_group_model):
    class Meta:
        verbose_name = 'Пара группы 02361-ДБ'
        verbose_name_plural = 'Расписание группы 02361-ДБ'
        db_table = "Расписание группы 02361-ДБ"


class group_2371(abstract_group_model):
    class Meta:
        verbose_name = 'Пара группы 02371-ДБ'
        verbose_name_plural = 'Расписание группы 02371-ДБ'
        db_table = "Расписание группы 02371-ДБ"


class group_2261M(abstract_group_model):
    class Meta:
        verbose_name = 'Пара группы 02261-ДМ'
        verbose_name_plural = 'Расписание группы 02261-ДМ'
        db_table = 'Расписание группы 02261-ДМ'


class group_2121M(abstract_group_model):
    class Meta:
        verbose_name = 'Пара группы 02121-ДМ'
        verbose_name_plural = 'Расписание группы 02121-ДМ'
        db_table = 'Расписание группы 02121-ДМ'

class group_2122M(abstract_group_model):
    class Meta:
        verbose_name = 'Пара группы 02122-ДМ'
        verbose_name_plural = 'Расписание группы 02122-ДМ'
        db_table = 'Расписание группы 02122-ДМ'

class group_2161M(abstract_group_model):
    class Meta:
        verbose_name = 'Пара группы 02161-ДМ'
        verbose_name_plural = 'Расписание группы 02161-ДМ'
        db_table = 'Расписание группы 02161-ДМ'


class group_2171M(abstract_group_model):
    class Meta:
        verbose_name = 'Пара группы 02171-ДМ'
        verbose_name_plural = 'Расписание группы 02171-ДМ'
        db_table = 'Расписание группы 02171-ДМ'
