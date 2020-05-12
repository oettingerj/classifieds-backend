# Generated by Django 3.0.6 on 2020-05-12 00:38

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0005_ridelisting_sold'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemlisting',
            name='savedBy',
        ),
        migrations.RemoveField(
            model_name='ridelisting',
            name='savedBy',
        ),
        migrations.AddField(
            model_name='itemlisting',
            name='likedBy',
            field=models.ManyToManyField(related_name='likedItems', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='ridelisting',
            name='likedBy',
            field=models.ManyToManyField(related_name='likedRides', to=settings.AUTH_USER_MODEL),
        ),
    ]