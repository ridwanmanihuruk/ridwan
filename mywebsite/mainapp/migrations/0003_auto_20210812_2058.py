# Generated by Django 3.2.6 on 2021-08-12 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20210812_2024'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='color',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='picture',
            field=models.ImageField(default=None, upload_to=''),
            preserve_default=False,
        ),
    ]
