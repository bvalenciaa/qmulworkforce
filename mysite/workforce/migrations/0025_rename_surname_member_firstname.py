# Generated by Django 4.0.2 on 2022-04-24 00:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workforce', '0024_member_surname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='surname',
            new_name='firstname',
        ),
    ]
