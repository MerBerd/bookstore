# Generated by Django 3.2.7 on 2022-03-19 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0014_auto_20220319_2127'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='Active',
            field=models.BooleanField(default=True),
        ),
    ]