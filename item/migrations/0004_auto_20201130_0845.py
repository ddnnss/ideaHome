# Generated by Django 3.1 on 2020-11-30 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0003_auto_20200423_2010'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('order_num',), 'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='subcategory',
            options={'ordering': ('order_num',), 'verbose_name': 'Подкатегория', 'verbose_name_plural': 'Подкатегории'},
        ),
        migrations.AddField(
            model_name='category',
            name='manufactor',
            field=models.ManyToManyField(blank=True, related_name='manufactors', to='item.Manufactor', verbose_name='Производители'),
        ),
    ]
