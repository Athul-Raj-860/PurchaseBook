# Generated by Django 5.1.4 on 2024-12-31 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='Description',
            field=models.TextField(),
        ),
    ]
