# Generated by Django 5.1.4 on 2025-01-06 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0003_alter_book_published'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('User_Id', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=255)),
                ('Email', models.CharField(max_length=255)),
                ('Number', models.CharField(max_length=255)),
                ('Username', models.CharField(max_length=255)),
                ('Password', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'Register',
            },
        ),
    ]
