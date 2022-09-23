# Generated by Django 4.0.6 on 2022-09-02 21:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dromru', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.TextField(max_length=150, verbose_name='Тариф')),
            ],
        ),
        migrations.AddField(
            model_name='adsfilter',
            name='users_filters',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='adsfilter',
            name='create',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания'),
        ),
        migrations.AlterField(
            model_name='adsfilter',
            name='filter_word',
            field=models.CharField(blank=True, max_length=150, verbose_name='Слова которые должны быть'),
        ),
        migrations.AlterField(
            model_name='adsfilter',
            name='name_filter',
            field=models.CharField(max_length=50, verbose_name='Имя фильтра'),
        ),
        migrations.AlterField(
            model_name='adsfilter',
            name='no_price_skip',
            field=models.BooleanField(blank=True, default=False, verbose_name='Пропускать объявления бех цены(Y/N)'),
        ),
        migrations.AlterField(
            model_name='adsfilter',
            name='send_email',
            field=models.BooleanField(default=True, verbose_name='Отправка на E-mail(Y/N)'),
        ),
        migrations.AlterField(
            model_name='adsfilter',
            name='send_tg',
            field=models.BooleanField(default=False, verbose_name='Отправка в TG(Y/N)'),
        ),
        migrations.AlterField(
            model_name='adsfilter',
            name='stop_word',
            field=models.CharField(blank=True, max_length=150, verbose_name='Стоп слова'),
        ),
        migrations.AlterField(
            model_name='adsfilter',
            name='update',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата и время входа'),
        ),
        migrations.AlterField(
            model_name='adsfilter',
            name='url_filter',
            field=models.URLField(max_length=255, verbose_name='Ссылка на фильтр'),
        ),
        migrations.AlterField(
            model_name='adsfilter',
            name='recheck',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='dromru.price'),
        ),
    ]
