# Generated by Django 4.2.3 on 2023-08-18 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_profile_address_alter_profile_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profileImage',
            field=models.ImageField(blank=True, default='avatar.jpg', null=True, upload_to='profilePics'),
        ),
    ]
