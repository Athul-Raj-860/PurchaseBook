# Generated by Django 5.1.4 on 2025-01-23 08:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0016_remove_payment_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='billing',
            name='Pay',
        ),
        migrations.AddField(
            model_name='billing',
            name='Book',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Book.book'),
        ),
        migrations.AddField(
            model_name='billing',
            name='User',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Book.register'),
        ),
    ]
