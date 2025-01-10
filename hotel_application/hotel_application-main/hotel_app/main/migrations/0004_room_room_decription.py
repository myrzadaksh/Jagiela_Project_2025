

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_room_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='room_decription',
            field=models.TextField(default=False, verbose_name='Room Description'),
        ),
    ]
