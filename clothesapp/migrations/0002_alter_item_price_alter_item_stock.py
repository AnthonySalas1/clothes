# Generated by Django 4.1.7 on 2023-02-22 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothesapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='item',
            name='stock',
            field=models.IntegerField(default=0),
        ),
    ]
