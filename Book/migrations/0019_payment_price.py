# Generated by Django 5.1.4 on 2025-01-30 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0018_book_user_register_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='Price',
            field=models.IntegerField(default=100),
        ),
    ]
