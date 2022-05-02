# Generated by Django 4.0.2 on 2022-04-01 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workforce', '0009_upload'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
            ],
        ),
        migrations.AlterField(
            model_name='upload',
            name='title',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='upload',
            name='upload',
            field=models.FileField(upload_to=''),
        ),
    ]
