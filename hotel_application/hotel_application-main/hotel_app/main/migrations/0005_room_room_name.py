

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_room_room_decription'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='room_name',
            field=models.CharField(default=False, max_length=100, verbose_name='Room Name'),
        ),
    ]
