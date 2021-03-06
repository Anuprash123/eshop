# Generated by Django 3.0.2 on 2021-03-10 05:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0005_auto_20210306_2243'),
    ]

    operations = [
        migrations.CreateModel(
            name='Place_Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('date', models.DateField()),
                ('Address', models.TextField(max_length=100)),
                ('zipcode', models.CharField(max_length=6)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Cart')),
                ('fruits', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Fruit')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
