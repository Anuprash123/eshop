# Generated by Django 3.0.2 on 2021-03-06 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20210306_2242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]