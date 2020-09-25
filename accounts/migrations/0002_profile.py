# Generated by Django 3.1.1 on 2020-09-25 07:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('selfie_image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('bio', models.CharField(default=None, max_length=500)),
                ('headline', models.CharField(default=None, max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
