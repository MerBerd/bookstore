# Generated by Django 3.2.7 on 2022-03-08 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0007_alter_book_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='FirstName',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='LastName',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='Patronymic',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]