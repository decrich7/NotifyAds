# Generated by Django 4.0.6 on 2022-08-31 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdsFilter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_filter', models.CharField(max_length=50)),
                ('url_filter', models.URLField(max_length=255)),
                ('recheck', models.CharField(max_length=50)),
                ('send_email', models.BooleanField(default=True)),
                ('send_tg', models.BooleanField(default=False)),
                ('stop_word', models.CharField(blank=True, max_length=150)),
                ('filter_word', models.CharField(blank=True, max_length=150)),
                ('no_price_skip', models.BooleanField(blank=True, default=False)),
                ('create', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
