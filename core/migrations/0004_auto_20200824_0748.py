# Generated by Django 3.1 on 2020-08-24 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20200822_2039'),
    ]

    operations = [
        migrations.AddField(
            model_name='shrnkurl',
            name='xcode',
            field=models.CharField(blank=True, max_length=5, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='shrnkurl',
            name='shrnk_url_slug',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
