# Generated by Django 3.1.4 on 2021-03-11 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20210311_1836'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='delivery',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Телефон'),
        ),
    ]