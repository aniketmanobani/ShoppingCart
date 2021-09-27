# Generated by Django 3.2.7 on 2021-09-17 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=500)),
                ('pubdate', models.DateField()),
            ],
        ),
    ]
