# Generated by Django 3.0.3 on 2020-03-11 19:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0005_auto_20200311_1527'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': 'Тег', 'verbose_name_plural': 'Теги'},
        ),
        migrations.AddField(
            model_name='category',
            name='is_active',
            field=models.BooleanField(db_index=True, default=True, verbose_name='Отображать ?'),
        ),
        migrations.AddField(
            model_name='category',
            name='is_in_index_catalog',
            field=models.BooleanField(db_index=True, default=False, verbose_name='Показывать в каталоге на главной ?'),
        ),
        migrations.AlterField(
            model_name='item',
            name='tag',
            field=models.ManyToManyField(blank=True, db_index=True, to='item.Tag', verbose_name='Теги'),
        ),
        migrations.AlterField(
            model_name='itemimage',
            name='image',
            field=models.ImageField(blank=True, upload_to='items/', verbose_name='Изображение товара'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subcategory', to='item.Category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='item.Category', verbose_name='Относится к категории'),
        ),
    ]