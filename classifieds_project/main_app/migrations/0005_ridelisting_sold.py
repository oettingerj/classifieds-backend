# Generated by Django 3.0.2 on 2020-05-11 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_auto_20200511_1907'),
    ]

    operations = [
        migrations.AddField(
            model_name='ridelisting',
            name='sold',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
