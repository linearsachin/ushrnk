# Generated by Django 3.1 on 2020-08-22 15:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShrnkUrl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('og_url', models.URLField()),
                ('shrnk_url_slug', models.TextField()),
                ('total_clicks', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'ShrnkUrls',
                'verbose_name_plural': 'ShrnkUrls',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Clicks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('clicks', models.IntegerField()),
                ('shrnk_url', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.shrnkurl')),
            ],
            options={
                'verbose_name': 'Clicks',
                'verbose_name_plural': 'Clickss',
                'db_table': '',
                'managed': True,
            },
        ),
    ]
