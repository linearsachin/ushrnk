# Generated by Django 3.1 on 2020-08-22 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shrnkurl',
            name='shrnk_url_slug',
            field=models.CharField(max_length=10),
        ),
    ]
