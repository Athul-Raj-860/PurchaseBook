# Generated by Django 5.1.4 on 2025-01-21 14:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0009_wishlist_heart_on'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='heart_on',
        ),
        migrations.RemoveField(
            model_name='wishlist',
            name='heart_on',
        ),
    ]
