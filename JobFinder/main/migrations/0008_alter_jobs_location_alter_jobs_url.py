# Generated by Django 4.2.3 on 2023-09-26 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_profile_profileimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='location',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='url',
            field=models.CharField(max_length=400),
        ),
    ]
