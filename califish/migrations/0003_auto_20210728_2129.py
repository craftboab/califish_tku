# Generated by Django 3.1.13 on 2021-07-29 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('califish', '0002_auto_20210727_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='picture',
            field=models.ImageField(blank=True, upload_to='media/images/'),
        ),
    ]
