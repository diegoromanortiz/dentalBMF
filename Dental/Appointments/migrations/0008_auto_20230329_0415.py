# Generated by Django 2.2.24 on 2023-03-29 04:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Appointments', '0007_auto_20230329_0045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='hour',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Hour.Hour'),
        ),
    ]
