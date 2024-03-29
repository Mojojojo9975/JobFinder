# Generated by Django 4.2.3 on 2023-08-14 17:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='userProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profession', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=70)),
                ('phone', models.CharField(max_length=13)),
                ('address', models.CharField(max_length=100)),
                ('profileImage', models.ImageField(blank=True, default='https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-chat/ava3.webp', null=True, upload_to='images')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
