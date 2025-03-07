# Generated by Django 5.1.4 on 2025-01-20 10:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0006_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Book.book')),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Book.register')),
            ],
            options={
                'db_table': 'Wishlist',
            },
        ),
    ]
