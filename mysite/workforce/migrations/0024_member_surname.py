# Generated by Django 4.0.2 on 2022-04-24 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workforce', '0023_alter_member_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='surname',
            field=models.CharField(max_length=200, null=True),
        ),
    ]