# Generated by Django 3.1 on 2020-08-22 15:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200822_2038'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Clicks',
            new_name='Click',
        ),
        migrations.AlterModelOptions(
            name='click',
            options={'managed': True, 'verbose_name': 'Click', 'verbose_name_plural': 'Clicks'},
        ),
    ]
