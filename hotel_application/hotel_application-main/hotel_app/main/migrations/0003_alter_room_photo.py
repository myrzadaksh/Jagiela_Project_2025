

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_room_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='photo',
            field=models.ImageField(default='/photo/2024/06/14/empty.png', upload_to='photo/%Y/%m/%d/', verbose_name='Image of room'),
        ),
    ]
