# Generated by Django 2.2.5 on 2019-10-04 06:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_auto_20191004_0607'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Dinner_Platters',
            new_name='Dinner_Platter',
        ),
        migrations.RenameModel(
            old_name='Salads',
            new_name='Salad',
        ),
        migrations.RenameModel(
            old_name='Subs',
            new_name='Sub',
        ),
    ]
