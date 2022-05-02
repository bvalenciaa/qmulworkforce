# Generated by Django 4.0.2 on 2022-03-15 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workforce', '0004_team_delete_project'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='members',
        ),
        migrations.AddField(
            model_name='team',
            name='members',
            field=models.ManyToManyField(to='workforce.User'),
        ),
    ]
