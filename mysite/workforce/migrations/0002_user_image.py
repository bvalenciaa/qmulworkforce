# Generated by Django 4.0.2 on 2022-02-13 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workforce', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, default='workforce/static/workforce/default_profile.jpg', upload_to='workforce/static/workforce'),
        ),
    ]
