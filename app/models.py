from django.db import models


class Person(models.Model):
    name = models.CharField('Имя', max_length=100)
    surname = models.CharField('Фамилия', max_length=200)
    number = models.CharField('Номер телефона', max_length=100)
    email = models.EmailField('Почта', max_length=254)
    html = models.BooleanField(default=False)
    css = models.BooleanField(default=False)
    js = models.BooleanField(default=False)
    vue = models.BooleanField(default=False)
    react = models.BooleanField(default=False)
    ux = models.BooleanField(default=False)
    python = models.BooleanField(default=False)
    php = models.BooleanField(default=False)
    django = models.BooleanField(default=False)
    analytics = models.BooleanField(default=False, verbose_name='Создание запросов для получения аналитики на основе естественного языка')
    platform = models.BooleanField(default=False, verbose_name='Разработка открытой платформы для мгновенного обмена сообщениями')
    students = models.BooleanField(default=False, verbose_name='Разработка моделей оценки студентов на основании открытых данных')
    web = models.BooleanField(default=False, verbose_name='Разработка механизма сборки и исполнения кода веб-приложения в рамках архитектуры micro frontend')
    mechanism = models.BooleanField(default=False, verbose_name='Разработка механизма сборки и исполнения кода мобильных приложений в рамках микросервисной архитектуры')
    mobile = models.BooleanField(default=False, verbose_name='Разработка мобильного приложения для автоматической фиксации участия в спортивных мероприятиях')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Персоны'
        verbose_name_plural = 'Персоны'