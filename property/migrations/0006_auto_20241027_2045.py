# Generated by Django 2.2.24 on 2024-10-27 17:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0005_complaint'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='decription',
            field=models.TextField(blank=True, null=True, verbose_name='Текст жалобы'),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='flat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='property.Flat', verbose_name='Квартира на которую подали жалобу'),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='user_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь подавший жалобу'),
        ),
    ]
