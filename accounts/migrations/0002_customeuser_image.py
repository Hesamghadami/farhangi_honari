# Generated by Django 4.2.2 on 2024-01-26 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customeuser',
            name='image',
            field=models.ImageField(default='user.png', upload_to=''),
        ),
    ]
