# Generated by Django 3.0.3 on 2020-03-27 08:10

import customuser.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('item', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session', models.CharField(blank=True, max_length=255, null=True, verbose_name='Ключ сессии')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Эл. почта')),
                ('fio', models.CharField(blank=True, max_length=50, null=True, verbose_name='ФИО')),
                ('phone', models.CharField(blank=True, max_length=50, null=True, verbose_name='Телефон')),
                ('used_promo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='item.PromoCode', verbose_name='Использованный промо-код при текущей корзине')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Эл. почта')),
                ('is_vip', models.BooleanField(default=False, verbose_name='Вип?')),
                ('fio', models.CharField(blank=True, max_length=50, null=True, verbose_name='ФИО')),
                ('phone', models.CharField(blank=True, max_length=50, null=True, verbose_name='Телефон')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Комментарий')),
                ('is_allow_email', models.BooleanField(default=True, verbose_name='Согласен на рассылку')),
                ('profile_ok', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('used_promo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='item.PromoCode', verbose_name='Использованный промо-код при текущей корзине')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', customuser.models.UserManager()),
            ],
        ),
    ]
