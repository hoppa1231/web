from django.db import models


class Product(models.Model):
    autor = models.CharField('Автор', max_length=25)
    title = models.CharField('Название', max_length=25)
    min_group = models.IntegerField('Минимальный размер группы')
    max_group = models.IntegerField('Максимальный размер группы')
    price = models.IntegerField('Цена')
    date = models.DateTimeField('Дата')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.title


class Groups(models.Model):
    title = models.CharField('Название', max_length=25)
    students = models.TextField('Ученики', blank=True, null=True)
    link = models.CharField('Продукт', max_length=25)

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

    def __str__(self):
        return self.title


class Lessons(models.Model):
    title = models.CharField('Название', max_length=25)
    src = models.TextField('Ссылка на видео', blank=True, null=True)
    link = models.CharField('Продукт', max_length=25)

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'

    def __str__(self):
        return self.title