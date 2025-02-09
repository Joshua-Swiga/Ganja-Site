# Generated by Django 3.2.10 on 2024-05-31 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0002_auto_20240530_2217'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quality_shelf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('product_price', models.IntegerField()),
                ('product_currency', models.CharField(max_length=100)),
                ('product_image', models.ImageField(upload_to='product_information/quality_shelf')),
            ],
        ),
    ]
