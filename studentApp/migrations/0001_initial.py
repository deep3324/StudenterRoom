# Generated by Django 3.0 on 2022-06-12 07:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(default='', max_length=300)),
                ('email', models.EmailField(default='', max_length=300)),
                ('phone', models.CharField(default='', max_length=300)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(default='', max_length=300)),
                ('email', models.EmailField(default='', max_length=300)),
                ('phone', models.CharField(default='', max_length=300)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('Mess', 'Mess'), ('PG', 'PG'), ('Hostels', 'Hostels'), ('Flat', 'Flat')], max_length=50)),
                ('propertyName', models.CharField(default='', max_length=300)),
                ('registrationTime', models.DateTimeField(auto_now_add=True)),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='studentApp.Owner')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookedFor', models.CharField(choices=[('Mess', 'Mess'), ('PG', 'PG'), ('Hostels', 'Hostels'), ('Flat', 'Flat')], max_length=50)),
                ('bookingTime', models.DateTimeField(auto_now_add=True)),
                ('propertyName', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='studentApp.Property')),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='studentApp.Student')),
            ],
        ),
    ]
