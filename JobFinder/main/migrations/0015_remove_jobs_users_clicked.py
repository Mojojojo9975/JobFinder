# Generated by Django 4.2.3 on 2023-11-15 19:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_alter_jobs_options_jobs_is_clicked_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobs',
            name='users_clicked',
        ),
    ]
