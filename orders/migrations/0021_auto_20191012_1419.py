# Generated by Django 2.2.5 on 2019-10-12 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0020_auto_20191012_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='flavor',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='food',
            name='size',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
    ]
