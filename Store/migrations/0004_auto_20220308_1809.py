# Generated by Django 3.2.7 on 2022-03-08 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0003_auto_20220308_1801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='FirstName',
            field=models.CharField(blank=True, default='', max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='LastName',
            field=models.CharField(blank=True, default='', max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='Patronymic',
            field=models.CharField(blank=True, default='', max_length=64, null=True),
        ),
    ]
