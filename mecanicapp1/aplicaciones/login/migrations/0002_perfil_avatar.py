# Generated by Django 3.0.7 on 2020-07-17 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='users/%Y/%m/%d'),
        ),
    ]
