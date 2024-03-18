# Generated by Django 4.2.3 on 2023-08-18 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_rename_userprofile_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='address',
            field=models.CharField(default='xyz', max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.CharField(default='xyz@abc.com', max_length=70),
        ),
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(default='xyz', max_length=30),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(default='12345678', max_length=13),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profession',
            field=models.CharField(default='xyz', max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profileImage',
            field=models.ImageField(blank=True, default='avatar.jpg', null=True, upload_to='media'),
        ),
    ]