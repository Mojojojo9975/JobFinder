# Generated by Django 4.2.3 on 2023-10-21 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_alter_scholarships_degree'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobs',
            name='category',
            field=models.CharField(default='-', max_length=150),
        ),
    ]
