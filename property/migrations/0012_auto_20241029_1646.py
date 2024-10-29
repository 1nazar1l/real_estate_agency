# Generated by Django 2.2.24 on 2024-10-29 13:46

from django.db import migrations
import phonenumbers

def update_phonenumbers(apps, schema_editor):
    flats = apps.get_model('property', 'Flat')
    for flat in flats.objects.all():
        x = phonenumbers.parse(flat.owners_phonenumber, "RU")
        flat.owner_pure_phone = x

class Migration(migrations.Migration):

    dependencies = [
        ('property', '0011_auto_20241029_1624'),
    ]

    operations = [
        migrations.RunPython(update_phonenumbers)
    ]