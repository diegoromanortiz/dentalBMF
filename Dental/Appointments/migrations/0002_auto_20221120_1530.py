# Generated by Django 2.2.24 on 2022-11-20 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Appointments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='hour',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
