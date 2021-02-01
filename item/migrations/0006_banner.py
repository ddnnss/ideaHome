# Generated by Django 3.1.4 on 2021-01-18 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0005_auto_20201130_0857'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='images/banners/', verbose_name='Баннер')),
                ('text', models.CharField(blank=True, max_length=255, null=True, verbose_name='Текст')),
                ('btn_text', models.CharField(blank=True, max_length=255, null=True, verbose_name='Текст на кнопке')),
                ('btn_url', models.CharField(blank=True, max_length=255, null=True, verbose_name='Ссылка на кнопке')),
                ('is_active', models.BooleanField(default=True, verbose_name='Отображается')),
                ('at_home_page', models.BooleanField(default=True, verbose_name='На главной')),
                ('at_sale_page', models.BooleanField(default=True, verbose_name='На акциях')),
            ],
            options={
                'verbose_name': 'Баннер',
                'verbose_name_plural': 'Баннеры',
            },
        ),
    ]
