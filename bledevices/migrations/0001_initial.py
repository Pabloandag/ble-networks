# Generated by Django 4.0.4 on 2022-04-23 23:18

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BleDeviceType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(2, 'Name must be greater than 1 character')])),
            ],
        ),
        migrations.CreateModel(
            name='BleNetwork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('active', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='BleDevice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.CharField(max_length=200, validators=[django.core.validators.MinLengthValidator(5, 'Identifier must be greater than 4 characters')])),
                ('friendly_name', models.CharField(max_length=200, validators=[django.core.validators.MinLengthValidator(2, 'Friendly name must be greater than 1 character')])),
                ('mac', models.CharField(max_length=17, validators=[django.core.validators.RegexValidator(message='Expected format is AA:BB:CC:DD:EE:FF', regex='^([0-9A-F]{2}:){5}([0-9A-Fa-f]{2})|([0-9A-F]{4}\\.[0-9A-F]{4}\\.[0-9A-F]{4})$')])),
                ('active', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('device_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bledevices.bledevicetype')),
                ('network', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bledevices.blenetwork')),
            ],
        ),
    ]
