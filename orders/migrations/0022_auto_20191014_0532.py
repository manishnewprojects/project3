# Generated by Django 2.2.5 on 2019-10-14 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0021_auto_20191012_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sub',
            name='name',
            field=models.CharField(max_length=40),
        ),
    ]
