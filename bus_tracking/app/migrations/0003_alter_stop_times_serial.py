# Generated by Django 5.0.1 on 2024-01-12 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_stop_times_days'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stop_times',
            name='serial',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
