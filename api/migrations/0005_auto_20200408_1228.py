# Generated by Django 3.0.5 on 2020-04-08 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20200408_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='tag',
            field=models.PositiveIntegerField(primary_key=True, serialize=False),
        ),
    ]
