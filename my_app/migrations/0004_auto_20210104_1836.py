# Generated by Django 3.1.4 on 2021-01-04 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0003_wishlist_item_namesss'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wishlist',
            name='item_namesss',
        ),
        migrations.AddField(
            model_name='wishlist',
            name='expected_price',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]
