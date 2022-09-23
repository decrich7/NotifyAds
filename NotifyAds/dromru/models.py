# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User


class AdsFilter(models.Model):
    name_filter = models.CharField(max_length=50, verbose_name='Имя фильтра')
    url_filter = models.URLField(max_length=255, verbose_name='Ссылка на фильтр')
    recheck = models.ForeignKey('Price', on_delete=models.PROTECT, null=True, verbose_name='Период проверки')
    send_email = models.BooleanField(default=True, verbose_name='Отправка на E-mail')
    send_tg = models.BooleanField(default=False, verbose_name='Отправка в TG')
    stop_word = models.CharField(max_length=150, blank=True, verbose_name='Стоп слова (Через пробел)')
    filter_word = models.CharField(max_length=150, blank=True,
                                   verbose_name='Слова которые должны быть в объявлении (Через пробел)')
    no_price_skip = models.BooleanField(blank=True, default=False, verbose_name='Пропускать объявления без цены')
    default_start = models.BooleanField(default=True, verbose_name='Запуск')
    create = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')
    update = models.DateTimeField(auto_now=True, verbose_name='Дата и время входа')
    users_filters = models.ForeignKey(User, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.name_filter


class Price(models.Model):
    rate = models.TextField(max_length=150, verbose_name="Тариф")

    def __str__(self):
        return self.rate


class TelegramUser(models.Model):
    tg = models.TextField(max_length=50,blank=True, verbose_name="Телеграм")
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.tg
