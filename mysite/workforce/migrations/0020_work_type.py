# Generated by Django 4.0.2 on 2022-04-23 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workforce', '0019_work'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='type',
            field=models.BooleanField(default=False),
        ),
    ]