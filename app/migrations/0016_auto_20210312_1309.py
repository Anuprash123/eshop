# Generated by Django 3.0.2 on 2021-03-12 07:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_auto_20210312_1306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Cart'),
        ),
    ]
