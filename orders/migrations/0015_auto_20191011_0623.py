# Generated by Django 2.2.5 on 2019-10-11 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0014_auto_20191010_0548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='price',
            field=models.CharField(max_length=100),
        ),
    ]
