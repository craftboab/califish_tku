# Generated by Django 3.1.13 on 2021-07-29 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('califish', '0005_auto_20210729_1403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
