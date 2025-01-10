

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='photo',
            field=models.ImageField(default='/templates/media/empty.png', upload_to='photo/%Y/%m/%d/', verbose_name='Image of room'),
        ),
    ]
