# Generated by Django 3.0.5 on 2020-04-08 11:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20200408_1225'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quiz',
            old_name='id',
            new_name='tag',
        ),
    ]
