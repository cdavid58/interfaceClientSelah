# Generated by Django 3.2.8 on 2023-02-25 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resident', '0002_alter_resident_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='resident',
            name='photo',
            field=models.ImageField(default='Profile/photo.png', upload_to='Profile'),
        ),
    ]
