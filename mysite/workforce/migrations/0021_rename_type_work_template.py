# Generated by Django 4.0.2 on 2022-04-23 01:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workforce', '0020_work_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='work',
            old_name='type',
            new_name='template',
        ),
    ]
