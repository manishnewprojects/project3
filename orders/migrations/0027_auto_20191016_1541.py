# Generated by Django 2.2.5 on 2019-10-16 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0026_auto_20191016_0516'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='carts',
            new_name='food',
        ),
    ]
