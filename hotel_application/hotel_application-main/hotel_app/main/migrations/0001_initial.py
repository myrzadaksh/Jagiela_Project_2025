

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BedSize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Bed Size')),
            ],
        ),
        migrations.CreateModel(
            name='HotelInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Hotel Name')),
                ('description', models.TextField(verbose_name='Hotel Description')),
                ('address', models.CharField(max_length=255, verbose_name='Hotel Address')),
                ('phone', models.CharField(max_length=20, verbose_name='Hotel Phone Number')),
            ],
        ),
        migrations.CreateModel(
            name='RoomType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Type of Room')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_number', models.CharField(max_length=10, unique=True, verbose_name='Room Number')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Room Price')),
                ('is_available', models.BooleanField(default=True, verbose_name='Room Status')),
                ('room_bed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.bedsize')),
                ('room_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.roomtype')),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_in', models.DateTimeField(verbose_name='Check in')),
                ('check_out', models.DateTimeField(verbose_name='Check out')),
                ('number_of_guests', models.PositiveIntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.room')),
            ],
        ),
    ]
