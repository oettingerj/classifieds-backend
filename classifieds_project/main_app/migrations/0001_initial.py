# Generated by Django 3.0.3 on 2020-03-03 06:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
#        ('main_app'),
    ]

    operations = [
        migrations.CreateModel(
            name='Posting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timePosted', models.DateTimeField()),
                ('category', models.CharField(max_length=240)),
                ('prospective', models.BooleanField()),
                ('fulfilled', models.BooleanField()),
                ('description', models.TextField()),
                ('audience', models.CharField(choices=[('STUDENT', 'Student'), ('FACULTY', 'Faculty'), ('STAFF', 'Staff'), ('ALL', 'All')], max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=240, verbose_name='Name')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('role', models.CharField(choices=[('STUDENT', 'Student'), ('FACULTY', 'Faculty'), ('STAFF', 'Staff'), ('ALL', 'All')], max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='RidePosting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateTimeOfRide', models.DateTimeField()),
                ('startLocation', models.TextField()),
                ('endLocation', models.TextField()),
                ('numberOfPeople', models.IntegerField()),
                ('posting', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='main_app.Posting')),
            ],
        ),
        migrations.AddField(
            model_name='posting',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main_app.User'),
        ),
        migrations.CreateModel(
            name='ItemPosting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(blank=True, upload_to='')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('forSale', models.BooleanField()),
                ('forLoan', models.BooleanField()),
                ('posting', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='main_app.Posting')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timePosted', models.DateTimeField()),
                ('content', models.TextField()),
                ('posting', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main_app.Posting')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main_app.User')),
            ],
        ),
    ]