# Generated by Django 4.1.1 on 2022-09-26 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bugs',
            name='fixed',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]