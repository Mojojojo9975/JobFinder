# Generated by Django 4.2.3 on 2023-10-01 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_jobs_location_alter_jobs_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='publish_date',
            field=models.CharField(max_length=20),
        ),
    ]
